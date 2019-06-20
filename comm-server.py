#!/usr/bin/env python
print( "Content-type: text/html\n")
import cgitb
import cgi
import datetime
import sqlite3
cgitb.enable()
#command below takes the arguements from the get request and puts them in some sort of a dictionary

inDataDict = cgi.FieldStorage()

print(inDataDict)
#ask that the info will bi in the form of asdfgefs/dataHandler.py?command=getLast
inData = inDataDict["t"].value
print(inData)
