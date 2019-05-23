# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:17:08 2019

@author: Obinna Isiwekpeni
"""

def reverse_string(string):
    split_string = string.split()                    #split the string
    reverse_string = split_string[::-1]              #reverse the string
    return ' '.join(reverse_string)                  #join the string
print(reverse_string(''))