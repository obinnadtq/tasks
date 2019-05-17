# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:36:52 2019

@author: Obinna Isiwekpeni
"""
string1 = input('Enter the string:')                #request user to input string

for_string = string1[0::]                           # print the string from left to right

rev_string = string1[::-1]                          #print thr string from right to left

if for_string == rev_string:
    print('This is a palindrome')
else:
    print('This is not a palindrome')