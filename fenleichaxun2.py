# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import re
import requests
ccnt = 0 # 用来计数一共开了多少个网页

headers = {

}

def store(city,invnuti,invention,utility,appearance):
    f = open(u"发明和实用新型公开日期re.txt", "a")
    f.write(city)
    for i in invnuti:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()

    f = open(u"发明专利公开日期re.txt", "a")
    f.write(city)
    for i in invention:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()

    f = open(u"实用新型公开日期re.txt", "a")
    f.write(city)
    for i in utility:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()

    f = open(u"外观设计公开日期re"
             u".txt", "a")
    f.write(city)
    for i in appearance:
        f.write(str(i) + ' ')
    f.write('\n\n')
    f.close()


def deal(city):# 函数参数city 城市名 根据城市名生成url
    global ccnt
    a = []
    b = []
    c = []
    d = []
    for i in range(2000, 2016+1):
        time.sleep(2)
        ccnt = ccnt + 1
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B'+str(i)+'01+TO+'+str(i)+'02%5D%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number = hurtspirit(testurl, headers, data, i)

        time.sleep(2)
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B'+str(i)+'03+TO+'+str(i)+'04%5D%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number1 = hurtspirit(testurl, headers, data, i)

        time.sleep(2)
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B'+str(i)+'05+TO+'+str(i)+'06%5D%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number2 = hurtspirit(testurl, headers, data, i)

        time.sleep(2)
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B'+str(i)+'07+TO+'+str(i)+'08%5D%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number3 = hurtspirit(testurl, headers, data, i)

        time.sleep(2)
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B'+str(i)+'09+TO+'+str(i)+'10%5D%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number4 = hurtspirit(testurl, headers, data, i)

        time.sleep(2)
        data = 'Category=GKRQY&MainChartType=&AnalyticsPatentType=&DisplayCount=20&DisplayType=&Db=&Embed=&IpcIdc=0&FolderIds=&Valid=-1&SearchWord=GKRQ%3A%28%5B'+str(i)+'11+TO+'+str(i)+'12%5D%29+DZ%3A%28'+str(city)+'%29+&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        testurl = 'http://www2.soopat.com/Analytics/Result'
        print i, city
        x = 0
        while x == 0:
            x, number5 = hurtspirit(testurl, headers, data, i)

        for i in range(10):
            number[i] = int(number[i])+int(number1[i])+int(number2[i])+int(number3[i])+int(number4[i])+int(number5[i])


        while len(number) < 10:
            number.append(0)
        print number
        a.append(number[2])
        b.append(number[4])
        c.append(number[6])
        d.append(number[8])
    store(city, a, b, c, d)

def hurtspirit(testurl, headers, data, i):
    try:
        number = find(testurl, headers, data, i)
    except:
        number = []
        print "mmp"
        time.sleep(5)
        return 0, number

    return 1, number




def find(testurl, headers, data, i):
    s = requests.get(testurl, headers=headers, data=data)
    #print s.text
    pip = str(i)+u'年.?\n 数量：(\d+)" />'
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

