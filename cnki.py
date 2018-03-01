# -*- coding: utf-8 -*-
import time
import urllib
import urllib2
import time
import cookielib
import re
import requests


ccnt = 0
def constructtime(city,i):
    x = time.localtime()
    ccity = str(city).encode('hex')
    hexcity = ''
    # print ccity
    for ii in range(len(ccity)):
        if ii % 2 == 0:
            hexcity = hexcity+'%'
        hexcity = hexcity + ccity[ii]
    hexcity = hexcity.upper()[:-3]
    print hexcity
    # print str(i)
    if int(x.tm_sec) < 10:
        sec = '0'+str(x.tm_sec)
    else:
        sec = x.tm_sec
    url = 'http://kns.cnki.net/kns/request/SearchHandler.ashx?action=&NaviCode=*&ua=1.21&PageName=ASP.brief_result_aspx&DbPrefix=SCPD&DbCatalog=%e4%b8%ad%e5%9b%bd%e4%b8%93%e5%88%a9%e6%95%b0%e6%8d%ae%e5%ba%93&ConfigFile=SCPD.xml&db_opt=SCPD&db_value=%E4%B8%AD%E5%9B%BD%E4%B8%93%E5%88%A9%E6%95%B0%E6%8D%AE%E5%BA%93&@thesislevel=%E4%B8%93%E5%88%A9%E7%B1%BB%E5%88%AB%3D3&date_gkr_from='+str(i)+'-01-01&date_gkr_to='+str(i)+'-12-31&txt_1_sel=DZ&txt_1_value1=%E8%A5%BF%E5%AE%89%E5%B8%82&txt_1_relation=%23CNKI_AND&txt_1_special1=%25&his=0&__=Sun%20Jan%2014%202018%20'+str(x.tm_hour)+'%3A'+str(x.tm_min)+'%3A'+str(sec)+'%20GMT%2B0800'
    print url
    return url


def hahacookie():
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open('http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCPD')
    return cookie



}

def bigdeal(city):
    try:
        deal(city)
        return
    except:
        print 'errorrrrrrr'
        time.sleep(2)
        bigdeal(city)


def deal(city):
    text = []
    print city
    for i in range(2000, 2016+1):
        print i
        url1 = constructtime(city, i)
        cookiie = hahacookie()
        s = requests.get(url1, headers=headers, cookies=cookiie)
        t = time.time()
        tt = (int(round(t * 1000)))
        url = 'http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&dbPrefix=SCPD&dbCatalog=%e4%b8%ad%e5%9b%bd%e4%b8%93%e5%88%a9%e6%95%b0%e6%8d%ae%e5%ba%93&ConfigFile=SCPD.xml&research=off&t='+str(tt)+'&keyValue=%E8%A5%BF%E5%AE%89%E5%B8%82&S=1'
        s = requests.get(url, headers=headers, cookies=cookiie)
        pip = u'找到&nbsp;([,0-9]*)&nbsp;'
        # print s.text
        pattern = re.compile(pip)
        number = re.findall(pattern, s.text)
        text.append(number[0])

        print number[0]
    f = open(u'公开日实用新型', 'a')
    f.write(city)
    print text
    for i in text:
        num = str(i).split(',')
        for j in num:
            f.write(j)
        f.write(' ')
    f.write('\n\n')
    f.close()



def main():
    f = open('..\999.txt', 'r')
    while 1:
        line = f.readline()
        if not line:
            break
        bigdeal(line)
        n = f.readline()
        for i in range(int(n)):
            line = f.readline()
            bigdeal(line)
    f.close()
    print('total pages:%d' % (ccnt))


if __name__ == '__main__':
    main()
