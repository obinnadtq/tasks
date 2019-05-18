# -*- coding: utf-8 -*-
"""
Created on Sat May 18 21:51:43 2019

@author: Obinna Isiwekpeni
"""
user1 = input('User 1 please enter your choice: ')
user2 = input('User 2 please enter your choice: ')

while True:
    if user1.lower() == user2.lower():
        user1 = input('User 1 please enter another choice: ')
        user2 = input('User 2 please enter another choice: ')
        
    elif user1.lower() == 'rock' and user2.lower() == 'scissors':
        print('Congratulations user 1 you are the winner')
        break
    
    elif user2.lower() == 'rock' and user1.lower() == 'scissors':
        print('Congratulations user 2 you are the winner')
        break
     
    elif user1.lower() == 'scissors' and user2.lower() == 'paper':
        print('Congratulations user 1 you are the winner')
        break
    elif user2.lower() == 'scissors' and user2.lower() == 'paper':
        print('Congratulations user 2 you are the winner')
        break
    elif user1.lower() == 'paper' and user2.lower() == 'rock':
        print('Congratulations user 1 you are the winner')
        break
    elif user2.lower() == 'paper' and user1.lower() == 'rock':
        print('Congratulations user 2 you are the winner')
        break





