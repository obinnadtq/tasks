# -*- coding: utf-8 -*-
"""
Created on Fri May 17 20:35:03 2019

@author: Obinna Isiwekpeni
"""

user_input = int(input('Enter a number:'))          #user input

list_1 = [1,1,2,3,5,8,13,21,34,55,89]               #list of numbers

new_list = []                                       #empty list

for num in list_1 :
    if num < user_input:
        new_list.append(num)
        
print(new_list)