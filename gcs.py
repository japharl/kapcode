#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Note - a bunch of stuff here was directly imported from adafruit source code for rpi oled library.

RST = None     # on the PiOLED this pin isnt used
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

disp.begin()

# Clear display.
disp.clear()
disp.display()


width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Load default font.

font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
#

cmd = "hostname -I | cut -d\' \' -f1"
IP = subprocess.check_output(cmd, shell = True )

lines = {1:"IP:" + str(IP),2:"",3:"",4:""}

def updateDisplay():
        disp.clear()
        disp.display()
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        draw.text((x, top), lines[1],  font=font, fill=255)
        draw.text((x, top + 8), lines[2],  font=font, fill=255)
        draw.text((x, top + 16), lines[3],  font=font, fill=255)
        draw.text((x, top + 24), lines[4],  font=font, fill=255)
        disp.image(image)
        disp.display()
        return

@app.route("/")
def index():
        return"/line/[1234]/string:val"
@app.route('/line/<int:l>/<string:val>')
def l1(l,val):
        lines[l]=val
        updateDisplay()
        return "ok"

lines[2]="Run this via flask"
updateDisplay()
