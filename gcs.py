#!/usr/bin/env python

from flask import Flask
app = Flask(__name__)

import dothat.lcd as lcd

import dothat.backlight as backlight

lines = {1:"Ready to connect",2:"",3:""}
settings ={"contrast":49,"r":255,"g":255,"b":255,"hz":0}

backlight.graph_set_led_duty(0,1)

def updateDisplay():
        lcd.clear()
        lcd.set_contrast(settings["contrast"])
        backlight.graph_off()
        backlight.graph_set_led_state(5-settings["hz"],1)
        backlight.rgb(settings["r"],settings["g"],settings["b"])
        lcd.set_cursor_position(0,0)
        lcd.write(lines[1])
        lcd.set_cursor_position(0,1)
        lcd.write(lines[2])
        lcd.set_cursor_position(0,2)
        lcd.write(lines[3])
        return

@app.route("/")
def index():
        return"set val"
@app.route('/line/<int:l>/<string:val>')
def l1(l,val):
        lines[l]=val
        updateDisplay()
        return "ok"
@app.route('/height/<int:hapi>')
def heights(hapi):
        settings["hz"]=hapi
        updateDisplay()
        return "ok"
@app.route('/rgb/<int:r0>/<int:g0>/<int:b0>')
def rgbd(r0,g0,b0):
        settings["r"]=r0
        settings["g"]=g0
        settings["b"]=b0
        updateDisplay()
        return "ok"
@app.route('/contrast/<int:c>')
def contr(c):
        settings["contrast"]=c
        updateDisplay()
        return "oK"
