#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Despliegue y Actualización Automática a la Raspberry Pi Zero
Para: Bloqueador_Publicidad_Nemo_Raspberry
Autor: Jose Manuel Caamaño González
"""

import paramiko
import os
import sys
import time

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PI_IP = os.getenv("PI_IP", "192.168.0.23")
PI_USER = os.getenv("PI_USER", "jose")
PI_PASS = os.getenv("PI_PASS", "josejosejose1")

print(f"🚀 Conectando a la Raspberry Pi Zero ({PI_IP})...")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(PI_IP, username=PI_USER, password=PI_PASS, timeout=15)
    print("✅ Conexión SSH establecida con éxito.")
except Exception as e:
    print(f"❌ Error de conexión: {e}")
    sys.exit(1)

def run(cmd, desc=""):
    if desc:
        print(f"\n---> {desc}")
    stdin, stdout, stderr = ssh.exec_command(f"echo {PI_PASS} | sudo -S {cmd}")
    out = stdout.read().decode('utf-8', errors='ignore').strip()
    if out:
        print(out)
    err = stderr.read().decode('utf-8', errors='ignore').strip()
    if err and "password for jose" not in err:
        print("ERR:", err[:300])

# 1. Habilitar I2C para la pantalla OLED
run("raspi-config nonint do_i2c 0", "Habilitando módulo I2C del Kernel...")

# 2. Instalar dependencias del sistema
run("apt-get update && apt-get install -y i2c-tools python3-pil python3-rpi.gpio python3-pip git", "Instalando paquetes del sistema...")

# 3. Instalar librerías de hardware en Python (WS2812B y OLED)
run("pip3 install rpi_ws281x luma.oled --break-system-packages", "Instalando librerías Python (rpi_ws281x, luma.oled)...")

# 4. Crear directorio /opt/nemo y clonar/sincronizar el repositorio
run("mkdir -p /opt/nemo && chown -R jose:jose /opt/nemo", "Preparando directorio /opt/nemo...")

# Subir scripts locales por SFTP
sftp = ssh.open_sftp()
local_display_script = os.path.join(os.path.dirname(__file__), "display", "nemo_oled_service.py")
if os.path.exists(local_display_script):
    run("mkdir -p /opt/nemo/scripts/display", "Creando rutas remotas...")
    sftp.put(local_display_script, "/opt/nemo/scripts/display/nemo_oled_service.py")
    print("✅ Script nemo_oled_service.py transferido a /opt/nemo.")

local_telegram_script = os.path.join(os.path.dirname(__file__), "telegram", "nemo_telegram_bot.py")
if os.path.exists(local_telegram_script):
    run("mkdir -p /opt/nemo/scripts/telegram", "Creando rutas remotas...")
    sftp.put(local_telegram_script, "/opt/nemo/scripts/telegram/nemo_telegram_bot.py")
    print("✅ Script nemo_telegram_bot.py transferido a /opt/nemo.")

local_service = os.path.join(os.path.dirname(__file__), "..", "systemd", "nemo-display.service")
if os.path.exists(local_service):
    sftp.put(local_service, "/tmp/nemo-display.service")
    run("cp /tmp/nemo-display.service /etc/systemd/system/nemo-display.service && systemctl daemon-reload && systemctl enable nemo-display.service", "Instalando servicio systemd...")
    print("✅ Servicio nemo-display.service registrado en systemd.")

sftp.close()

# 5. Comprobar bus I2C
run("i2cdetect -y 1", "Escaneando dispositivos I2C...")

ssh.close()
print("\n🎉 ¡ACTUALIZACIÓN Y DESPLIEGUE EN LA RASPBERRY PI ZERO COMPLETADOS CON ÉXITO!")
