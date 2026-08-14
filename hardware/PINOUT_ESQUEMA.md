# 🔌 Esquema de Conexionado de Hardware (Pinout)

Guía de cableado para la **Pantalla OLED 1.3" I2C**, **2 Botones de Control** y **2 LEDs de Estado** en la **Raspberry Pi Zero**.

---

## 📐 Diagrama de Pines del Header de 40 Pines

```text
               Raspberry Pi Zero (GPIO)
               +-----------------------+
   3.3V (OLED) |  (1) (2)  | 5V Power
GPIO 2 (I2C SDA)|  (3) (4)  | 5V Power
GPIO 3 (I2C SCL)|  (5) (6)  | Ground (OLED GND)
       GPIO 4  |  (7) (8)  | GPIO 14 (TXD)
       Ground  |  (9) (10) | GPIO 15 (RXD)
GPIO 17 (BTN 1)| (11) (12) | GPIO 18 (PCM_CLK)
GPIO 27 (BTN 2)| (13) (14) | Ground (BTN 2 GND)
GPIO 22 (LED G)| (15) (16) | GPIO 23 (LED R)
         3.3V  | (17) (18) | GPIO 24
GPIO 10 (MOSI) | (19) (20) | Ground (LEDs GND)
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
| **🟢 LED Verde (Escudo)** | **Pin 15** | GPIO 22 (Ánodo +) | Ánodo (+) | Intercalar resistencia 220Ω-330Ω hacia **Pin 20 (GND)** |
| **🟠 LED Rojo (Alerta)** | **Pin 16** | GPIO 23 (Ánodo +) | Ánodo (+) | Intercalar resistencia 220Ω-330Ω hacia **Pin 20 (GND)** |

---

## 🛠️ Comandos de Activación de I2C en la Raspberry Pi
Para habilitar el bus I2C en Raspbian Lite:
```bash
sudo raspi-config nonint do_i2c 0
sudo apt-get install -y i2c-tools python3-pil python3-rpi.gpio
i2cdetect -y 1
```
*(Deberá responder el dispositivo en la dirección `0x3C`).*
