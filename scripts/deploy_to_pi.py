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

def get_ssh_client():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    for attempt in range(5):
        try:
            ssh.connect(PI_IP, username=PI_USER, password=PI_PASS, timeout=20)
            return ssh
        except Exception as e:
            print(f"Reintentando conexión ({attempt+1}/5): {e}")
            time.sleep(3)
    return None

def run_command(cmd, desc=""):
    if desc:
        print(f"\n---> {desc}")
    ssh = get_ssh_client()
    if not ssh:
        print(f"❌ No se pudo conectar a {PI_IP}")
        return False
    try:
        stdin, stdout, stderr = ssh.exec_command(f"echo {PI_PASS} | sudo -S {cmd}", timeout=300)
        out = stdout.read().decode('utf-8', errors='ignore').strip()
        if out:
            print(out)
        err = stderr.read().decode('utf-8', errors='ignore').strip()
        if err and "password for jose" not in err:
            print("ERR:", err[:300])
        ssh.close()
        return True
    except Exception as e:
        print(f"Error ejecutando '{cmd}': {e}")
        ssh.close()
        return False

print(f"🚀 Iniciando despliegue en Raspberry Pi Zero ({PI_IP})...")

# 1. Habilitar I2C
run_command("raspi-config nonint do_i2c 0", "Habilitando módulo I2C del Kernel...")

# 2. Instalar dependencias del sistema
run_command("apt-get update && apt-get install -y i2c-tools python3-pil python3-rpi.gpio python3-pip git", "Instalando paquetes del sistema...")

# 3. Instalar librerías de hardware en Python (WS2812B y OLED)
run_command("pip3 install rpi_ws281x luma.oled --break-system-packages", "Instalando librerías Python (rpi_ws281x, luma.oled)...")

# 4. Crear directorios y copiar scripts
run_command("mkdir -p /opt/nemo/scripts/display /opt/nemo/scripts/telegram && chown -R jose:jose /opt/nemo", "Preparando directorio /opt/nemo...")

ssh = get_ssh_client()
if ssh:
    sftp = ssh.open_sftp()
    
    local_display = os.path.join(os.path.dirname(__file__), "display", "nemo_oled_service.py")
    if os.path.exists(local_display):
        sftp.put(local_display, "/opt/nemo/scripts/display/nemo_oled_service.py")
        print("✅ nemo_oled_service.py copiado a /opt/nemo.")

    local_telegram = os.path.join(os.path.dirname(__file__), "telegram", "nemo_telegram_bot.py")
    if os.path.exists(local_telegram):
        sftp.put(local_telegram, "/opt/nemo/scripts/telegram/nemo_telegram_bot.py")
        print("✅ nemo_telegram_bot.py copiado a /opt/nemo.")

    local_service = os.path.join(os.path.dirname(__file__), "..", "systemd", "nemo-display.service")
    if os.path.exists(local_service):
        sftp.put(local_service, "/tmp/nemo-display.service")
        print("✅ nemo-display.service subido.")

    sftp.close()
    ssh.close()

run_command("cp /tmp/nemo-display.service /etc/systemd/system/nemo-display.service && systemctl daemon-reload && systemctl enable nemo-display.service", "Habilitando servicio systemd...")

# 5. Comprobar I2C
run_command("i2cdetect -y 1", "Escaneando dispositivos I2C en el bus...")

print("\n🎉 ¡DESPLIEGUE COMPLETO Y SISTEMA PREPARADO!")
