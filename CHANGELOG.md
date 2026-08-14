# 📜 Historial de Cambios (CHANGELOG)

Todas las novedades y modificaciones notables de este proyecto se documentan en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/es-ES/1.0.0/), y este proyecto se adhiere a [Semantic Versioning](https://semver.org/lang/es/).

---

## [2.0.0] - 2026-08-14
### ✨ Añadido
* **Despliegue Maestro Automatizado V2**: Instalación desatendida de **Pi-hole v6.7** sobre **Raspbian Bookworm (32-bit Lite)** en Raspberry Pi Zero 1.
* **Resolver Recursivo Local Unbound**: Integración de Unbound en `127.0.0.1#5335` con validación DNSSEC y consultas directas a los servidores raíz (Root Hints).
* **211 Reglas Regex Maestras**: Inyección de patrones avanzados para bloqueo de Native Ads, Clickbait, SSP/DSP, Taboola, Outbrain, MediaGo, Criteo, Teads, MGID y Popups.
* **26 Listas de Bloqueo de Alto Rendimiento**: Pack curado con listas de Firebog (Adguard, Admiral, Easylist, Prigent), HaGeZi (Multi Normal, Pop-Up Ads, TIF) y BlocklistProject (Malware, Phishing, Scam, Redirect).
* **Protección de Tarjeta SD con Log2Ram**: Montaje de `/var/log` en memoria RAM para evitar el desgaste de escrituras flash en microSD.
* **Acceso Remoto Seguro con Tailscale**: Integración de VPN WireGuard basada en malla para administración y resolución fuera de casa.
* **Mantenimiento Semanal Automatizado**: Cron semanal para actualización silenciosa de la base de datos de gravedad.

### 🛡️ Seguridad y Optimización
* Configuración de listeningMode `ALL` en `pihole.toml` para resolución en subredes locales y clientes Wi-Fi.
* Protección contra falsos positivos y limpieza de entradas whitelist heredadas.

---

## [1.0.0] - 2026-08-10
### ✨ Inicial
* Configuración básica de Pi-hole en Raspberry Pi Zero 1 (W).
* Scripts de formateo y preparación de tarjeta microSD FAT32.
