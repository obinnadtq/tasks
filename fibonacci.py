# -*- coding: utf-8 -*-
"""
Created on Tue May 21 22:44:13 2019

@author: Obinna Isiwekpeni
"""
def fibonacci(user_input):
    
    fib = [0,1]
    
    for i in range(user_input):
        next_val = fib[i]+fib[i+1]
        fib.append(next_val)
        
    return fib
input_user = int(input('Please enter the number:'))
print(fibonacci(input_user))    

