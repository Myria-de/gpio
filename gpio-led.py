#!/usr/bin/python3
# Beispiel Seite 78
# LED an GPIO 18 ein- und ausschalten
import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
# Bei Bedarf: Warnmeldung wegen des
# bereits geoeffneten Kanals unterdruecken
# gpio.setwarnings(False)
gpio.setup(18, gpio.OUT)
gpio.output(18, gpio.HIGH)
time.sleep(4)
gpio.output(18, gpio.LOW)