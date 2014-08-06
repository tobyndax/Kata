#!/usr/bin/python 
# -*- coding: utf-8 -*-
from crypto2 import * 
import unittest
import os


def touch(path):
    open(path, 'a').close()

class MyTest(unittest.TestCase):
    
    #File I/Otesting
    def test_open_file(self):
        touch('exist.txt')
        f = openFile('exist.txt')
        self.assertIsNotNone(f)
        f.close()
        os.remove('exist.txt')
    
    def test_open_file_noexist(self):
        self.assertRaises(IOError,openFile,'noexist.txt')
        
    def test_create_file_noexist(self):
        f = createFile('shouldexist.txt')
        self.assertIsNotNone(f)
        os.remove('shouldexist.txt')
        
    def test_create_file_exist(self): 
        touch('exist.txt')
        f = createFile('exist.txt')
        self.assertIsNotNone(f)
        
    def test_save_and_get_data_from_file(self):
        #---------Setup for file----------
        a = "this is a teststring"
        saveData(a,'test.txt')
        self.assertEqual(getData('test.txt'),a,"Written data is not same as read data \n Original: %s \n File: %s"%(a,getData('test.txt')))
        
        os.remove('test.txt')
        
    def test_build_library(self):
        touch('library.dat')
        os.remove('library.dat')
        buildLibrary()
        self.assertIs(getLibrary()['plain'],plain,"The plain method is missing from library")
        os.remove('library.dat')
        
    def test_get_method(self):
        buildLibrary()
        self.assertIs(getMethod('plain'),plain,"Get method does not get 'plain'")
        
    def test_get_method_noexist(self):
        buildLibrary()
        self.assertRaises(KeyError,getMethod,'garbage')
        
    def test_apply_method(self):
        a = "this is a teststring"
        data = getMethod('plain')(a)
        self.assertEqual(data,a,"plain method not returning same string")
    
    def test_build_shift_dict(self):
        a  = {u'\xf6': 'c', u'\xe5': 'a', u'\xe4': 'b', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': u'\xe4', 'x': u'\xe5', 'z': u'\xf6'}
        self.assertEqual(a,buildShiftDict(3),"Build Shift does not shift correctly: \n %s"%buildShiftDict(3))
    def test_Shift(self):
        touch('test.txt')
        file = codecs.open('test.txt',encoding='utf-8',mode='w+')
        file.write(u"abcdefghijklmnopqrstuvwxyzåäö")
        file.close()
        b = u"defghijklmnopqrstuvwxyzåäöabc"
        self.assertEqual(ceasar('test.txt',shift = 3),b,"Ceasar function not returning properly shifted data: %s"%ceasar('test.txt',3))

    
if __name__ == '__main__':
    unittest.main()
    