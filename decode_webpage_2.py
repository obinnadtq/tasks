# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:13:03 2019

@author: Obinna Isiwekpeni
"""

import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')

for story_heading in soup.find_all(class_ = 'content paywall drop-cap'):
    print(story_heading.getText())