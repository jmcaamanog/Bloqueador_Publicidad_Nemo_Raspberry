#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servicio Maestro de Pantalla OLED 1.3" (SH1106/SSD1306) + 2 Botones + 2 LEDs
Para: Bloqueador_Publicidad_Nemo_Raspberry
Autor: Jose Manuel Caamaño González
"""

import time
import subprocess
import os
import sys
import json
import urllib.request
from datetime import datetime

try:
    from PIL import Image, ImageDraw, ImageFont
    from luma.core.interface.serial import i2c
    from luma.oled.device import sh1106, ssd1306
    import RPi.GPIO as GPIO
except ImportError:
    print("Aviso: Librerías luma.oled / RPi.GPIO no disponibles en local. Modo Simulación.")

# --- Configuración de Pines GPIO ---
PIN_BTN_NAV = 17   # Botón 1: Navegación / Sleep (Pin 11)
PIN_BTN_CTRL = 27  # Botón 2: Bypass / Safe Poweroff (Pin 13)
PIN_LED_GREEN = 22 # LED Verde: Escudo Activo (Pin 15)
PIN_LED_RED = 23   # LED Rojo: Bypass / Alerta (Pin 16)

class NemoDisplayManager:
    def __init__(self):
        self.current_screen = 0
        self.total_screens = 4
        self.screen_on = True
        self.bypass_until = 0
        self.width = 128
        self.height = 64
        
        # Inicializar GPIO
        try:
            GPIO.setmode(GPIO.BCM)
            GPIO.setwarnings(False)
            GPIO.setup(PIN_BTN_NAV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(PIN_BTN_CTRL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(PIN_LED_GREEN, GPIO.OUT)
            GPIO.setup(PIN_LED_RED, GPIO.OUT)
            
            # Inicializar OLED (SH1106 1.3" por defecto)
            serial = i2c(port=1, address=0x3C)
            self.device = sh1106(serial, width=128, height=64)
        except Exception as e:
            self.device = None
            print(f"Modo emulado sin hardware GPIO: {e}")

        # Fuentes
        try:
            self.font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
            self.font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
            self.font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
        except Exception:
            self.font_title = ImageFont.load_default()
            self.font_body = ImageFont.load_default()
            self.font_large = ImageFont.load_default()

    def get_system_stats(self):
        # IP Local
        try:
            ip = subprocess.check_output("hostname -I", shell=True).decode('utf-8').split()[0]
        except Exception:
            ip = "127.0.0.1"

        # Temperatura CPU
        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp = float(f.read().strip()) / 1000.0
        except Exception:
            temp = 0.0

        # Stats de Pi-hole vía API local
        stats = {
            "queries": 0,
            "blocked": 0,
            "percent": 0.0,
            "clients": 0,
            "status": "enabled"
        }
        try:
            req = urllib.request.urlopen("http://127.0.0.1/api/stats/summary", timeout=2)
            data = json.loads(req.read().decode('utf-8'))
            stats["queries"] = data.get("queries", {}).get("total", 0)
            stats["blocked"] = data.get("queries", {}).get("blocked", 0)
            stats["percent"] = data.get("queries", {}).get("percent_blocked", 0.0)
            stats["clients"] = data.get("clients", {}).get("active", 0)
            stats["status"] = data.get("status", "enabled")
        except Exception:
            pass

        return ip, temp, stats

    def draw_screen_dashboard(self, draw, ip, temp, stats):
        draw.text((0, 0), "🐶 NEMO GUARD 🛡️", font=self.font_title, fill=255)
        draw.line((0, 11, 128, 11), fill=255)
        draw.text((0, 14), f"IP: {ip}", font=self.font_body, fill=255)
        draw.text((0, 26), f"Bloqueo: {stats['percent']:.1f}% ({stats['blocked']})", font=self.font_body, fill=255)
        draw.text((0, 38), f"Total Queries: {stats['queries']}", font=self.font_body, fill=255)
        draw.text((0, 50), f"Temp: {temp:.1f}°C | Clis: {stats['clients']}", font=self.font_body, fill=255)

    def draw_screen_bypass(self, draw, remaining):
        draw.text((0, 0), "⚠️ MODO BYPASS ⚠️", font=self.font_title, fill=255)
        draw.line((0, 11, 128, 11), fill=255)
        draw.text((10, 20), "Filtrado en Pausa", font=self.font_body, fill=255)
        draw.text((20, 35), f"{remaining // 60:02d}:{remaining % 60:02d} min", font=self.font_large, fill=255)
        draw.text((5, 52), "Pulsa B para reactivar", font=self.font_body, fill=255)

    def update_leds(self, is_bypass):
        try:
            if is_bypass:
                GPIO.output(PIN_LED_GREEN, GPIO.LOW)
                GPIO.output(PIN_LED_RED, GPIO.HIGH)
            else:
                GPIO.output(PIN_LED_GREEN, GPIO.HIGH)
                GPIO.output(PIN_LED_RED, GPIO.LOW)
        except Exception:
            pass

    def run(self):
        print("Iniciando servicio Nemo Display Manager...")
        while True:
            ip, temp, stats = self.get_system_stats()
            now = time.time()
            is_bypass = now < self.bypass_until
            
            self.update_leds(is_bypass)
            
            if self.device and self.screen_on:
                image = Image.new("1", (self.width, self.height))
                draw = ImageDraw.Draw(image)
                
                if is_bypass:
                    remaining = int(self.bypass_until - now)
                    self.draw_screen_bypass(draw, remaining)
                else:
                    self.draw_screen_dashboard(draw, ip, temp, stats)
                
                self.device.display(image)

            time.sleep(1)

if __name__ == "__main__":
    mgr = NemoDisplayManager()
    mgr.run()
