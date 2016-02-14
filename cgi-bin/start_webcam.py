#!/usr/bin/python
# -*- coding: UTF-8 -*-

#--------------------------------------------------------------------
#File: 	start_webcam.py
#Author: F.Kesel
#Date: 	7.2.2016
#Purpose:Start webcam
#--------------------------------------------------------------------

import sys
import os
from subprocess import call
import cgi
import cgitb
sys.path.append('/home/frank/python/lib/')
import www_util as util #Local module with utilities

cgitb.enable() #Enable debugging

webcamPath = "/home/frank/python/webcam/"

#Header
print "Content-type: text/html;charset=utf-8\n\n"
#Title
print """
<html>
<head><title>Start Webcam</title></head>
<body>
"""

#Read form values from the calling html to the list form
form=cgi.FieldStorage()
s1=form["Webcam"].value

#If webcam should be started, then generate a file 'start_cam'
#using a system call
#if it should be stopped then remove this file
if s1=="an":
	print "<h4>Webcam gestartet ...</h4>"
	call(["touch", webcamPath + "start_cam"])
elif s1=="aus":
	print "<h4>Webcam gestoppt ...</h4>"
	call(["rm", webcamPath + "start_cam"])
	call(["rm", webcamPath + "motion_detected"])
elif s1=="reset":
	print "<h4>Rücksetzen der Bewegungserkennung ...</h4>"
	call(["rm", webcamPath + "motion_detected"])

#End
print "</body> </html>"
