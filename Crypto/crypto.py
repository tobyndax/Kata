#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os.path
import codecs

def saveToFile(name,data):
    newFile = codecs.open(name, encoding='utf-8', mode='w+')
    newFile.write(data)
    newFile.close()

# Crypto Definitions
cryptoDict = dict()
    
#--------Plain----------------
#No Crypto at all.    
def plain(file):
    data = file.read()
    return data
cryptoDict['plain'] = plain
    
#--------FixedShift----------------
#Shift all letters by a integer    
def fixedShift(file):
    
    try:
        shift = int(input("You selected the Ceasar chiper. Please specify a shift length: "))
        print "%s is the shift integer, continuing"%(shift)
    except:
        print "input is not a integer "
        
    alphabet=["a","b","c","d","e","f","g","h","i","j","k","l",  
        "m","n","o","p","q","r","s","t","u","v","w","x","y","z",u"å",u"ä",u"ö"]
    dic = {}
    for i in range(len(alphabet)):
        dic[alphabet[i]] =alphabet[(i+shift)%len(alphabet)]
    
    dataOut = ""
    dataIn = file.read()
    #for each char in file.
    for l in dataIn.lower():  
            if l in dic:  
                l=dic[l]
            dataOut+=l    #add data to dataOut
        
    return dataOut

cryptoDict['fixedshift'] = fixedShift
    


def main():
#---------------Parsing tests-------------------------
    if len(sys.argv) != 3:
        print "The script takes two arguments. A textfile and a type of crypto"
        return
        
    if not os.path.isfile(sys.argv[1]):
        print "The file %s does not exist"%(sys.argv[1])
        return
    
    if sys.argv[2].lower() not in cryptoDict:
        print "%s is not a valid crypto. Valid cryptos are:" %(sys.argv[2])
        for key, value in cryptoDict.iteritems():
            print key
        return
    
    try:
        rawText = codecs.open(sys.argv[1],encoding='utf-8')
    except:
        print "The specified file was not able to open"
        return
        
    print "successfully passed"
    
    outData = cryptoDict[sys.argv[2].lower()](rawText)
    
    newName =  sys.argv[2].lower() + sys.argv[1]
    saveToFile(newName, outData)
    
#-----------------------------------------------------
    
    
    
if __name__ == '__main__': 
    main()