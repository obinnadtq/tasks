# -*- coding: utf-8 -*-
"""
Created on Sun May 19 23:37:33 2019

@author: Obinna Isiwekpeni
"""

def prime_number(user_input):
    
    for x in range(2,user_input+1):
        if user_input % x == 0:
            return 'This is not a prime number'
        
        else:
            return 'You just entered a  prime number'

input_user = int(input('Enter your number: '))
print(prime_number(input_user))
    