mport time
import math
from sense_hat import SenseHat

# This should be installed in /home/pi

sense = SenseHat()

pre = [255, 0, 0]  # Red

post = [0,255,0]

sense.clear(pre)
# Code translated from https://github.com/danjperron/mpu6050TestInC/tree/master
Threshold = 0.1
ShakeFlag = True;
Counter = 1000;

camera = picamera.PiCamera()
camera.resolution = (2592, 1944)
camera.iso=800
camera.start_preview()
time.sleep(2)

while (ShakeFlag):

  data1 = sense.get_accelerometer_raw()

  data2 = sense.get_accelerometer_raw()

     #calculate new force
  CurrentForce = math.sqrt( (data1['x'] - data2['x']) * ( data1['x'] - data2['x']) +
                            (data1['y'] - data2['y']) * ( data1['y'] - data2['y']) +
                            (data1['z'] - data2['z']) * ( data1['z'] - data2['z']))

  print "Current: " , CurrentForce, "Counter: ", Counter
  # If we are not shaking...
  if CurrentForce < Threshold :
    ShakeFlag = False
  else :
    Counter = Counter - 1;
      if Counter < 1  :
        ShakeFlag = False
sense.clear()

camera.capture('image.jpg')
sense.clear(post)
time.sleep(2)
sense.clear()
camera.stop_preview()
print("Humiditiy: ")
print(sense.humidity)
print("Temp: ")
print(sense.temp)
print("Pressure:")
print(sense.pressure)
