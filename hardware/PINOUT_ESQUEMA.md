# 🔌 Esquema de Conexionado de Hardware (Pinout)

Guía de cableado para la **Pantalla OLED 1.3" I2C**, **2 Botones de Control** y **LED Direccionable RGB WS2812B (NeoPixel)** en la **Raspberry Pi Zero**.

---

## 📐 Diagrama de Pines del Header de 40 Pines

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

---

## 📋 Lista de Conexiones por Componente

| Componente | Pin Físico RPi | Señal / GPIO | Pin en Componente | Notas |
| :--- | :---: | :--- | :--- | :--- |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 1** | 3.3V DC Power | `VCC` | Consumo <15mA |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 6** | Ground (GND) | `GND` | Línea de masa |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 3** | GPIO 2 (SDA) | `SDA` | Bus I2C Datos |
| **🖥️ OLED 1.3" (SH1106)** | **Pin 5** | GPIO 3 (SCL) | `SCL` | Bus I2C Reloj |
| **🔘 Botón 1 (Navegación)** | **Pin 11** | GPIO 17 (Pull-Up) | Terminal A | Terminal B a **Pin 9 (GND)** |
| **🔴 Botón 2 (Bypass/Power)** | **Pin 13** | GPIO 27 (Pull-Up) | Terminal A | Terminal B a **Pin 14 (GND)** |
| **🌈 LED WS2812B (5V)** | **Pin 2 o 4** | 5V DC Power | `5V` / `VCC` | Alimentación de 5V |
| **🌈 LED WS2812B (GND)** | **Pin 20** | Ground (GND) | `GND` | Línea de masa |
| **🌈 LED WS2812B (DIN)** | **Pin 12** | GPIO 18 (PWM/DMA) | `DIN` / `Data In` | Control por Hardware PWM |

---

## 🎨 Código de Colores y Efectos del LED WS2812B

* 🟢 **Verde (Respiración suave):** Escudo Activo / Todo el tráfico filtrado y seguro.
* 🟠 **Naranja / Ámbar:** Modo Bypass 5 minutos activado (cuenta atrás en OLED).
* 🔵 **Azul Cian (Destello):** Petición DNS procesada en tiempo real.
* 🔴 **Rojo Fijo / Flash:** Alerta crítica (sin conexión a internet o Temp CPU > 65°C).
* 🟣 **Morado:** Reinicio de DNS o actualización de gravedad en curso.

---

## 🛠️ Instalación de Librerías en la Raspberry Pi
```bash
sudo apt-get update
sudo apt-get install -y i2c-tools python3-pil python3-rpi.gpio python3-pip
sudo pip3 install rpi_ws281x --break-system-packages
```
