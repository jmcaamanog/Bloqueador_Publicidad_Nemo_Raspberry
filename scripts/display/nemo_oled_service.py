#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Servicio Maestro de Pantalla OLED 1.3" (SH1106) + 2 Botones + LED Direccionable WS2812B (NeoPixel)
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
    from luma.oled.device import sh1106
    import RPi.GPIO as GPIO
    from rpi_ws281x import PixelStrip, Color
    HAS_HARDWARE = True
except ImportError:
    HAS_HARDWARE = False
    print("Aviso: Librerías luma.oled / rpi_ws281x no disponibles en local. Modo Simulación.")

# --- Configuración de Pines GPIO ---
PIN_BTN_NAV = 17   # Botón 1: Navegación / Sleep (Pin 11)
PIN_BTN_CTRL = 27  # Botón 2: Bypass / Safe Poweroff (Pin 13)

# --- Configuración LED WS2812B (NeoPixel) ---
LED_COUNT = 1          # 1 LED individual (o tira en la carcasa)
LED_PIN = 18           # GPIO 18 / Pin 12 (PWM por hardware)
LED_FREQ_HZ = 800000   # Frecuencia de señal LED (800khz)
LED_DMA = 10           # Canal DMA para generar señal
LED_BRIGHTNESS = 64    # Brillo (0 a 255)
LED_INVERT = False     # False para no invertir señal

# Colores predefinidos WS2812B (G, R, B)
COLOR_OFF = (0, 0, 0)
COLOR_GREEN = (0, 255, 0)      # Escudo activo
COLOR_ORANGE = (255, 120, 0)   # Modo Bypass
COLOR_BLUE = (0, 150, 255)     # Actividad DNS
COLOR_RED = (255, 0, 0)        # Alerta / Error
COLOR_PURPLE = (180, 0, 255)   # Mantenimiento

class NemoDisplayManager:
    def __init__(self):
        self.current_screen = 0
        self.screen_on = True
        self.bypass_until = 0
        self.width = 128
        self.height = 64
        
        if HAS_HARDWARE:
            try:
                GPIO.setmode(GPIO.BCM)
                GPIO.setwarnings(False)
                GPIO.setup(PIN_BTN_NAV, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                GPIO.setup(PIN_BTN_CTRL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
                
                # Inicializar OLED 1.3"
                serial = i2c(port=1, address=0x3C)
                self.device = sh1106(serial, width=128, height=64)
                
                # Inicializar WS2812B
                self.strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
                self.strip.begin()
            except Exception as e:
                self.device = None
                self.strip = None
                print(f"Error hardware: {e}")
        else:
            self.device = None
            self.strip = None

        # Fuentes
        try:
            self.font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
            self.font_body = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 9)
            self.font_large = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 14)
        except Exception:
            self.font_title = ImageFont.load_default()
            self.font_body = ImageFont.load_default()
            self.font_large = ImageFont.load_default()

    def set_ws2812b_color(self, r, g, b):
        if self.strip:
            try:
                self.strip.setPixelColor(0, Color(r, g, b))
                self.strip.show()
            except Exception:
                pass

    def get_system_stats(self):
        try:
            ip = subprocess.check_output("hostname -I", shell=True).decode('utf-8').split()[0]
        except Exception:
            ip = "127.0.0.1"

        try:
            with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
                temp = float(f.read().strip()) / 1000.0
        except Exception:
            temp = 0.0

        stats = {"queries": 0, "blocked": 0, "percent": 0.0, "clients": 0}
        try:
            req = urllib.request.urlopen("http://127.0.0.1/api/stats/summary", timeout=2)
            data = json.loads(req.read().decode('utf-8'))
            stats["queries"] = data.get("queries", {}).get("total", 0)
            stats["blocked"] = data.get("queries", {}).get("blocked", 0)
            stats["percent"] = data.get("queries", {}).get("percent_blocked", 0.0)
            stats["clients"] = data.get("clients", {}).get("active", 0)
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

    def run(self):
        print("Iniciando servicio Nemo Display Manager (WS2812B Edition)...")
        while True:
            ip, temp, stats = self.get_system_stats()
            now = time.time()
            is_bypass = now < self.bypass_until
            
            # Control de Color WS2812B
            if is_bypass:
                self.set_ws2812b_color(*COLOR_ORANGE)
            elif temp > 65.0:
                self.set_ws2812b_color(*COLOR_RED)
            else:
                self.set_ws2812b_color(*COLOR_GREEN)
            
            # Dibujado OLED
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
