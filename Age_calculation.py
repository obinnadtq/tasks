# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:42:18 2019

@author: Obinna Isiwekpeni
"""
import datetime
name = input('Please enter your name: ')            #Enter user name
age = int(input('Please enter your age: '))         #Enter user age
age_diff = 100 - age                                #difference between age and 100
todays_date = datetime.datetime.now()   
future_date = todays_date.year + age_diff            #today's date
print('{} you will be 100 years old in the year {}'.format(name, future_date))

#string formating
