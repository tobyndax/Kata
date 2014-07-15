#!/usr/bin/python

import sys
import re

small = ""
line = "nonempty"
smallSize = float("inf")

#-------------------------------------------------------------------------------

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#-------------------------------------------------------------------------------

def difference(a,b,c,file):
    
    file = open(file,"r")
    
    global small
    global smallSize
    
    for line in file.readlines():
        data = line.split()
        if(len(data) > b):
            data[a] = re.sub("[^0-9]","",data[a])
            data[b] = re.sub("[^0-9]","",data[b])
        if(len(data) > a and is_number(data[a])):
            currentSize = float(data[a])-float(data[b])
            if(currentSize < smallSize):
                smallSize = currentSize
                small = data[c]
        
    return
    
#-------------------------------------------------------------------------------

if (len(sys.argv) != 2):
    print "The program takes one argument. 0 for football and 1 for weather"
    print "n they will look for respective .dat file for data"
    
if (str(sys.argv[1]) == '0'):
    difference(6,8,1,"football.dat")
    print("The least difference team was " + small)
    print("And the difference was %.0f") %smallSize

if (str(sys.argv[1]) == '1'):
    difference(1,2,0,"weather.dat")
    print("The day was " + small)
    print("And the difference was %.0f") %smallSize
    
    
    
