#!/usr/bin/env python3
print( "Content-type: text/html\n")
import cgitb
import cgi
import json
import datetime
import sqlite3
cgitb.enable()
"""
# related files are:
  * name_to_msg.json -- maps names to the message they will send\
  * msg_history.txt  -- keeps track of the msgs that were sent. This is used to retrieve msgs - 
                        aka send them to the clients. Also cool to see history.
"""


DEFAULT_MSG = "I'm shouting and barfing hysterically"

def update_msgs(data):
    """
    function that updates the file msg_history.txt with a new msg request
    Arguments:
        data {} -- data of form {"sender": string_sender_name}
    """
    # take the msg that corresponds to the name in the json file, revert it to default for future use, and send the msg to msg_history.txt
    # if name is not in the json file, then add it and assign default msg
    with open("name_to_msg.json", 'r') as name_to_msg_data:
        name_to_msg = json.load(name_to_msg_data)
        print("\n")
        print(name_to_msg)
        print("<br>", data["sender"].value)
        
    
    



if __name__ == "__main__":
    #ask that the info will bi in the form of asdfgefs/dataHandler.py?command=getLast
    #command below takes the arguements from the get request and puts them in some sort of a dictionary
    inDataDict = cgi.FieldStorage()
    # update the msg_history.txt file with the new msg
    update_msgs(inDataDict)
