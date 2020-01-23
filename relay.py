#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Beispiel Seite 81
# Relais schalten
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
relay = 14
gpio.setup(relay, gpio.OUT)
gpio.output(relay, gpio.HIGH) # relay geschaltet
time.sleep(4)
gpio.output(relay, gpio.LOW)  # relay geschaltet

#while True: # Diese Schleife läuft für immer
#        gpio.output(relay, gpio.HIGH) # relay geschaltet
#        time.sleep(2)
#        gpio.output(relay, gpio.LOW)  # relay geschaltet
#        time.sleep(1)