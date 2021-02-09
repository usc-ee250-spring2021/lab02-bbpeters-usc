""" EE 250L Lab 02: GrovePi Sensors

Bradford Peterson

https://www.github.com/usc-ee250-spring2021/lab02-bbpeters-usc
"""

"""python3 interpreters in Ubuntu (and other linux distros) will look in a 
default set of directories for modules when a program tries to `import` one. 
Examples of some default directories are (but not limited to):
  /usr/lib/python3.5
  /usr/local/lib/python3.5/dist-packages

The `sys` module, however, is a builtin that is written in and compiled in C for
performance. Because of this, you will not find this in the default directories.
"""
import sys
import time
# By appending the folder of all the GrovePi libraries to the system path here,
# we are successfully `import grovepi`
sys.path.append('../../Software/Python/')
# This append is to support importing the LCD library.
sys.path.append('../../Software/Python/grove_rgb_lcd')

import grovepi
from grove_rgb_lcd import *

"""This if-statement checks if you are running this python file directly. That 
is, if you run `python3 grovepi_sensors.py` in terminal, this if-statement will 
be true"""
if __name__ == '__main__':
    DPORT = 4    # D4 - Digital Port
    APORT = 0    # A0 - Analog Port

    while True:
        #So we do not poll the sensors too quickly which may introduce noise,
        #sleep for a reasonable time of 200ms between each iteration.
        time.sleep(0.2)

        #Threshold read in cm from rotary  angle sensor. Range is [0,1023]
        threshold = grovepi.analogRead(APORT)

        #Distance read in cm from the ultrasonic ranger
        dist = grovepi.ultrasonicRead(DPORT)

        #If the measured distance falls within the threshold, change screen to
        #red and print the two readings with OBJ PRES
        if dist <= threshold:
            setRGB(255,0,0)
            setText_norefresh(str(threshold) + "cm OBJ PRES   " + str(dist) + "cm")
	#Otherwise simply report the threshold and distance with a green background
        else:
            setRGB(0,255,0)
            setText_norefresh(str(threshold) + "cm            " + str(dist) + "cm")
