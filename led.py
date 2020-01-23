#!/usr/bin/python3
# Beispiel Seite 79
# LED mit Taster an/ausschalten
# LED an GPIO-Port 18 
# Taster an GPIO-Port 24
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(24, gpio.IN)
gpio.setup(18, gpio.OUT)
while True:
    if gpio.input(24) == 0:
        gpio.output(18, gpio.LOW)
    else:
        gpio.output(18, gpio.HIGH)