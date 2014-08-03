#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

os.system("./crypto.py noexist.txt noexist")
os.system("touch exist.txt")
os.system("./crypto.py exist.txt noexist")
os.system("./crypto.py exist.txt PlaIn")
os.system("./crypto.py exist.txt FixedShift")