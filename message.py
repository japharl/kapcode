#!/usr/bin/python

from sense_hat import SenseHat
import sys

sense = SenseHat()

for arg in sys.argv[1:]:
  sense.show_message(arg)
  sense.show_message(" ")
