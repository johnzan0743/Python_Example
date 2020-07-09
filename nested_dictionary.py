#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:07:33 2020

@author: yuanzhuang
"""

class Solution():
    def __init__(self):
        
        self.key_list = []
        self.value_list =[] 
        self.index = 0
    def nest_dictionary(self, dictionary):


        for key, value in dictionary.items():
            # self.key_list.append(self.index)
            print(key)
            print(value)
            # self.key_list.append(self.index)
            if type(value) is dict:

                self.key_list.append(key)
                self.index +=1
                self.key_list.append(self.index)
                self.nest_dictionary(value)
                self.index -=1

            else:
                print('continue')
                self.key_list.append(key)
                self.value_list.append(value)
                self.index +=1
                self.key_list.append(self.index)
                self.index -=1
                continue
        return self.key_list, self.value_list
    
    def search(self, key_list, value_list,keyword):
        
        final_string = keyword
        flag = False
        for i in range(len(value_list)):
            if keyword in value_list[i]:
                flag = False
                value_list_index = i
            else:
                flag = True
            
        if keyword not in key_list and flag is True:
            print(f'不存在关键字：{keyword}')
        elif keyword in value_list[value_list_index]:
            max_level = max(key_list[1:len(key_list):2])
            for j in range(len(value_list)):
                for i, x in enumerate(key_list):
                    if x == max_level:
                        key_list[i] = value_list[j]
                        print('OHHHHH')
                        break
            print(key_list)
            key_list.reverse()
            for i in range(len(key_list)):
                if type(key_list[i]) is list and keyword in key_list[i]:
                    start_index = i
                    final_string = final_string + '.' + key_list[start_index+1]
            level_index = max_level-1
            while level_index >= 1:
                string = key_list[key_list[start_index:].index(level_index)+1]
                final_string = final_string + '.'+ string
                level_index -=1
                print(final_string)
        return final_string
                
                
        

        
            





a = {"奴隶社会": {"亚洲": {"古印度": ["种姓制度", "佛教的创立"], "两河流域文明": ["汉谟拉比法典"]}, "欧洲": {"希腊罗马古典文化": ["建筑艺术", "公历"], "罗马": ["城邦", "帝国的征服与扩展"], "希腊": ["希腊城邦", "雅典民主"]}, "非洲": {"古埃及文明": ["金字塔"]}}}


B=Solution()
key_list, value_list = B.nest_dictionary(a)

Q = B.search(key_list, value_list, '金字塔')















