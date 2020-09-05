# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:47:36 2020

@author: MSI-PC
"""

# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os
import csv
import sys
import importlib
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba
import re # 正则表达式库
import collections # 词频统计库
import numpy as np # numpy数据处理库
import jieba # 结巴分词
import wordcloud # 词云展示库
from PIL import Image # 图像处理库
import matplotlib.pyplot as plt # 图像展示库
import cv2 as cv
importlib.reload(sys)
headers1={
  'user-agent':'Mozilla/5.0'
}#模拟浏览器进行爬取

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3',
'Cache-Control':'max-age=0',
'Connection':'keep-alive',
}


#从tag类中拔出所有的链接并返回链接列表
def get_general(url,tag):
    r=url
    html = requests.get(r,headers=headers)
    html.raise_for_status()
    html.encoding = html.apparent_encoding#内容获取的内容进行转码，以防出现乱码的情况。    
    soup = BeautifulSoup(html.text,'html.parser')
    print(type(soup))
    tmplist = soup.find_all(class_=tag)#获取第一页href相关的位置
    targetlist=[]#爬虫目标的url集合
    for link in (tmplist):
        linklist=(link.find_all('a'))
        for targetlink in linklist:           
            targetlist.append(targetlink.get('href'))
    print(targetlist)
    return targetlist
#获取文字内容
def get_url_text(url):
    r=url
    html = requests.get(r,headers=headers)
    html.raise_for_status()
    html.encoding = html.apparent_encoding#内容获取的内容进行转码，以防出现乱码的情况。    
    soup = BeautifulSoup(html.text,'html.parser')
    tmp = soup.find(class_='content').get_text()#获取第一页href相关的位置
    print(tmp)
    return tmp
url='https://www.eduxiao.com/xeiren/'
# get_general(url,'tabs')
baba='https://www.eduxiao.com/xeiren/238.html'
get_url_text(baba)