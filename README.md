# 🍓 Pi-hole v6 + Unbound Master DNS (Raspberry Pi Zero)

| 🏗️ Perfil & Ubicación | 📈 Repositorio & Enlaces |
| :--- | :--- |
| ![Profesión](https://img.shields.io/badge/Profesi%C3%B3n-Arquitectos%20T%C3%A9cnicos-2e7d32?logo=micro%3Abit&logoColor=white&style=plastic) <br> ![Role](https://img.shields.io/badge/Role-BIM%20%26%20ConTech-007ACC?logo=bim360&style=plastic) <br> ![Location](https://img.shields.io/badge/Location-A%20Coru%C3%B1a%20%F0%9F%8C%8A-005B94?logo=lighthouse&logoColor=white&style=plastic) <br> ![Sector](https://img.shields.io/badge/Sector-ConTech%20%7C%20AECO-E65100?logo=construct3&style=plastic) <br> ![Maker](https://img.shields.io/badge/Maker-Software%20%2B%20Hardware-red?logo=makerbot&style=plastic) <br> ![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Zero-C51A4A?logo=raspberrypi&logoColor=white&style=plastic) <br> ![OS](https://img.shields.io/badge/OS-Raspbian%20Bookworm%2032bit-A22846?logo=debian&logoColor=white&style=plastic) <br> ![Language](https://img.shields.io/badge/Language-Python%20%7C%20Bash-3776AB?logo=python&logoColor=white&style=plastic) | [![Versión](https://img.shields.io/badge/Version-v2.0.0-3b82f6?logo=github&style=plastic)](https://github.com/jmcaamanog/raspberry_pi_zero_pihole/releases/latest) <br> [![Licencia](https://img.shields.io/badge/Licencia-MIT-8b5cf6.svg?style=plastic)](./LICENSE) <br> [![DNS](https://img.shields.io/badge/DNS-Pi--hole%20v6%20%2B%20Unbound-F60D1A?logo=pihole&logoColor=white&style=plastic)](https://pi-hole.net/) <br> [![VPN](https://img.shields.io/badge/VPN-Tailscale-24292E?logo=tailscale&logoColor=white&style=plastic)](https://tailscale.com/) <br> [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin)](https://www.linkedin.com/in/jmcaamanog/) |

### Solución DNS privada, recursiva y sin publicidad optimizada para Raspberry Pi Zero 1.
*Arquitectura de defensa en red en 3 capas, combinando Pi-hole v6, resolver recursivo Unbound (raíz), 211 reglas Regex maestras contra publicidad nativa/clickbait y preservación de tarjeta SD con Log2Ram.*

---

## ⚡ Enlaces y Accesos Rápidos

| 🌟 Recurso | 🚀 Acción / Enlace | 📝 Descripción |
| :--- | :--- | :--- |
| **Panel Web Pi-hole** | 👉 **[Abrir Dashboard](http://192.168.0.23/admin/)** | Acceso a la interfaz web oficial de Pi-hole v6. |
| **Arquitectura de Bloqueo** | 🛡️ **[Ver Guía Arquitectura V2](./doc_info/pihole_arquitectura_bloqueo_V2_2026.md)** | Documento técnico detallado sobre la defensa en 3 capas. |
| **Reglas Regex Maestras** | 📝 **[Ver 211 Reglas (.conf)](./doc_info/pihole_ads_clickbait_native_2026.conf)** | Configuración de patrones Regex anti Native Ads y DSP. |
| **Historial de Versiones** | 📜 **[Ver CHANGELOG.md](./CHANGELOG.md)** | Registro detallado de versiones y mejoras. |
| **Cómo Contribuir** | 🛠️ **[Ver CONTRIBUTING.md](./CONTRIBUTING.md)** | Guía de colaboración, nuevas ideas y Pull Requests. |
| **Código de Conducta** | 🤝 **[Ver CODE_OF_CONDUCT.md](./CODE_OF_CONDUCT.md)** | El manual del buen rollo y convivencia comunitaria. |
| **Seguridad y Reportes** | 🛡️ **[Ver SECURITY.md](./SECURITY.md)** | Política de reporte responsable de vulnerabilidades. |

---

> [!IMPORTANT]
> ### 🛡️ Arquitectura de Protección de Alto Rendimiento
> Este despliegue convierte una modesta **Raspberry Pi Zero 1 (Single-Core 1GHz ARMv6 con 512MB RAM)** en un escudo de red corporativo:
> *   **DNS 100% Autónomo (Unbound):** Resuelve directamente en los servidores raíz DNS en `127.0.0.1#5335` con validación criptográfica DNSSEC, sin ceder telemetría a intermediarios (Google/Cloudflare).
> *   **Filtrado Estricto (+250.000 dominios):** Bloquea publicidad intrusiva, rastreadores, telemetría de Smart TVs, malware, phishing y estafas.
> *   **211 Reglas Regex para Publicidad Nativa:** Elimina widgets de Outbrain, Taboola, MediaGo, Google Syndication (DV360), SSPs y Popups.
> *   **Log2Ram:** Elimina el 95% de escrituras continuas en la tarjeta microSD montando los registros en memoria RAM.

---

## 🌟 Características Principales

| Módulo | Icono | Funcionalidades Destacadas |
| :--- | :---: | :--- |
| **Pi-hole v6 Engine** | 🍓 | Servidor DNS local con motor FTL v6 nativo de alto rendimiento, bajo consumo de memoria y panel de control web moderno integrado. |
| **Unbound Resolver** | 🔒 | Servidor DNS recursivo local con soporte DNSSEC. Realiza consultas directas a los servidores raíz (`.root-servers.net`) para máxima privacidad. |
| **211 Reglas Regex** | 🎯 | Bloqueo por expresiones regulares de dominios ad-tech elusivos: Native Ads (Taboola, Outbrain, MGID), MediaGo, Google DV360, Popups y Push notifications. |
| **Listas Curadas (26 Feeds)** | 📋 | Integración sin falsos positivos de **Firebog Tick Lists**, **HaGeZi (Multi, Popups, TIF)** y **BlocklistProject (Malware, Scam, Phishing)**. |
| **Log2Ram Protection** | 💾 | Redirección de logs del sistema (`/var/log`) a un disco virtual en memoria RAM, multiplicando la vida útil de la tarjeta microSD. |
| **Tailscale Mesh VPN** | 🌐 | Permite utilizar la Pi-hole como servidor DNS seguro desde cualquier parte del mundo en smartphones y portátiles conectados a la red Tailscale. |
| **Mantenimiento Autónomo** | ⚙️ | Tarea programada semanal (`cron.weekly`) para actualización y saneamiento desatendido de la gravedad de dominios. |

---

## 📁 Estructura del Repositorio

```text
raspberry_pi_zero_pihole/
├── config/                               # Plantillas de configuración del sistema
│   ├── unbound.conf                      # Configuración de Unbound para Pi-hole (puerto 5335)
│   └── pihole.toml.example               # Configuración de referencia para Pi-hole v6
├── doc_info/                             # Documentación técnica y reglas de bloqueo
│   ├── pihole_ads_clickbait_native_2026.conf  # Las 211 reglas Regex organizadas por categorías
│   ├── pihole_ads_clickbait_native_2026.md    # Manual técnico de las reglas Regex
│   └── pihole_arquitectura_bloqueo_V2_2026.md # Guía de Arquitectura de Defensa en 3 Capas
├── scripts/                              # Scripts de utilidad y mantenimiento
│   ├── check_system_status.py            # Diagnóstico rápido de servicios y resolución DNS
│   ├── inject_gravity_rules.py           # Inyección directa de listas y reglas en gravity.db
│   └── format_sd_card.bat                # Utilidad para formatear tarjetas microSD a FAT32
├── CHANGELOG.md                          # Historial de versiones y cambios del proyecto
├── LICENSE                               # Licencia de código abierto MIT
└── README.md                             # Documentación principal del repositorio
```

---

## 🚀 Guía de Instalación y Despliegue

### 1. Preparación de la Tarjeta microSD
1. Graba **Raspberry Pi OS Lite (32-bit)** utilizando *Raspberry Pi Imager*.
2. En las opciones de configuración (icono ⚙️):
   * Habilita **SSH** con autenticación por contraseña.
   * Configura tu usuario y contraseña.
   * Configura tu red **Wi-Fi** y país de red (`ES`).

### 2. Despliegue Automatizado
Para desplegar la pila completa en la Raspberry Pi Zero, ejecuta el script de inyección:
```bash
python scripts/inject_gravity_rules.py
```

### 3. Configuración de Clientes / Router
* **En el Router (Toda la casa):** Configura en la sección **LAN / DHCP** la IP de la Pi Zero (`192.168.0.23`) como **DNS Primario**.
* **En un PC individual (Windows):**
  ```cmd
  netsh interface ip set dns name="Wi-Fi" static 192.168.0.23
  ipconfig /flushdns
  ```

---

## 👨‍💻 Autor

**Jose Manuel Caamaño González** | Arquitecto Técnico & BIM Manager  
Digital Product Lead | ConTech & Digital Twin SaaS | Data Analytics (SQL, Power BI)

Hecho con código y café desde A Coruña. ☕  
[LinkedIn](https://www.linkedin.com/in/jmcaamanog/) · [Web](https://jmcaamanog.pages.dev)
