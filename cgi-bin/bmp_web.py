#!/usr/bin/python
# -*- coding: UTF-8 -*-

#--------------------------------------------------------------------
#File: 	bmp_web.py
#Author: F.Kesel
#Date: 	01.01.2016
#Purpose:Generate website for BMP180 sensor data 
#--------------------------------------------------------------------

import os, time, sys
import re
import subprocess
sys.path.append('/home/frank/python/lib/')
import www_util #Local module with utilities
import bmp_util
import log_util
from GChartWrapper import *

#Define variables for temperature and pressure graphs
temperatureX = []
temperatureY = []
pressureX = []
pressureY = []

#Read data from logfiles
log_util.readLogFile(bmp_util.logTemp, temperatureX, temperatureY)
log_util.readLogFile(bmp_util.logPress, pressureX, pressureY)

#Construct Google Chart wrapper for temperature graph
G_1 = Line( temperatureY, encoding='text' )
G_1.axes.type('xxyy')
G_1.axes.label( 0, temperatureX[0], temperatureX[len(temperatureX)-1] )
G_1.axes.label( 1, 'Zeit' )
G_1.axes.label( 3, 'Temperatur' )
G_1.axes.range( 2, 15, 25 )
G_1.scale( 15, 25 )
G_1.legend( 'Temperatur' )
G_1.size ( 500, 200 )
G_1.title( "Temperaturverlauf am " + bmp_util.date)

#Construct Google Chart wrapper for pressure graph
G_2 = Line( pressureY, encoding='text' )
G_2.axes.type('xxyy')
G_2.axes.label( 0, pressureX[0], pressureX[len(pressureX)-1] )
G_2.axes.label( 1, 'Zeit' )
G_2.axes.label( 3, 'Luftdruck' )
G_2.axes.range( 2, 950, 1050 )
G_2.scale( 950, 1050 )
G_2.legend( 'Luftdruck' )
G_2.size ( 500, 200 )
G_2.title( "Luftdruckverlauf im Monat " + bmp_util.month )

#Get actual data from BMP180
bmpVal = bmp_util.readBMP180()

#-------------------------The Website----------------------------------
#Header
print "Content-type:text/html\n\n"
#Title
print """
<html><head><title>BMP180 Sensor Webseite</title></head>
<body><h2>Temperatur und Luftdruck</h2>
"""
#Print Frosch
print(www_util.readImage('../images/frosch.png'))

print "<h4> Aktuelle Werte am " + bmp_util.date + ", " + bmp_util.hour + ":<br>" 
print "Raumtemperatur: " + bmpVal[0] + " ° Celsius <br>"
print "Luftdruck (Meereshöhe): " + bmpVal[1] + " hPa <br><br>"

#Print Google charts
print "<img src=\"" + str(G_1) + "\">"
print "<br>"
print "<img src=\"" + str(G_2) + "\">"

#End
print "</h4></body></html>"

