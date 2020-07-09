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
url2 = 'https://auxxxreviews.com/forum/f100/ada-chatswood-wechat-ada666-777-a-53584/'

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

a = ' '.join(final_list)
User_Agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'

soup, Final = WebScrape(url2, User_Agent, a)


#s = session.get('https://auxxxreviews.com/forum/f100/ada-chatswood-wechat-ada666-777-a-53584/')
# s = requests.get(url2, cookies=cookies)
# soup = BeautifulSoup(s.text, 'html.parser')
# print('页响应状态码：', s.status_code)














