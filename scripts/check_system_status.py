import paramiko
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

PI_IP = os.getenv("PI_IP", "192.168.0.23")
PI_USER = os.getenv("PI_USER", "jose")
PI_PASS = os.getenv("PI_PASS", "josejosejose1")

print(f"Comprobando estado de la Pi Zero ({PI_IP})...")

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    ssh.connect(PI_IP, username=PI_USER, password=PI_PASS, timeout=8)
    
    commands = [
        ("Estado de Pi-hole", "pihole status"),
        ("Servicios Activos", "systemctl is-active pihole-FTL unbound log2ram tailscaled"),
        ("Estadísticas de Gravedad", "sqlite3 /etc/pihole/gravity.db 'SELECT count(*) FROM gravity; SELECT count(*) FROM domainlist WHERE type=2; SELECT count(*) FROM adlist;'"),
        ("Prueba DNS Google", "dig @127.0.0.1 google.com +short"),
        ("Prueba Bloqueo Publicidad", "dig @127.0.0.1 tpc.googlesyndication.com +short")
    ]
    
    for title, cmd in commands:
        print(f"\n=== {title} ===")
        stdin, stdout, stderr = ssh.exec_command(f"echo {PI_PASS} | sudo -S {cmd}")
        print(stdout.read().decode('utf-8', errors='ignore').strip())
        
    ssh.close()
    print("\n✅ Diagnóstico completado.")
except Exception as e:
    print(f"Error conectando a la Pi Zero: {e}")
