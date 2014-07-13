#!/usr/bin/python

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


file = open("football.dat","r")
small = ""
line ="nonempty"
smallSize = float("inf")


for line in file.readlines():
    data = line.split()
    if(len(data) > 6 and is_number(data[6])):
        print("for ",data[6]),
        print(" against",data[8])
        diff = int(data[6])-int(data[8])
        if(diff < smallSize):
            smallSize = diff
            small = data[1]
            
print("Smallest difference goes to " + small)
print("With the difference being ",smallSize)
    

