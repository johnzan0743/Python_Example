#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 12:24:50 2020

@author: yuanzhuang
"""


from selenium import webdriver

from bs4 import BeautifulSoup

import requests

import json

import time

import re

import pickle

from WebScrape import  WebScrape

from random import randint

session = requests.Session()

username = 'johnzan'
password = '070743'
url = 'https://auxxxreviews.com/forum/'

open('/Users/yuanzhuang/Downloads/final_link.txt', 'w').close()


driver = webdriver.Chrome('/Users/yuanzhuang/Downloads/chromedriver')
driver.get(url)
driver.find_element_by_id('navbar_username').send_keys(username)
driver.find_element_by_id('navbar_password').send_keys(password)
driver.find_element_by_id('logindetails').submit()
driver.implicitly_wait(30)
path = '/Users/yuanzhuang/Downloads/cookie.txt'

cookie_items = driver.get_cookies()
cookie_dict = {}
for cookie in cookie_items:
    cookie_dict[cookie['name']] = cookie['value']

print(cookie_dict)

key_list = list(cookie_dict.keys())

value_list = list(cookie_dict.values())

final_list=[]
for i in range(len(key_list)-1):
    final_list.append(key_list[i] + '=' + value_list[i] + ';')
    
final_list.append(key_list[len(key_list)-1] + '=' + value_list[len(key_list)-1])

cookies = ' '.join(final_list)
User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

original_link = "https://auxxxreviews.com/forum/f30/"

final_link = []

for index in range(1,14):
    if index == 1:
        link = original_link
    else:
        index = str(index)
        link = original_link + 'index' + index + '.html'
    
    soup, Final = WebScrape(link, User_Agent, cookies)
    A = soup.findAll('h3',{'class':'threadtitle'})
    for _ in range(len(A)):
        final_link.append(A[_].a['href'])

with open('/Users/yuanzhuang/Downloads/final_link.txt','a') as f:
    for i in range(len(final_link)):
        f.writelines(final_link[i]+'\n')
f.close()


    








