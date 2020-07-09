# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver

from bs4 import BeautifulSoup

import requests

import json

import time

import pickle

from WebScrape import  WebScrape

session = requests.Session()

username = 'johnzan'
password = '070743'
url = 'https://auxxxreviews.com/forum/'

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

url2 = 'https://auxxxreviews.com/forum/'
soup, Final = WebScrape(url2, User_Agent, cookies)
open('/Users/yuanzhuang/Downloads/error.txt','w').close()

open('/Users/yuanzhuang/Downloads/link_list.txt', 'w').close()
open('/Users/yuanzhuang/Downloads/true_link.txt', 'w').close()
open('/Users/yuanzhuang/Downloads/final_link.txt', 'w').close()

for page_num in range(1,72):
    page_num = str(page_num)
    
    if page_num == '1':
        url = 'https://auxxxreviews.com/forum/f100/'
    else:
        url ='https://auxxxreviews.com/forum/f100/index'+page_num+'.html'

    soup, Final = WebScrape(url, User_Agent, cookies)
    
    info = soup.findAll('a')
    
    
    link_list = []
    true_link = []
    final_link = []
    
    for i in range(len(info)):
        a = str(info[i])
        link_list.append(a)
    
    with open('/Users/yuanzhuang/Downloads/link_list.txt', 'a') as f:
        f.writelines("%s\n" % _ for _ in link_list)
    f.close()
    
    for i in range(len(link_list)):
        if '"lastpostdate understate" href' in link_list[i]:
            true_link.append(link_list[i])
               
    with open('/Users/yuanzhuang/Downloads/true_link.txt', 'a') as f:
        f.writelines("%s\n" % _ for _ in true_link)
    f.close()
    

    
    for _ in range(len(true_link)):
        count = 0
        for i, x in enumerate(true_link[_],1):
            if x == '"':
                count +=1
                if count == 3:
                    link_start = i
                elif count == 4:
                    link_end = i
                    break
        temp = true_link[_][link_start:link_end-1]
        temp = temp.split('?')[0]
        # temp = temp[0:len(temp)-1].join('/')
        # temp = '/'.join(temp)
        final_link.append(temp)
    
    
        
    with open('/Users/yuanzhuang/Downloads/final_link.txt', 'a') as f:
        f.writelines("%s\n" % _ for _ in final_link)
    f.close()
                
    
        
        





