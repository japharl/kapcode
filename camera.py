import time
import picamera
import math
import os
import sys
from sense_hat import SenseHat

# from sense_hat import time

file = open("/home/pi/kapcode/last.txt","r");
i = int(file.readline())
file.close()
sense = SenseHat()

camera = picamera.PiCamera()
camera.led = False
camera.resolution=(2592,1944)
time.sleep(1)

t = sense.pressure

sense.show_message("WAIT")

# Wait till barometric pressure is > 0
# due to bug
while (t == 0.0):
  t = sense.pressure
  time.sleep(1)
  
# Wait till barometric pressure is < last pressure - 2 
# (eg. off the ground)
sense.show_message("READY")

c = t
while ( c > t - .2):
  c = sense.pressure
  time.sleep(1)

sense.show_message("STARTED")
while (True):
  for event in sense.stick.get_events():
    sense.show_message("SHUT DOWN")
    os.sync()
    sys.exit(0)

  i = i + 1
  # Write last photo taken.
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

    print ("Current: " , CurrentForce, "Counter: ", Counter + "\n")
    if (CurrentForce < Threshold) :
      ShakeFlag = False
    else :
      Counter = Counter - 1;
    if (Counter < 1)  :
      ShakeFlag = False
  camera.capture("/home/pi/kapcode/photos/image_" + str(i) + ".jpg")
  os.sync()
  time.sleep(2)
  f=open("/home/pi/kapcode/photos/log" + str(i) + ".txt","w");
  f.write("I" + str(i) + "\n" )
  f.write("Humiditiy: " + str(sense.humidity) + "\n")
  f.write("Temp: " + str(sense.temp) + "\n")
  f.write("Pressure:" + str(sense.pressure) + "\n")
  f.close()
  os.sync()
