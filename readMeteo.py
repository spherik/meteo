#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial  
import time  
import sqlite3
from datetime import datetime, timedelta

locations=['/dev/ttyUSB0','/dev/ttyUSB1','/dev/ttyUSB2','/dev/ttyUSB3',  
'/dev/ttyS0','/dev/ttyS1','/dev/ttyS2','/dev/ttyS3']    

def connect():
    try:
        # Creates or opens a file called meteo with a SQLite3 DB
        db = sqlite3.connect('/home/pi/sketchbook/Meteo/meteo')
        # Get a cursor object
        cursor = db.cursor()
        # Check if table meteo does not exist and create it
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS meteo(id INTEGER PRIMARY KEY, date TEXT,
                       temp INTEGER, humidity INTEGER, light INTEGER, moisture INTEGER)
                       ''')
    	# Commit the change
    	db.commit()
    # Catch the exception
    except Exception as e:
        # Roll back any change if something goes wrong
        db.rollback()
        raise e
    finally:
        # Close the db connection
        db.close()

def readMeteo():
    line = arduino.readline();
    print datetime.now().strftime("%Y-%m-%d %H:%M:%S")+";"+line
    temperature, humidity, light, moisture, newline = line.split(';');
    try:
        # Creates or opens a file called meteo with a SQLite3 DB
        db = sqlite3.connect('/home/pi/sketchbook/Meteo/meteo')
        # Get a cursor object
        cursor = db.cursor()
        # Insert new values
        cursor.execute("INSERT INTO Meteo(date, temp, humidity, light, moisture) VALUES(?, ?, ?, ?, ?)", (datetime.now(), temperature, humidity, light, moisture))
        # Commit the change
    	db.commit()
    except Exception as e:
        # Roll back any change if something goes wrong
        db.rollback()
        raise e
    finally:
        # Close the db connection
        db.close()
        
        
for device in locations:    
    try:    
        print "Trying...",device  
        arduino = serial.Serial(device, 9600)   
        break  
    except:    
        print "Failed to connect on",device
connect()     
#while 1 :
readMeteo()
    #time.sleep(300)
 
