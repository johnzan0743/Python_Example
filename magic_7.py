#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 00:13:10 2020

@author: yuanzhuang
"""


class Solution():
    def magic_seven(self, n):
        index = 1
        result = 0
        flag = 1
        while index < n+1:
            if index%7 ==0 or '7' in str(index) :
                result +=flag
                flag = flag * -1
            else:
                result +=flag
            
            index +=1
        # if n%7 == 0 or '7' in str(n):
        #     flag = flag * -1
        
        # result +=flag
        
        return result
    
A=Solution()
QQ = list(range(31))
for i in QQ:
    Q = A.magic_seven(i)
    print(Q)
            