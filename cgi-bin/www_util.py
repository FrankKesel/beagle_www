#--------------------------------------------------------------------
#File: 	www_util.py
#Author: F.Kesel
#Date: 	29.12.2015
#Purpose:Functions for the Python CGI-Scripts 
#--------------------------------------------------------------------

#Read an image and store it in an image tag, such that it
#can be embedded in a normal HTML-page as data-url (see: Data-Url)
#arg: fileName: path to the file on disk
#return: image tag to be printed in a Python-CGI-Script 
def readImage(fileName="default"):
	data_uri = open(fileName, 'rb').read().encode('base64').replace('\n', '') 
	img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
	return img_tag

