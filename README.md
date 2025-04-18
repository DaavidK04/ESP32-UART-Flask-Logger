# ESP32 UART Flask Logger

Dieses Projekt zeigt, wie ein ESP32 Daten über UART an einen Raspberry Pi sendet, wo die Daten von einem Python-Script empfangen und über einen Flask-Webserver visualisiert werden.

## Ziel

Ziel ist es, Logdaten (z. B. aktuelle Tasteninputs, Motordaten oder Statusinformationen) in Echtzeit vom ESP32 an einen Raspberry Pi zu senden und über eine Weboberfläche zugänglich zu machen.

---

## Komponenten

### Mikrocontroller
- **ESP32 Dev Board**
  - UART-fähig
  - Bluetooth-fähig (z. B. Verbindung mit PS5-Controller)

### Empfänger
- **Raspberry Pi**
  - z. B. Raspberry Pi 4 oder 3B+
  - Raspbian OS mit Desktop oder Lite
  - UART-fähige GPIO-Pins

### Verbindung
- UART (TX vom ESP32 an RX vom Pi und GND zu GND)
- Optional: USB zu UART Adapter, falls kein GPIO verwendet wird

---

## Schaltplan

| ESP32 Pin | Funktion        | Raspberry Pi Pin |
|-----------|------------------|------------------|
| TX (z. B. GPIO1) | UART TX       | GPIO15 (RXD0, Pin 10) |
| GND       | Masse           | GND (z. B. Pin 6) |

> **Hinweis**: ESP32 TX darf *nicht direkt* mit 3.3V RX vom Pi verbunden werden, wenn Pegelwandler benötigt wird (je nach Modell). In der Praxis funktioniert es oft trotzdem direkt.

---

## UART Konfiguration auf dem Pi

Bearbeite `/boot/config.txt`:

```bash
enable_uart=1
