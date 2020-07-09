#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:33:23 2020

@author: yuanzhuang
"""


a = {'6HUP ILE 228 D', 
 '6HUP ASN 60 C',
 '6HUP PHE 289 B',
 '6HUP PRO 233 D', 
 '6HUP MET 286 E', 
 '6HUP THR 237 A',
 '6HUP ILE 228 A',
 '6HUP THR 262 B',
 '6HUP PHE 77 C'}

def sorter(item):
    item = item.split(' ')
    
    return(item[-1], item[-2])

sorted_list = sorted(a, key=sorter)


[' '.join(k) for k in sorted([i.split() for i in a], key=lambda x:(x[3],x[2]))]


list =[]
for i in a:
    i = i.split(' ')
    list.append(i)
A = sorted(list, key=lambda x:(x[3], x[2]))
list.clear()
for i in A:
    temp = (' ').join(i)
    list.append(temp)
    
print(list)
    