# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import re
import requests
ccnt = 0 # 用来计数一共开了多少个网页


headers = {

}

def store(info,city):
    print info
    invnuti = []
    invention = []
    utility = []
    appearance = []
    for i in info:
        invnuti.append(i)

    f = open(u"公开日re.txt", "a")
    f.write(city)
    for i in invnuti:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()



def deal(city):# 函数参数city 城市名 根据城市名生成urlb
    global ccnt
    apply = []
    for i in range(2000,2008):
        time.sleep(2)
        ccnt = ccnt + 1
        data = 'Category=D&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B' + str(i) + '01+TO+' + str(i) + '02%5D%29+DZ%3A%28' + str(city) + '%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://adv.soopat.com/Analytics/Result'
        print i, city
        time.sleep(2)
        number = find(testurl, headers, data, i)

        data = 'Category=D&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B' + str(
            i) + '03+TO+' + str(i) + '04%5D%29+DZ%3A%28' + str(city) + '%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print i, city
        time.sleep(2)
        number1 = find(testurl, headers, data, i)

        data = 'Category=D&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B' + str(
            i) + '05+TO+' + str(i) + '06%5D%29+DZ%3A%28' + str(city) + '%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print i, city
        time.sleep(2)
        number2 = find(testurl, headers, data, i)

        data = 'Category=D&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B' + str(
            i) + '07+TO+' + str(i) + '08%5D%29+DZ%3A%28' + str(city) + '%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print i, city
        time.sleep(2)
        number3 = find(testurl, headers, data, i)

        data = 'Category=D&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B' + str(
            i) + '09+TO+' + str(i) + '10%5D%29+DZ%3A%28' + str(city) + '%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print i, city
        time.sleep(2)
        number4 = find(testurl, headers, data, i)

        data = 'Category=D&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B' + str(
            i) + '11+TO+' + str(i) + '12%5D%29+DZ%3A%28' + str(city) + '%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print i, city
        time.sleep(2)
        number5 = find(testurl, headers, data, i)

        print number
        print number1
        number[0] = int(number[1]) + int(number1[1]) + int(number2[1]) + int(number3[1]) + int(number4[1]) + int(
            number5[1])

        apply.append(number[0])
        store(apply, city)


    #print s.text
    #print s.content

def find(testurl, headers, data, i):
    s = requests.get(testurl, headers=headers, data=data)
    #print s.text
    pip = u'title="'+str(i)+u'年\n(\d+)" />'

    pattern = re.compile(pip)
    number = re.findall(pattern, s.text)
    print number
    return number

def main():
    f = open('999.txt', 'r')
    while 1:
        line = f.readline()
        if not line:
            break
        deal(line)
        n = f.readline()
        for i in range(int(n)):
            line = f.readline()
            deal(line)
    f.close()
    print('total pages:%d' % (ccnt))


if __name__ == '__main__':
    main()

