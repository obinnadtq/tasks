# -*- coding: utf-8 -*-
"""
Created on Sun May 19 22:42:07 2019

@author: Obinna Isiwekpeni
"""

import random

random_number = random.randint(1,9)

user_input = int(input('Please enter your guess between 1 and 9: '))

counter = 0

while True:
    if user_input > random_number:
        print('You guessed too high')
        user_input = int(input('Please enter your guess between 1 and 9: '))
        
    elif user_input < random_number:
        print('You guessed too low' )
        user_input = int(input('Please enter your guess between 1 and 9: '))
        
        counter = counter+1
        
    elif user_input == random_number:
        print('You guess is right')
        break
    
    print(counter)

# 3 trials
# when trial ends, ask user to play again
