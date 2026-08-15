# 🐶 Bloqueador_Publicidad_Nemo_Raspberry 🍓

| 🏗️ Perfil & Ubicación | 📈 Repositorio & Enlaces |
| :--- | :--- |
| ![Profesión](https://img.shields.io/badge/Profesi%C3%B3n-Arquitectos%20T%C3%A9cnicos-2e7d32?logo=micro%3Abit&logoColor=white&style=plastic) <br> ![Role](https://img.shields.io/badge/Role-BIM%20%26%20ConTech-007ACC?logo=bim360&style=plastic) <br> ![Location](https://img.shields.io/badge/Location-A%20Coru%C3%B1a%20%F0%9F%8C%8A-005B94?logo=lighthouse&logoColor=white&style=plastic) <br> ![Sector](https://img.shields.io/badge/Sector-ConTech%20%7C%20AECO-E65100?logo=construct3&style=plastic) <br> ![Maker](https://img.shields.io/badge/Maker-Software%20%2B%20Hardware-red?logo=makerbot&style=plastic) <br> ![Hardware](https://img.shields.io/badge/Hardware-Raspberry%20Pi%20Zero-C51A4A?logo=raspberrypi&logoColor=white&style=plastic) <br> ![OS](https://img.shields.io/badge/OS-Raspbian%20Bookworm%2032bit-A22846?logo=debian&logoColor=white&style=plastic) <br> ![Language](https://img.shields.io/badge/Language-Python%20%7C%20Bash-3776AB?logo=python&logoColor=white&style=plastic) | [![Versión](https://img.shields.io/badge/Version-v2.1.0-3b82f6?logo=github&style=plastic)](https://github.com/jmcaamanog/Bloqueador_Publicidad_Nemo_Raspberry/releases/latest) <br> [![Licencia](https://img.shields.io/badge/Licencia-MIT-8b5cf6.svg?style=plastic)](./LICENSE) <br> [![DNS](https://img.shields.io/badge/DNS-Pi--hole%20v6%20%2B%20Unbound-F60D1A?logo=pihole&logoColor=white&style=plastic)](https://pi-hole.net/) <br> [![VPN](https://img.shields.io/badge/VPN-Tailscale-24292E?logo=tailscale&logoColor=white&style=plastic)](https://tailscale.com/) <br> [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=plastic&logo=linkedin)](https://www.linkedin.com/in/jmcaamanog/) |

### Solución DNS privada, recursiva y sin publicidad optimizada para Raspberry Pi Zero 1.
*Arquitectura de defensa en red en 3 capas, combinando Pi-hole v6, resolver recursivo Unbound (raíz), 211 reglas Regex maestras contra publicidad nativa/clickbait, preservación de tarjeta SD con Log2Ram y suite física con Pantalla OLED 1.3", 2 Botones y LED direccionable RGB WS2812B.*

---

## ⚡ Enlaces y Accesos Rápidos

| 🌟 Recurso | 🚀 Acción / Enlace | 📝 Descripción |
| :--- | :--- | :--- |
| **Panel Web Pi-hole** | 👉 **[Abrir Dashboard](http://192.168.0.23/admin/)** | Acceso a la interfaz web oficial de Pi-hole v6. |
| **Esquema de Pines (Pinout)** | 🔌 **[Ver Guía de Conexionado](./hardware/PINOUT_ESQUEMA.md)** | Diagrama de cableado para OLED, 2 botones y WS2812B. |
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
> *   **Filtrado Estricto (+100.000 dominios):** Bloquea publicidad intrusiva, rastreadores, telemetría de Smart TVs, malware, phishing y estafas.
> *   **211 Reglas Regex para Publicidad Nativa:** Elimina widgets de Outbrain, Taboola, MediaGo, Google Syndication (DV360), SSPs y Popups sin saturar la RAM.
> *   **Log2Ram:** Elimina el 95% de escrituras continuas en la tarjeta microSD montando los registros en memoria RAM.

---

## 🌟 Características Principales

| Módulo | Icono | Funcionalidades Destacadas |
| :--- | :---: | :--- |
| **Pi-hole v6 Engine** | 🍓 | Servidor DNS local con motor FTL v6 nativo de alto rendimiento, bajo consumo de memoria y panel de control web moderno integrado. |
| **Unbound Resolver** | 🔒 | Servidor DNS recursivo local con soporte DNSSEC. Realiza consultas directas a los servidores raíz (`.root-servers.net`) para máxima privacidad. |
| **211 Reglas Regex** | 🎯 | Bloqueo por expresiones regulares de dominios ad-tech elusivos: Native Ads (Taboola, Outbrain, MGID), MediaGo, Google DV360, Popups y Push notifications. |
| **Listas Curadas** | 📋 | Integración equilibrada de **StevenBlack Hosts**, **Firebog Tick Lists** y feeds de alta reputación optimizados para 512MB de RAM. |
| **Log2Ram Protection** | 💾 | Redirección de logs del sistema (`/var/log`) a un disco virtual en memoria RAM, multiplicando la vida útil de la tarjeta microSD. |
| **Tailscale Mesh VPN** | 🌐 | Permite utilizar la Pi-hole como servidor DNS seguro desde cualquier parte del mundo en smartphones (Android / iOS) con datos móviles (4G / 5G). |
| **Pantalla OLED 1.3" & 2 Botones** | 🖥️ | Interfaz física con 4 vistas (Dashboard, Top Clientes, Gráficas, Info de Nemo) y control por pulsaciones (cambio de pantalla, sleep, bypass 5m y safe poweroff). |
| **LED RGB WS2812B (NeoPixel)** | 🌈 | Indicador luminoso multicolor de estados (Verde = Protegido, Naranja = Bypass, Azul = Petición DNS, Rojo = Alerta/Error). |
| **Bot de Alertas Telegram** | 🤖 | Notificaciones programadas con el resumen diario del estado de la red y alertas ante anomalías de tráfico en dispositivos IoT. |

---

## 🔌 Conexionado de Hardware (Pinout para Carcasa 3D)

```text
               Raspberry Pi Zero (GPIO)
               +-----------------------+
   3.3V (OLED) |  (1) (2)  | 5V Power (WS2812B 5V)
GPIO 2 (I2C SDA)|  (3) (4)  | 5V Power
GPIO 3 (I2C SCL)|  (5) (6)  | Ground (OLED GND)
       GPIO 4  |  (7) (8)  | GPIO 14 (TXD)
       Ground  |  (9) (10) | GPIO 15 (RXD)
GPIO 17 (BTN 1)| (11) (12) | GPIO 18 (WS2812B DIN - PWM)
GPIO 27 (BTN 2)| (13) (14) | Ground (BTN 2 GND)
       GPIO 22 | (15) (16) | GPIO 23
         3.3V  | (17) (18) | GPIO 24
GPIO 10 (MOSI) | (19) (20) | Ground (WS2812B GND)
               +-----------------------+
```

| Componente | Pin Físico RPi | Señal / GPIO | Pin en Componente | Función |
| :--- | :---: | :--- | :--- | :--- |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 1** | 3.3V DC Power | `VCC` | Alimentación pantalla OLED |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 6** | Ground (GND) | `GND` | Masa pantalla OLED |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 3** | GPIO 2 (SDA) | `SDA` | Datos I2C |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 5** | GPIO 3 (SCL) | `SCL` | Reloj I2C |
| **🔘 Botón 1 (Navegación)** | **Pin 11** | GPIO 17 (Pull-Up) | Terminal A | Terminal B a **Pin 9 (GND)** |
| **🔴 Botón 2 (Bypass/Power)** | **Pin 13** | GPIO 27 (Pull-Up) | Terminal A | Terminal B a **Pin 14 (GND)** |
| **🌈 LED WS2812B (5V)** | **Pin 2 o 4** | 5V DC Power | `5V` / `VCC` | Alimentación 5V Neopixel |
| **🌈 LED WS2812B (GND)** | **Pin 20** | Ground (GND) | `GND` | Masa Neopixel |
| **🌈 LED WS2812B (DIN)** | **Pin 12** | GPIO 18 (PWM/DMA) | `DIN` / `Data In` | Señal de control de color |

---

## 📱 Protección Fuera de Casa con Tailscale VPN (4G / 5G)

Tailscale te permite navegar en tu móvil fuera de casa utilizando tu Raspberry Pi Zero como servidor DNS seguro, bloqueando anuncios en redes móviles 4G/5G y Wi-Fi públicas.

1. **Instala la app Tailscale en tu móvil** (Android / iOS) e inicia sesión con tu cuenta.
2. **Vincula la Raspberry Pi Zero**:
   * Ejecuta en la Pi: `sudo tailscale up` y abre el enlace de autenticación generado para vincularla a tu misma cuenta.
3. **Configura el DNS en el Panel de Tailscale ([login.tailscale.com/admin/dns](https://login.tailscale.com/admin/dns))**:
   * En la sección **Nameservers**, pulsa **Add nameserver** ➔ **Custom**.
   * Escribe la **IP de Tailscale de tu Raspberry Pi Zero** (empieza por `100.x.y.z`).
   * Activa el interruptor **Override local DNS** (MagicDNS).
4. **¡Listo!** Enciende la VPN en la app de Tailscale de tu móvil y disfrutarás de bloqueo total de anuncios en cualquier parte del mundo.

---

## 📁 Estructura del Repositorio

```text
Bloqueador_Publicidad_Nemo_Raspberry/
├── config/                               # Plantillas de configuración del sistema
│   ├── unbound.conf                      # Configuración de Unbound para Pi-hole (puerto 5335)
│   └── pihole.toml.example               # Configuración de referencia para Pi-hole v6
├── doc_info/                             # Documentación técnica y reglas de bloqueo
│   ├── pihole_ads_clickbait_native_2026.conf  # Las 211 reglas Regex organizadas por categorías
│   ├── pihole_ads_clickbait_native_2026.md    # Manual técnico de las reglas Regex
│   └── pihole_arquitectura_bloqueo_V2_2026.md # Guía de Arquitectura de Defensa en 3 Capas
├── hardware/                             # Esquemas de conexionado físico y pinout
│   └── PINOUT_ESQUEMA.md                 # Guía de pines para OLED 1.3", 2 Botones y LED RGB WS2812B
├── scripts/                              # Scripts de utilidad, visualización y mantenimiento
│   ├── deploy_to_pi.py                   # Script de despliegue y actualización en 1 clic
│   ├── check_system_status.py            # Diagnóstico rápido de servicios y resolución DNS
│   ├── inject_gravity_rules.py           # Inyección directa de listas y reglas en gravity.db
│   ├── format_sd_card.bat                # Utilidad para formatear tarjetas microSD a FAT32
│   ├── display/                          # Driver de pantalla OLED y gestión de gestos GPIO
│   │   └── nemo_oled_service.py          # Servicio de pantalla OLED 1.3" + Botones + WS2812B
│   └── telegram/                         # Bot de alertas e informes diarios
│       └── nemo_telegram_bot.py          # Notificador automático a Telegram
├── systemd/                              # Servicios systemd para inicio automático
│   └── nemo-display.service              # Servicio de arranque para pantalla OLED y GPIO
├── CHANGELOG.md                          # Historial de versiones y cambios del proyecto
├── LICENSE                               # Licencia de código abierto MIT
└── README.md                             # Documentación principal del repositorio
```

---

## 👨‍💻 Autor

**Jose Manuel Caamaño González** | Arquitecto Técnico & BIM Manager  
Digital Product Lead | ConTech & Digital Twin SaaS | Data Analytics (SQL, Power BI)

Hecho con código y café desde A Coruña. ☕  
[LinkedIn](https://www.linkedin.com/in/jmcaamanog/) · [Web](https://jmcaamanog.pages.dev)
