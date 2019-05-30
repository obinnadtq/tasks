# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:04:44 2019

@author: Obinna Isiwekpeni
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.nytimes.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

for story_heading in soup.find_all(class_ = 'css-1qwxefa esl82me0'):
    print(story_heading)