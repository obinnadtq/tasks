# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:25:38 2019

@author: Obinna Isiwekpeni
"""
new_list = []
def list_ends(lists):
    first_element = lists[0]
    last_element = lists[-1]
    new_list.append(first_element)
    new_list.append(last_element)
    return new_list

print(list_ends([5,10,15,20,25]))

# scopes, variable scope
