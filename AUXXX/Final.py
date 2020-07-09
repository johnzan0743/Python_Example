#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 12:44:46 2020

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

with open('/Users/yuanzhuang/Downloads/final_link.txt', 'r') as f:
    url_list = f.readlines()
f.close()

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

open('/Users/yuanzhuang/Downloads/error.txt','w').close()


for url_num in range(len(url_list)):
    # url2 = 'https://auxxxreviews.com/forum/f100/ada-chatswood-wechat-ada666-777-a-53584/'
    url2 = url_list[url_num].strip()
    if url2[-5:-1] == '-new':
        url2 = url2[0:-5]+'/'
        
    # url2 = url2[:url2.find('post')-1]+'/'
    # url2 = 'https://auxxxreviews.com/forum/f100/tina-riverstone-0422-286-993-a-69353/'
    

    soup, Final = WebScrape(url2, User_Agent, cookies)
    
    try:   
        last = soup.findAll('span',{'class':'first_last'})
        if last:
    
            last_page_url = last[0].a['href']
            last_page_number = last_page_url.split('/')
            last_page_number = last_page_number[len(last_page_number)-1][5:-5]
        else:
            last_page_number = 1
    except:
        pass
    

    try:
        open('/Users/yuanzhuang/Downloads/'+ soup.findAll('span',{'class':'threadtitle'})[0].text+'.txt','w').close()
    except:
        file_title = soup.findAll('span',{'class':'threadtitle'})[0].text
        file_title = re.sub('[\/:*?"<>|]','-',file_title)
        open('/Users/yuanzhuang/Downloads/'+file_title+'.txt', 'w').close()
        

            
        
    
    for num in range(1,int(last_page_number)+1):
        if num == 1:
            soup, Final = WebScrape(url2, User_Agent, cookies)
        else:
            soup, Final = WebScrape(url2+'index'+str(num)+'.html', User_Agent, cookies)
    
    
    
        
        username_list = []
        user_names = soup.findAll('div',{'class':'username_container'})
        
        for i in range(len(user_names)):
           #username_list.append((user_names[i].text))
           a = user_names[i].text.strip()
           username_list.append(a[0:a.find('\n')])
        
        postcounter = []
        counter = soup.findAll('a', {'class':'postcounter'})
        
        for i in range(len(counter)):
            postcounter.append(counter[i].text)
            
        
        date_time = []
        date = soup.findAll('span', class_ = 'date')
        #time = soup.findAll('span', class_ = 'time')
        
        for i in range(len(date)):
            date_time.append(date[i].text.replace('\xa0',' '))
        
        if num == 1:
            thread_title = soup.findAll('span',{'class':'threadtitle'})[0].text
        
        page_number = soup.findAll('div',{'class':'pagination_top'})[0].text
        page_number = page_number.strip()
        page_number = page_number[0:page_number.find('\n')]
        
        
        post_title = []
        title = soup.findAll('div',{'class':'postbody'})
        for i in range(len(title)):
            if title[i].h2 is None or title[i].h2.text.isspace() == True:
                title[i] = 'None'
                post_title.append(title[i].strip())
            else:
                post_title.append(title[i].h2.text)
        
        
        post_content = []
        content = soup.findAll('div',{'class':'content'})
        for j in range(len(content)):
            a = content[j].text
            a = a.replace('\x91','\'')
            a = a.replace('\x92', '\'')
            a = a.replace('\x93', '"')
            a = a.replace('\x94', '"')
            a = a.strip()
            if len(content[j].findAll('div',{'class':'message'})) > 0:
                quotation = content[j].findAll('div',{'class':'quote_container'})
                b = quotation[0].text
                b = b.replace('\x91','\'')
                b = b.replace('\x92', '\'')
                b = b.replace('\x93', '"')
                b = b.replace('\x94', '"')
                b = b.strip()
                
                if a[len(b)-1] == b[len(b)-1]:
                    post_content.append('"""\n' + a[0:len(b)-1] + '\n"""\n' + a[len(b):])
                    # print(f'j is {j}\n')
                    # print(f'a is {a}\n')
                    # print(f'b is {b}\n')
                    continue
                
            post_content.append(a)
                      
                
            
        
        
        quotation_message = []
        quotation = soup.findAll('div',{'class':'message'})
        for i in range(len(quotation)):
            a = quotation[i].text
            a = a.replace('\x91','\'')
            a = a.replace('\x92', '\'')
            a = a.replace('\x93', '"')
            a = a.replace('\x94', '"')
            a = '""""\n' + a + '\n' + '"""'
            quotation_message.append(a)
            
            
        
        print(post_title[0])
        
        try:
            with open('/Users/yuanzhuang/Downloads/'+ soup.findAll('span',{'class':'threadtitle'})[0].text+'.txt','a') as f:
                f.writelines('Thread Title: ' + thread_title + '\n')
                try:
                    for _ in range(len(content)):
                        f.writelines('Floor: ' + postcounter[_] + '\n')
                        f.writelines('Post Time: ' + date_time[_] + '\n')
                        f.writelines('Poster ID: ' + username_list[_] + '\n')
                        f.writelines('Post Title: ' + post_title[_] + '\n')
                        f.writelines('Post Content: \n' + post_content[_] + '\n\n\n')
                except:
                    pass
            f.close()
        except:
            with open('/Users/yuanzhuang/Downloads/'+file_title+'.txt','a') as f:                
                try:
                    for _ in range(len(content)):
                        f.writelines('Floor: ' + postcounter[_] + '\n')
                        f.writelines('Post Time: ' + date_time[_] + '\n')
                        f.writelines('Poster ID: ' + username_list[_] + '\n')
                        f.writelines('Post Title: ' + post_title[_] + '\n')
                        f.writelines('Post Content: \n' + post_content[_] + '\n\n\n')
                except:
                    pass
            f.close()
            
            
            with open('/Users/yuanzhuang/Downloads/error.txt','a') as f:                
                try:
                    for _ in range(len(content)):
                        f.writelines('Floor: ' + postcounter[_] + '\n')
                        f.writelines('Post Time: ' + date_time[_] + '\n')
                        f.writelines('Poster ID: ' + username_list[_] + '\n')
                        f.writelines('Post Title: ' + post_title[_] + '\n')
                        f.writelines('Post Content: \n' + post_content[_] + '\n\n\n')
                except:
                    pass
            f.close()
    print('OK')
    # rand_number = randint(0,5)
    # time.sleep(rand_number)
    
        
    
        

    
        
        








                
    
        
        





