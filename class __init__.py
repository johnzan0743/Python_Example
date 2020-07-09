# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Solution():
    def __init__(self,current_name):
        # self.current_name = 'John'
        self.current_name = current_name
        self.all_name = []
        
        
    def add_name(self, former_name):
        current_name = 'Peter'
        print(f'current name is {current_name}')
        print(f'object current name is {self.current_name}')
        self.all_name.append(former_name)
        self.all_name.append(self.current_name)
        former_name.append(self.current_name)
        # self.all_name.append(current_name)
        return self.all_name, former_name
        


Instantiate=Solution(current_name = 'Patrick')
name_list =['Mary', 'Maggie', "Cody"]
A2, A3 = Instantiate.add_name(name_list)
                
    
        
        





