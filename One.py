#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import urllib3
import urllib.request
import time
from requests_html import HTMLSession,UserAgent

print("********************")
print("  ####   ####")
print(" #       #")
print("#        ####")
print(" #       #")
print("  ####   #")
print("********************")
print("github:https://github/hapuren")
print("web:http://hapuren.nsjiasu.com/")
print("")
url = input("请输入您要爬的网址(后面记得加/)：")
response = requests.get(url)
html = urllib.request.urlopen(url=url)
urllib3.disable_warnings()
http = urllib3.PoolManager()
r = http.request('GET',url)
session = HTMLSession()
ua = UserAgent().random
u = session.get("https://seo.chinaz.com/"+url,
                headers = {'user-agent':ua})
u.enconding='gb2312'


print("[                    ] 0% ")
time.sleep(5)
print("[=====               ] 25%")
time.sleep(5)
print("[==========          ] 50%")
time.sleep(5)
print("[===============     ] 75%")
time.sleep(5)
print("[====================] 100%")
time.sleep(3)
if u.status_code == 200:
    div_list = u.html.xpath('.//div[@class="_chinaz-seo-new1 wrapper mb10"]/div')
    i_list = u.html.xpath('.//i[@class="color-2f87c1"]/a')
    i_1 = u.html.xpath('.//td[@class="w62-0"]/div')
    for div in div_list:
        title = div.find('div[@class="_chinaz-seo-t2l ellipsis"]')[0].text
        print("---------------分界线---------------")
        print("网站标题：",title)
        time.sleep(2)
    for i in i_list:
        icp = i.find('a[@target="_blank"]')[0].text
        print("---------------分界线---------------")
        print("备案号：",icp)
        time.sleep(2)
    for ms in i_1:
        ms = ms.find('div[@class="ball color-63"]')[0].text
        print("---------------分界线---------------")
        print("网页描述：",ms)
        time.sleep(2)
print("---------------分界线---------------")
print("响应代码为：",response.status_code)
time.sleep(2)
print("---------------分界线---------------")
print("网络请求地址为：",response.url)
time.sleep(2)
print("---------------分界线---------------")
print("头部信息为：",response.headers)
time.sleep(2)
print("---------------分界线---------------")
print("cookie信息为：",response.cookies)
time.sleep(2)
print("---------------分界线---------------")
print("默认重试请求为：",r.retries.total)
time.sleep(2)
print("---------------分界线---------------")
print("网页源码：\n",html.read().decode("utf-8"))
print("                                                                                                                 ")
print("版权所有：哈葡人")
