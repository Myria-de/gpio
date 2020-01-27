#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Grafische Oberfläche für Scripts
# Seite 81
#
# Voraussetzung:
# sudo apt-get install python3-tk python-pmw python3-pil
#

from tkinter import *
from gpiozero import LED
from PIL import Image, ImageTk
from signal import pause

# Bild wechseln für LED an oder aus
def changeimage(img):
    canvas.itemconfig(image_on_canvas, image=my_images[img])

# Ist die LED an oder aus?
def checkstate():
    if(led.value == 1):
        labelText.set('LED-Status: An')
        changeimage(0)
    else:
        labelText.set('LED-Status: Aus')
        changeimage(1)

# LED anschalten
def callback1():
    led.on()
    checkstate()

# LED ausschalten	
def callback2():
    led.off()
    checkstate()


root = Tk()  # Fenster erstellen
root.wm_title("LED-GUI")  # Fenster Titel
root.geometry('250x150')
root.config(background = "#FFFFFF")  # Hintergrundfarbe des Fensters

# Hier kommen die Elemente hin

actionBtn1 = Button(root, text="LED An", width=10, height=1, command=callback1).place(x=70, y=10)
actionBtn2 = Button(root, text="LED Aus", width=10, height=1, command=callback2).place(x=70, y=50)	
labelText = StringVar()
w = Label(root, textvariable=labelText, padx=10, pady=5).place(x=60, y=90)

canvas_width = 24
canvas_height =24
canvas = Canvas(root,
           width=canvas_width,
           height=canvas_height,
           highlightthickness=0)

canvas.place(x=30, y=90)
canvas.config(background = "#FFFFFF")

my_images = []
my_images.append(PhotoImage(file="/home/pi/led-red.png"))
my_images.append(PhotoImage(file="/home/pi/led-grey.png"))
my_image_number = 0

image_on_canvas = canvas.create_image(2, 0, anchor=NW, image = my_images[my_image_number])

# LED an GPIO 23
led = LED("GPIO23")
# Ist die LED an oder aus?
checkstate()

root.mainloop() # GUI wird aktualisiert. Danach keine Elemente setzen.