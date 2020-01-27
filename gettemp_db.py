#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Beispiel Seite 81
# Voraussetzungen:
# Fügen Sie in die Datei /boot/config.txt
# diese Zeile ein:
#
# dtoverlay=w1-gpio
#
# Speichern Sie die Datei und starten Sie das System neu.
# Führen Sie dann in einem Terminal
#
# cd /sys/bus/w1/devices/
# ls
# aus. Die Ausgabe enthält einen eindeutige Geräte-ID für den DS18B20-Sensor. 
# Tragen Sie den Pfad in diesem Script hinter "pathes=" ein.
#
# Für die Datenbank installieren Sie diese Pakete
#
# sudo apt-get install rrdtool python-rrdtool
#
# Um aus den Einträgen in der Datenbank einen Grafik mit dem Verlauf zu erzeugen,
# verwenden Sie das Bash-Script create_rrd_graph.sh
#
import re, os, time
import rrdtool

# function: Sensor-Daten-Datei lesen und auswerten
def read_sensor(path):
    value = "U"
    try:
        f = open(path, "r")
        line = f.readline()
        if re.match(r"([0-9a-f]{2} ){9}: crc=[0-9a-f]{2} YES", line):
            line = f.readline()
            m = re.match(r"([0-9a-f]{2} ){9}t=([+-]?[0-9]+)", line)
            if m:
                value = str(float(m.group(2)) / 1000.0)
        f.close()
    except IOError as err:
        # print time.strftime("%x %X"), "Fehler beim Lesen", path, ": ", format(err)
        print('I/O error: {0}'.format(err))
    return value

# Pfad oder Pfade zum Sensor angeben
# Sensor-Pfad
pathes = (
'/sys/bus/w1/devices/28-031797798836/w1_slave',
)

# Sensordaten lesen
data = 'N'
for path in pathes:
  data += ':'
  data += read_sensor(path)
  time.sleep(1)

# Daten in der Round-Robin-Datenbank speichern
rrdtool.update(
  "%s/temperature.rrd" % (os.path.dirname(os.path.abspath(__file__))),
  data)