#!/usr/bin/python
# -*- coding: UTF-8 -*-

#--------------------------------------------------------------------
#File: 	bmp.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Read the values from the BMP180 sensor and 
#			calculate the temperature and pressure 
#--------------------------------------------------------------------

import os
import re
import subprocess
import www_util as util #Local module with utilities

#Header
print "Content-type:text/html\n\n"
#Title
print """
<html><head><title>BMP180 Sensor Webseite</title></head>
<body><h2>Temperatur und Luftdruck</h2>
"""

print(util.readImage('../images/frosch.png'))

#Start bmp180 program
output = subprocess.Popen(["/home/frank/bin/bmp180"], stdout=subprocess.PIPE)
#Read values from stdout of bmp180
valueString = output.stdout.read()
#Find the numbers in stdout (must be temperature and pressure)
numbers = re.findall(r"[-+]?\d*\.\d+|\d+", valueString)
temperature = numbers[0]
pressure = float(numbers[1])

pSea = pressure * 1.058 #Calculate pressure at sea level

#Print to webserver
print "<h4>Raumtemperatur: " + temperature + " ° Celsius <br>"
print "Luftdruck (Meereshöhe): " + "{:.2f}".format(pSea) + " hPa <br><br>"
#Weather related to pressure
print "Wetterlage: "
if pSea > 1020 :
  print "Hochdruck"
elif pSea > 1000 :
  print "Normal"
else :
  print "Tiefdruck"

#End
print "</h4></body></html>"

