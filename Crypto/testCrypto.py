#!/usr/bin/python 
from crypto2 import * 
import unittest
import os

class MyTest(unittest.TestCase):
    
    #File I/Otesting
    def test_open_file(self):
        os.system("touch exist.txt")
        f = openFile('exist.txt')
        self.assertIsNotNone(f)
        f.close()
        os.system("rm exist.txt")
    
    def test_open_file_noexist(self):
        self.assertRaises(IOError,openFile,'noexist.txt')
        
    def test_create_file_noexist(self):
        f = createFile('shouldexist.txt')
        self.assertIsNotNone(f)
        os.system("rm shouldexist.txt")
        
    def test_create_file_exist(self): 
        os.system("touch exist.txt")
        f = createFile('exist.txt')
        self.assertIsNotNone(f)
        
    def test_get_data_from_file(self):
        #---------Setup for file----------
        a = u"this is a teststring"
        f = createFile('test.txt')
        f.write(a)
        f.close()
        #---------------------------------
        f = openFile('test.txt')
        self.assertEqual(getData(f),a,"Written data is not same as read data \n Original: %s \n File: %s"%(a,getData(f)))
        
        os.system("rm test.txt")
        
        
    def test_get_method_from_library(self):
        
    
if __name__ == '__main__':
    unittest.main()
    