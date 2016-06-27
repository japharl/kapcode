#!/usr/bin/python

from sense_hat import SenseHat
import sys

print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

sense = SenseHat()

sense.show_message(str(sys.argv))
