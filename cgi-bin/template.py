#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi
import cgitb

cgitb.enable() #Enable debugging

#HTML-Header
print "Content-type: text/html;charset=utf-8\n\n"
#Title
print """
<html>
<head><title>Title</title></head>
<body>
"""

print "Template text" 


#End
print "</body> </html>"
	


