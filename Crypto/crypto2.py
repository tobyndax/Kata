#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs
import os
import pickle

def openFile(path):
    if(os.path.isfile(path)):
        return codecs.open(path, encoding='utf-8', mode='r+')
    raise IOError("Trying to open non-existing file")
    
def createFile(path):
    return codecs.open(path,encoding='utf-8',mode='w+')

def getData(path):
    inFile = openFile(path)
    data = inFile.read()
    return data
    
def saveData(data, path):
    file = createFile(path)
    file.write(data)
    file.close()
    
def plain(data):
    return data 
    
def getInput(msg):
    return raw_input(msg)
    
def getShift():
    for i in range(3):
        try:
            shift = int(getInput("Please specify a shift (integer) for the ceasar chipher:"))
            return shift
        except TypeError:
            print "Value must be of integer type"
            pass
    raise TypeError("Non Integer Value from user.")

def buildShiftDict(shift):
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",  
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z",u"å",u"ä",u"ö"]
    dic = {}
    for i in range(len(alphabet)):
        dic[alphabet[i]] = alphabet[(i+shift)%len(alphabet)]
    return dic


def ceasar(path,shift = 0):
    #shift = 3
    if(shift == 0):
        print "Yes!!"
        shift = getShift()
    dataOut=""
    inData = getData(path)
    dic = buildShiftDict(shift)
    for char in inData.lower():
        if char in dic:
            char = dic[char]
        dataOut += char

    return dataOut
    
def buildLibrary(): 
    cryptoDict = dict()
    cryptoDict['ceasar'] = ceasar
    cryptoDict['plain'] = plain   
    with open('library.dat', 'w') as outfile:
      pickle.dump(cryptoDict, outfile)
    
def getLibrary():
    with open('library.dat', 'r') as infile:
      return pickle.load(infile)  

def printMethods():
    print "Available methods are:"
    for key, value in getLibrary().iteritems():
        print key
         
def getMethod(method):
    try:
        outMethod = getLibrary()[method]
        return outMethod
    except KeyError:
        printMethods()
        raise
        
def main():
    buildLibrary()
    
    path = raw_input("Please specify the path to the textfile: ")
    data = getData(path)
    printMethods()
    method = raw_input("Please choose a method to apply: ")
    
    
    newData = getMethod(method)(path)
    
    newfilename = method+path
    saveData(newData,newfilename)
if __name__ == '__main__':    
    main()
    
    
    
