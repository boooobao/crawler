# -*- coding: utf-8 -*-
import csv
import codecs
import re
import chardet

def read(line):
    cnt = 0
    while line == "":
        line = f.readline()
        line = line.replace('\n', '')
        cnt += 1
        if cnt == 5:
            return -1
    return line

csvf = open("total.csv", 'a')
csvf.write(codecs.BOM_UTF8)
writer = csv.writer(csvf)
f = open("sor.txt", "r")
cnt = 0
line = ""
while 1:
    app = ""
    pub = ""
    name = ""
    name = read(name)
    if name == -1:
        break
    app = read(app)
    if app == -1:
        break
    pub = read(pub)
    if pub == -1:
        break
    app = app.split(':')[1]
    app = app.split(' ')
    pub = pub.split(':')[1]
    pub = pub.split(' ')
    na = ["啊士大夫"]
    print name
    na.append(str(name))
    print na
    writer.writerow(na)
    writer.writerow(app)
    writer.writerow(pub)

print line.split(':')