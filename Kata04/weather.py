#!/usr/bin/python


file = open("weather.dat","r")
small = ""
line ="nonempty"
smallSize = float("inf")
file.readline()
file.readline() #remove header and blankline
for line in file.readlines():
    data = line.split()
    data[1] = data[1].replace('*','')
    data[2] = data[2].replace('*','')
    currentSize = float(data[1])-float(data[2])
    if(currentSize < smallSize):
        smallSize = currentSize
        small = data[0]
    
print("The day with the least difference was " + small)
print("And the difference was %.0f") %smallSize

        
    
    

