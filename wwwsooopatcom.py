# -*- coding: utf-8 -*-
import urllib
import urllib2
import time
import re
import requests
ccnt = 0 # 用来计数一共开了多少个网页

def find(testurl,cookies,i):
    s = requests.get(testurl, cookies=cookies)
    # print s.text
    pip = u'title="' + str(i) + u'年\n(\d+)" />'
    pattern = re.compile(pip)
    print re.findall(pattern, s.text)
    number = re.findall(pattern, s.text)
    return number


def deal(city):# 函数参数city 城市名 根据城市名生成url
    global ccnt
    raw_cookies = ''#cookie
    cookies = {}
    for line in raw_cookies.split(';'):
        key,value = line.split('=', 1)
        cookies[key] = value

    apply = []# 申请日
    topub = []# 公开日
    for i in range(2000, 2016+1):
        time.sleep(2.5)
        ccnt = ccnt + 1 # 计数加一
        testurl = 'http://www.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(%5B'+str(i)+'01%20TO%20'+str(i)+'02%5D)%20DZ%3A('+str(city)+')%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print testurl
        number = find(testurl, cookies, i)
        testurl = 'http://www.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(%5B' + str(i) + '03%20TO%20' + str(i) + '04%5D)%20DZ%3A(' + str(city) + ')%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print testurl
        number1 = find(testurl, cookies, i)
        testurl = 'http://www.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(%5B' + str(i) + '05%20TO%20' + str(i) + '06%5D)%20DZ%3A(' + str(city) + ')%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print testurl
        number2 = find(testurl, cookies, i)
        testurl = 'http://www.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(%5B' + str(i) + '07%20TO%20' + str(i) + '08%5D)%20DZ%3A(' + str(city) + ')%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print testurl
        number3 = find(testurl, cookies, i)
        testurl = 'http://www.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(%5B' + str(i) + '09%20TO%20' + str(i) + '10%5D)%20DZ%3A(' + str(city) + ')%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print testurl
        number4 = find(testurl, cookies, i)
        testurl = 'http://www.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(%5B' + str(i) + '11%20TO%20' + str(i) + '12%5D)%20DZ%3A(' + str(city) + ')%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y'
        print testurl
        number5 = find(testurl, cookies, i)
        number[0] = int(number[0])+ int(number1[0])+int(number2[0]) + int(number3[0])+ int(number4[0])+ int(number5[0])
        number[1] = int(number[1])+ int(number1[1])+int(number2[1]) + int(number3[1])+ int(number5[1])+ int(number5[1])

        if len(number) == 0:#我发现有的网页没有分析信息 eg：http://adv.soopat.com/Analytics/Result?SearchWord=SQRQ%3A(2000)%20DZ%3A(%E5%90%90%E9%B2%81%E7%95%AA%E5%9C%B0%E5%8C%BA)%20&FMZL=Y&SYXX=Y&WGZL=Y&FMSQ=Y
            number.append("("+str(i)+")")# 所以我就把年份加上去了
            number.append("("+str(i)+")")
        apply.append(number[0])
        topub.append(number[1])


    # 我更改了一下顺序 我先把每个城市的信息保存到list里面 然后在一起写入文件
    f = open("xinjiang.txt", "a")
    f.write(city)
    f.write('apply:')
    for i in apply:
        f.write(str(i)+' ')
    f.write('\ntopub:')
    for i in topub:
        f.write(str(i)+' ')
    f.write('\n\n')#换行
    f.close()

def main():
    start = time.clock()#开始时间
    f = open('999.txt','r')
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
    end = time.clock()#结束时间
    print('Running time: %s Seconds' % (end - start))  # 开始时间减去结束时间 就是运行时间了
    print('total pages:%d' % (ccnt))


if __name__ == '__main__':
    main()