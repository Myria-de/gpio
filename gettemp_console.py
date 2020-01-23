#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Beispiel Seite 80/81
# Temperatur messen mit DS18S20
import time
# den Pfad bitte anpassen
sensor = '/sys/bus/w1/devices/28-031797798836/w1_slave'
def readTempSensor(sensorName) :
    f = open(sensorName, 'r')
    lines = f.readlines()
    f.close()
    return lines
while True :
    print(time.strftime('%H:%M:%S') +" - " + str(readTempSensor(sensor)))
    time.sleep(10)