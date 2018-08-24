#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 20:17:09 2018

@author: babavyas
"""

import urllib
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    html = urlopen('https://zenhabits.net/archives/')
except HTTPError as e:
    print(e)
bs = BeautifulSoup(html.read(), 'html.parser')

list_of_links = []
for a in bs.findAll('a',href=True):
    list_of_links.append(a['href'])

list_of_links = list_of_links[2]

len(list_of_links)

test = urlopen(list_of_links[0])
bs1 = BeautifulSoup(test.read(), 'html.parser')

bs1.find('div', {'class':'post'})

data = {
            'timestamp':[], 
            'title':[], 
            'blog':[]
        }

def get_article_from_link(link,data):
    
    try:
        page_html = urlopen(link)
    except HTTPError as e:
        print(e)
    bs = BeautifulSoup(page_html.read(), 'html.parser')
    timestamp = bs.find('div', {'class':'navigation'}).find('p').get_text()
    timestamp = timestamp.replace('Posted: ','')
    
    title = bs.find('head',).find('title').get_text()
    title = title.replace(':  zen habits', '')
    
    blog = bs.find('div', {'class':'post'},'!h').get_text()
    
    data['timestamp'].append(timestamp)
    data['title'].append(title)
    data['blog'].append(blog)