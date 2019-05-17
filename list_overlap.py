# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:59:24 2019

@author: Obinna Isiwekpeni
"""

list1 = [1,1,3,3,5,6,8,9,11]

list2 = [1,1,5,6,8,9,10]

new_list = []

for num1 in set(list1):
    for num2 in set(list2):
        if num1 == num2:
            new_list.append(num1)
print(new_list)
            


    