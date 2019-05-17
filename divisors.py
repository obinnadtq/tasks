# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:44:54 2019

@author: Obinna Isiwekpeni
"""

user_input = int(input('Enter the number: '))

list1 = []

for num in range(1,user_input+1):
    if user_input % num == 0:
        list1.append(num)
print(list1)
        