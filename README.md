# Raspberry GPIO: Schalten und messen
Hier finden Sie alle Programmierbeispiele, Befehlszeilen und Schaltpläne zum Artikel aus der LinuxWelt 02/2020, Seite 76 bis 81.

Auf dem Raspberry Pi sind mehrere Schnittstellen untergebracht, die eine Kommunikation mit der Außenwelt ermöglichen. Eine der wichtigsten davon ist die frei programmierbare GPIO (General Purpose Input/Output). Darüber lassen sich LEDs oder Relais steuern sowie Messwerte von Sensoren abfragen. Mit ein paar zusätzlichen Bauteilen wird aus dem Raspberry Pi ein Lehr- und Lerncomputer, der in die Welt der Elektronik und zugleich in die Programmierung einführt. Das eignet sich auch für Kinder und Jugendliche ab etwa 12 Jahren (mit Begleitung durch Erwachsene).

## Bestückung und Schaltpläne

Sie finden die Dateiem im Ordner "Fritzing".

Die fzz-Dateien lassen sich mit dem Tool Fritzing öffnen und bearbeiten. Sie Software ist Open-Source, der Quellcode ist unter https://github.com/fritzing/fritzing-app verfügbar. Das kompilierte Programm gibt es bei https://fritzing.org/download/. Die Entwickler verlangen vor dem Download 8 oder 25 Euro als Spende.

## Code-Beispiele

**gpio-led.py** Seite 78: LED ein/ausschalten

**led.py** Seite 79: LED mit Taster ein/ausschalten

**gettemp_console.py** Seite 81: Temperatur messen (DS18B20)

**gettemp_db.py** Seite 81: Temperatur messen (DS18B20) und Werte in Datenbank speichern (siehe Anleitung in der py-Datei)

**relay.py** Seite 81: Relais schalten

**LED-GUI.py** Seite 81 (Kasten): LED über grafische Oberfläche steuern

## Zusätzliches Beispiel: DHT11

**dht11.py** Seite 81: Temperatur und Feuchtigkeit messen

DHT11 ist eine Sensor für Luftfeuchtigkeit und Temperatur. Das Bauteil alleine kostet etwa 2 Euro, Module gibt es teilweise zum gleichen Preis. Das Modul hat den Vorteil, das hier in der Regel bereits ein Widerstand mit 4,7kΩ aufgelötet ist, den Sie ansonsten auf dem Steckbrett zwischen der Spannungsversorgung mit 3,3 Volt und der Datenleitung einbauen müssen. Der Widerstand dient neben der Stromversorgung auch zur Verbesserung der Messergebnisse.

Ein DHT11-Modul besitzt drei Pins von denen einer mit „S“ beschriftet ist. Diesen verbinden Sie mit GPIO 4, der mittlere („+“) wird mit dem 3,3-Volt-Pin verbunden und der auf der rechten Seite („-“) mit GND.

Für den Sensor benötigen Sie eine zusätzliche Programmbibliothek. Den Quellcode laden Sie mit 
```
git clone https://github.com/Myria-de/Python_DHT.git
```
herunter, für die Installation verwenden Sie 
```
sudo python3 setup.py install
```

## Python: Ein erster Eindruck

**Seite 78**

```
print('Hello World')
```

```
MeinName = 'Sepp'
print('Mein Name ist: ' + MeinName)
```

```
zahl1 = 2
zahl2 = 4
ergebnis = zahl1 + zahl2
print(str(ergebnis))
```
**Seite 79**
```
MeineListe = [2, 7, 8, 'red', 'blue']
print(MeineListe)
print(MeineListe[2])
```

```
MeineListe = []
MeineListe.append('red')
print(MeineListe)
```

```
MeinString = "Hello World"
print(MeinString[0])
print(MeinString[6:11])
```

```
print(MeinString[6:])
```

```
MeinString = "Hello World"
print(MeinString.replace('World','Universe'))
```

```
zahl = 11
if(zahl > 10):
    print('Wert ist größer 10')
    print('Das ist viel')
else:
    print('Wert ist kleiner oder gleich 10')
```

**Seite 80**
```
def add(a,b):
    print ('Addiere: ' + str(a) +' und ' + str(b))
    return a + b
print ('Ergebnis: ' + str(add(2,3)))
```

```
x=1
while x < 6:
    print(x)
    x += 1
```
**Seite 81**
```
colors = ['red', 'blue', 'green']
for x in colors:
    print(x)
```
```
import os
home=os.path.expanduser('~')
os.chdir(home)
files=os.system('ls -l')
print(files)
```

```
python3 [Pfad/Skriptname]
```

```
#!/usr/bin/python3
```

```
./[Pfad/Skriptname]
```
**Grafische Oberfläche für Skripts**
```
sudo apt-get install python3-tk python-pmw python3-pil
```

![GUI für Python: Die GPIO-Pins lassen sich über Python und eine grafische Oberfläche seteuern (TK/tkinter)](https://www.myria.de/dfiles/github/502_10_LED_GUI.png)


_GUI für Python: Die GPIO-Pins lassen sich über Python und eine grafische Oberfläche steuern (TK/tkinter)_
