# -*- coding: utf-8 -*-
"""
Created on Thu May 23 21:51:36 2019

@author: Obinna Isiwekpeni
"""
#import string library
import string
#import random library
import random

characters = string.ascii_letters + string.punctuation  + string.digits

password =  "".join(random.choice(characters) for x in range(random.randint(10,15)))

print (password)