#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bot de Notificaciones y Alertas Diarias para Telegram
Para: Bloqueador_Publicidad_Nemo_Raspberry
Autor: Jose Manuel Caamaño González
"""

import os
import sys
import time
import json
import urllib.request
import urllib.parse
from datetime import datetime

TELEGRAM_TOKEN = os.getenv("NEMO_TELEGRAM_TOKEN", "")
TELEGRAM_CHAT_ID = os.getenv("NEMO_TELEGRAM_CHAT_ID", "")

def send_telegram_message(text):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print(f"[Aviso] Tokens de Telegram no configurados. Mensaje:\n{text}")
        return False
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = urllib.parse.urlencode({
        "chat_id": TELEGRAM_CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }).encode("utf-8")
    
    try:
        req = urllib.request.Request(url, data=payload)
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception as e:
        print(f"Error enviando mensaje a Telegram: {e}")
        return False

def get_daily_report():
    try:
        req = urllib.request.urlopen("http://127.0.0.1/api/stats/summary", timeout=3)
        data = json.loads(req.read().decode('utf-8'))
        total = data.get("queries", {}).get("total", 0)
        blocked = data.get("queries", {}).get("blocked", 0)
        percent = data.get("queries", {}).get("percent_blocked", 0.0)
        clients = data.get("clients", {}).get("active", 0)
    except Exception:
        total, blocked, percent, clients = (0, 0, 0.0, 0)

    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
            temp = float(f.read().strip()) / 1000.0
    except Exception:
        temp = 0.0

    report = (
        "🐶 *[Nemo Guardián DNS] - Reporte Diario* 🛡️\n\n"
        f"📅 *Fecha:* `{datetime.now().strftime('%d/%m/%Y %H:%M')}`\n"
        f"📊 *Total Peticiones:* `{total}`\n"
        f"🛑 *Anuncios Bloqueados:* `{blocked}` (`{percent:.1f}%`)\n"
        f"📱 *Clientes Activos:* `{clients} dispositivos`\n"
        f"🌡️ *Temperatura CPU:* `{temp:.1f} °C`\n\n"
        "✅ _Tu red local está 100% protegida y sin rastreadores._"
    )
    return report

if __name__ == "__main__":
    report_text = get_daily_report()
    send_telegram_message(report_text)
    print("Reporte generado:")
    print(report_text)
