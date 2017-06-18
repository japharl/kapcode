import time
import picamera
import math
import sys
from sense_hat import SenseHat

file = open("/home/pi/kapcode/last.txt","r");
i = int(file.readline())
file.close()

sense = SenseHat()

pre = [255, 0, 0]  # Red

sense.clear(pre)
time.sleep(2)
sense.clear()
camera = picamera.PiCamera()
camera.led = False
camera.resolution=(2592,1944)
camera.start_preview()

while (1==1):
  i = i + 1
  file = open("/home/pi/kapcode/last.txt","w");
  file.write(str(i))
  file.close()
  Threshold = 0.05
  ShakeFlag = True;
  Counter = 1000;
  time.sleep(2)

  # Code translated from https://github.com/danjperron/mpu6050TestInC/tree/master
  while (ShakeFlag):
    data1 = sense.get_accelerometer_raw()
    data2 = sense.get_accelerometer_raw()
    #calculate new force
    CurrentForce = math.sqrt( (data1['x'] - data2['x']) * ( data1['x'] - data2['x']) +
                              (data1['y'] - data2['y']) * ( data1['y'] - data2['y']) +
                              (data1['z'] - data2['z']) * ( data1['z'] - data2['z']))
    #print "Current: " , CurrentForce, "Counter: ", Counter
    if CurrentForce < Threshold :
      ShakeFlag = False
    else :
      Counter = Counter - 1;
    if Counter < 1  :
      ShakeFlag = False
  camera.capture("/home/pi/kapcode/photos/image_" + str(i) + ".jpg")
  time.sleep(2)
  f=open("/home/pi/kapcode/photos/log" + str(i) + ".txt","w");
  f.write("I" + str(i) + "\n" )
  f.write("Humiditiy: " + str(sense.humidity) + "\n")
  f.write("Temp: " + str(sense.temp) + "\n")
  f.write("Pressure:" + str(sense.pressure) + "\n")
  f.close()

  f = open("/home/pi/kapcode/photos/latest.html","w");
  f.write("<HTML><BODY><IMG SRC=\"image_" + str(i) + ".jpg\"></IMG></BODY></HTML>")
  f.close()
