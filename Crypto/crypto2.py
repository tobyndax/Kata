#!/usr/bin/python

import codecs
import os
import json

def openFile(path):
    if(os.path.isfile(path)):
        return codecs.open(path, encoding='utf-8', mode='r+')
    raise IOError("Trying to open non-existing file")
    
def createFile(path):
    return codecs.open(path,encoding='utf-8',mode='w+')

def getData(inFile):
    data = inFile.read()
    return data
    
def buildMethod():    
    
    
    
def getMethod():