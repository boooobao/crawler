# -*- coding: utf-8 -*-
import time
import urllib
import urllib2
import time
import cookielib
import re
import requests


ccnt = 0
def constructtime(city):
    x = time.localtime()
    url = 'http://kns.cnki.net/kns/request/SearchHandler.ashx?action=&NaviCode=*&ua=1.21&PageName=ASP.brief_result_aspx&DbPrefix=SCPD&DbCatalog=%e4%b8%ad%e5%9b%bd%e4%b8%93%e5%88%a9%e6%95%b0%e6%8d%ae%e5%ba%93&ConfigFile=SCPD.xml&db_opt=SCPD&db_value=%E4%B8%AD%E5%9B%BD%E4%B8%93%E5%88%A9%E6%95%B0%E6%8D%AE%E5%BA%93&publishdate_from=2016-01-01&publishdate_to=2016-12-31&txt_1_sel=DZ&txt_1_value1=%E4%B8%8A%E6%B5%B7%E5%B8%82&txt_1_relation=%23CNKI_AND&txt_1_special1=%25&his=0&__=Sat%20Jan%2013%202018%2005%3A12%3A32%20GMT%2B0800'
    print x
    return url

def hahacookie():
    cookie = cookielib.CookieJar()
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler)
    response = opener.open('http://kns.cnki.net/kns/brief/result.aspx?dbprefix=SCPD')
    return cookie

headers1 = {

}

headers2 = {

}

def deal(city):
    text = []
    time.sleep(2)
    url1 = constructtime(city)
    print city
    cookiie = hahacookie()
    s = requests.get(url1, headers=headers1, cookies=cookiie)
    print s.text
    t = time.time()
    tt = (int(round(t * 1000)))
    # url = 'http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&dbPrefix=SCPD&dbCatalog=%e4%b8%ad%e5%9b%bd%e4%b8%93%e5%88%a9%e6%95%b0%e6%8d%ae%e5%ba%93&ConfigFile=SCPD.xml&research=off&t='+str(city)+'&keyValue='+str(city)+'&S=1'
    url = 'http://kns.cnki.net/kns/brief/brief.aspx?pagename=ASP.brief_result_aspx&dbPrefix=SCPD&dbCatalog=%e4%b8%ad%e5%9b%bd%e4%b8%93%e5%88%a9%e6%95%b0%e6%8d%ae%e5%ba%93&ConfigFile=SCPD.xml&research=off&t=1515790275768&keyValue=%E4%B8%8A%E6%B5%B7%E5%B8%82&S=1'
    s = requests.get(url, headers=headers2, cookies=cookiie)
    pip = u'找到&nbsp;(\d+,\d+)&nbsp'
    pattern = re.compile(pip)
    number = re.findall(pattern, s.text)
    print number
    print s.text
    text.append(number[0])
    f = open(u'申请日', 'a')
    f.write(city+'\n')
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
        deal(line)
        n = f.readline()
        for i in range(int(n)):
            line = f.readline()
            deal(line)
    f.close()
    print('total pages:%d' % (ccnt))


if __name__ == '__main__':
    main()
