#!/usr/bin/python
# -*- coding: UTF-8 -*-

#--------------------------------------------------------------------
#File: 	webcam.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Check password given by calling HTML-Page and then open
# 			image from webcam 
#--------------------------------------------------------------------

import cgi
import cgitb
import www_util as util #Local module with utilities

cgitb.enable() #Enable debugging

password = "engstingen" #set the password

#Header
print "Content-type: text/html;charset=utf-8\n\n"
#Title
print """
<html>
<head><title>Kesel-Cam</title></head>
<body>
"""
 
#Read form values from the calling html to the list form
form=cgi.FieldStorage()

if "Passwort" not in form:
	print "<h2>ERROR: Please fill in a password!</h2>"
else:
	s1=form["Passwort"].value
	if s1== password:
		print(util.readImage('../images/webcam.png'))
	else:
		print "<h2>ERROR: wrong password!</h2>"

#End
print "</body> </html>"
