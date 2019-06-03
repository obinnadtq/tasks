# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 01:49:49 2019

@author: Obinna Isiwekpeni
"""

import requests
from bs4 import BeautifulSoup


url = "http://www.nytimes.com/"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
with open('file_to_write.txt','w') as f:
    for story_heading in soup.find_all(class_ = 'css-1qwxefa esl82me0'):
          f.write(story_heading.get_text() + '\n')
f.close()