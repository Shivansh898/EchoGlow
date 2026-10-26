# Ultrasonic Distance Warning System

## Overview

This project uses an ultrasonic sensor to measure the distance of nearby objects and provides visual and audible feedback using three LEDs and a buzzer. As an object gets closer to the sensor, the warning level increases, making it useful as a simple proximity alert system.

## Why I Made This Project

I wanted to learn how to use an ultrasonic sensor with a Raspberry Pi and create a practical system that reacts to distance measurements. The project combines sensors, LEDs, and a buzzer to demonstrate how real-world warning systems work.

## Features

- Measures distance using an HC-SR04 ultrasonic sensor
- Green LED indicates a safe distance
- Yellow LED indicates a moderate distance
- Red LED indicates a very close object
- Buzzer sounds faster as objects get closer
- Continuous real-time monitoring

## How It Works

The ultrasonic sensor constantly measures the distance to objects in front of it.

### Distance Zones

| Distance | Output |
|-----------|---------|
| 0-6 cm | Red LED flashes and buzzer sounds rapidly |
| 7-30 cm | Yellow LED flashes and buzzer sounds |
| 31-50 cm | Green LED turns on |
| Over 50 cm | No warning |

## Wiring

### LEDs

- Red LED connected to GPIO 25 through a resistor
- Yellow LED connected to GPIO 16 through a resistor
- Green LED connected to GPIO 20 through a resistor
- All LED cathodes connected to GND

### Buzzer

- Positive terminal connected to GPIO 5
- Negative terminal connected to GND

### Ultrasonic Sensor

| HC-SR04 Pin | Raspberry Pi Pin |
|------------|------------------|
| VCC | 5V |
| GND | GND |
| TRIG | GPIO 18 |
| ECHO | GPIO 23 |

## Pictures

### Completed Circuit

<img width="4032" height="3024" alt="IMG_5079" src="https://github.com/user-attachments/assets/e2f7f12f-eaa8-4188-926a-ce58ae961bcb" />
<img width="5712" height="4284" alt="IMG_5078" src="https://github.com/user-attachments/assets/ad9bc502-a714-4908-995a-f5e9530ffcd9" />
<img width="4032" height="3024" alt="IMG_5077 (1)" src="https://github.com/user-attachments/assets/8931ffec-3154-402c-8456-a778c0fa38a0" />

### Code Running

<img width="4284" height="5712" alt="IMG_5081 (2)" src="https://github.com/user-attachments/assets/d2404725-19d5-4194-8437-c25a828bdd2f" />


## Installation

### Install GPIO Zero

sudo apt update
sudo apt install python3-gpiozero

Part,Quantity,Link
Raspberry Pi 4 Model B,1,https://www.raspberrypi.com/products/raspberry-pi-4-model-b/
HC-SR04 Ultrasonic Sensor,1,https://components101.com/sensors/ultrasonic-sensor-working-pinout-datasheet
Red LED (5mm),1,https://thepihut.com/products/5mm-red-led-pack-of-10
Yellow LED (5mm),1,https://thepihut.com/products/5mm-yellow-led-pack-of-10
Green LED (5mm),1,https://thepihut.com/products/5mm-green-led-pack-of-10
220 Ohm Resistor,3,https://thepihut.com/products/resistor-pack-220-ohm
Active Buzzer,1,https://thepihut.com/products/active-buzzer-module
Solderless Breadboard,1,https://thepihut.com/products/full-size-breadboard
Male-to-Male Jumper Wires,10,https://thepihut.com/products/male-to-male-jumper-wires-40-pack
USB-C Power Supply,1,https://www.raspberrypi.com/products/type-c-power-supply/
