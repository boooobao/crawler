# -*- coding: utf-8 -*-
import urllib2
import re
# 不记得是什么功能了
f = open("sor.txt", "r")
t = open('to.txt', "w+")
line = f.readline()
for line in open('sor.txt'):
    print line
    line = line.decode('utf-8')
    #lline = str(line)
    city = re.compile(u'([\u4e00-\u9fa5]+)邮政编码')
    prov = re.compile(u'<h1>([\u4e00-\u9fa5]+)</h1>')
    pr = re.findall(prov, line)
    ci = re.findall(city, line)
    print pr
    print ci

    for i in pr:
        t.write(i.encode('utf-8'))
        t.write(' '+str(len(ci)))
        t.write('\n')
    for i in ci:
        print i
        t.write(i.encode('utf-8'))
        t.write('\n')

    line = f.readline()
