#!/usr/bin/python
# -*- coding: utf-8 -*-

import codecs

f = codecs.open('test.txt',encoding='utf-8')

dic = [u"å",u"ä",u"ö"]

for line in f:
    for l in line:
        if l in dic:
            print l