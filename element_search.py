# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 01:41:29 2019

@author: Obinna Isiwekpeni
"""

def search(list1,num):
    if num in list1:
        return True
    else:
        return False
print(search([1,2,3,4,5,7],8))