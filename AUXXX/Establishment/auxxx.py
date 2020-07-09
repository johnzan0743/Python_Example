#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 13:56:37 2020

@author: yuanzhuang
"""


from selenium import webdriver

import requests

import json

import pickle

def login1(username, password, url):
    driver = webdriver.Chrome('/Users/yuanzhuang/Downloads/chromedriver')
    driver.get(url)
    driver.find_element_by_id('navbar_username').send_keys(username)
    driver.find_element_by_id('navbar_password').send_keys(password)
    driver.find_element_by_id('logindetails').submit()
    driver.implicitly_wait(30)
    path = '/Users/yuanzhuang/Downloads/cookie.txt'
    
# =============================================================================
#     driver.find_element_by_id('email').send_keys(username)
#     driver.find_element_by_id('pass').send_keys(password)
#     driver.find_element_by_id('login_form').submit()
#     driver.implicitly_wait(30)
# =============================================================================
    cookie_items = driver.get_cookies()
    print(cookie_items) #输出cookies
    return cookie_items
    
    

# =============================================================================
#     with open(path, 'wb') as filehandler:
#         pickle.dump(cookie_items, filehandler)
# 
#     with open(path, 'rb') as cookiesfile:
#         cookies = pickle.load(cookiesfile)
#     
#     header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36',
#             'Host': 'auxxxreviews.com'}
#     res = requests.get(url=url, cookies=cookies, headers=header)
# =============================================================================
    
    # return res
    # wait until the search box is available,
    # which means have succrssfully logged in
    #search = driver.find_element_by_id('q')
    # now are logged in so can navigate to the page of interest
    #driver.get(url)
    # add code to scrape data of interest here


login1('johnzan','070743','https://auxxxreviews.com/forum/')







