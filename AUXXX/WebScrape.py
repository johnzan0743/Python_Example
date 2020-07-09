#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 18:42:29 2020

@author: yuanzhuang
"""
import requests
from bs4 import BeautifulSoup

def WebScrape(url, User_Agent, cookies):

    headers = {'User-Agent':User_Agent, 'Cookie':cookies}   
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,'html.parser')
    print('页响应状态码：', res.status_code)
    
    Final = soup.prettify()
    return soup, Final