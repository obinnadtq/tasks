# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:17:57 2019

@author: Obinna Isiwekpeni
"""

list1 = [1,1,2,3,5,8,13,21,34,55,89]

list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]

#using list comprehension to get common list items

print([items1 for items1 in set(list1) for items2 in set(list2) if items1 == items2])  