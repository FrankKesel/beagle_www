#!/usr/bin/python
# -*- coding: UTF-8 -*-

#--------------------------------------------------------------------
#File: 	webcam.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Check password given by calling HTML-Page and then open
# 			image from webcam 
#--------------------------------------------------------------------

import sys
import os, time
import cgi
import cgitb
sys.path.append('/home/frank/python/lib/')
import www_util as util #Local module with utilities

cgitb.enable() #Enable debugging

webcamPath = "/home/frank/python/webcam/"

password = "engstingen" #set the password
#Read form values from the calling html to the list form
form=cgi.FieldStorage()

#Check if image files are available and get dates
if os.path.isfile(webcamPath + "webcam.png"):
	webcamDate = time.ctime(os.path.getmtime(webcamPath + "webcam.png"))
if os.path.isfile(webcamPath + "detected.png"):
	detectDate = time.ctime(os.path.getmtime(webcamPath + "detected.png"))
#Check if motion was detected, i.e. if file exists
if os.path.isfile(webcamPath + "motion_detected"):
	motionDetect = True
else:
	motionDetect = False

#Header
print "Content-type: text/html;charset=utf-8\n\n"
#Title
print """ <html><head><title>Kesel-Cam</title></head><body>"""
 
if "Passwort" not in form:
	print "<h2>ERROR: Please fill in a password!</h2>"
elif password != form["Passwort"].value:
	print "<h2>ERROR: Wrong password!</h2>"
else:
	print "<h4> Webcam Datum: " + webcamDate + "</h4>" 
	print(util.readImage(webcamPath + "webcam.png"))
	if motionDetect == True:
		print "<br><h4> Bewegung erkannt am: " + detectDate + "</h4>" 
		print(util.readImage(webcamPath + "detected.png"))
	else:
		print "<br><h4> Keine Veränderung!</h4>"
		


#End
print "</body> </html>"
