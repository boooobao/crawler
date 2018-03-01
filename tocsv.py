# -*- coding: utf-8 -*-
import csv
import codecs
import re
import chardet



def read():
    cnt = 0
    line = '\n'
    while line == '\n':
        line = f.readline()
        line = line
        if line =='':
            return -1
    print line
    return line


f = open(u"公开日.txt", "r")
while 1:
    csvf = open(u"公开日.csv", 'ab')
    csvf.write(codecs.BOM_UTF8)
    writer = csv.writer(csvf)
    name = read()
    if name == -1:
        break
    app = read()
    if app == -1:
        break
    name = name.split('\n')
    app = app.split(' ')
    print name
    writer.writerow(name)
    print app
    writer.writerow(app)
    csvf.close()
