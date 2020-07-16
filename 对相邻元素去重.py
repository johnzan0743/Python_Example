# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution():
    def unique_list(self, a_list):
        b_list =[]
        for i in range(len(a_list)-1):
            if a_list[i] != a_list[i+1]:
                b_list.append(a_list[i])
        
        if a_list[-2] != a_list[-1]:
            b_list.append(a_list[-1])
        return b_list        

    def unique_enumerate(self,a_list):
        for i, x in enumerate(a_list):
            while i <= len(a_list)-2: 
                if a_list[i+1] == x:
                    a_list[i] = False
                    break
                break
        if a_list[-2] == a_list[-1]:
            a_list[-2] = False
        a_list = list(filter(None,a_list))
        return a_list

A = Solution()

test_list =  [1, 1, 1, 3, 1, 4, 4, 1]
test1 = A.unique_list(test_list)
test2 = A.unique_enumerate(test_list)
        




                
    
        
        





