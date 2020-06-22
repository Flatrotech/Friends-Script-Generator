#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    This python script is used as a web scraper to gather all Friends scripts through various links
    found at this website https://fangj.github.io/friends/
"""

# Import Packages
import httplib2
from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import os

# root directory of the project
root_path = os.path.dirname(os.path.realpath(__file__))

# Declare an http object
http = httplib2.Http()

# Get the status and respose from the webpage
status, response = http.request('https://fangj.github.io/friends/')

# Create a list
links = []

# (same directory) in append mode and 
file1 = open(root_path + "/dataset/dataset.txt","a", encoding="utf-8") 

# Open the webpage, declaring the right decoder and parser
parser = 'html.parser'  # or 'lxml' (preferred) or 'html5lib', if installed
resp = urllib.request.urlopen("https://fangj.github.io/friends/")
soup = BeautifulSoup(resp, parser, from_encoding=resp.info().get_param('charset'))

# Add hyperlinks to a list
for link in soup.find_all('a', href=True):
    links.append("https://fangj.github.io/friends/" + link['href'])

# Open each webpage, read all text, then write the text to a file
for i in range(0, len(links)):
    resp = urllib.request.urlopen(links[i])
    print("Reading " + str(resp))
    soup = BeautifulSoup(resp, features="lxml")
    txt = soup.get_text()
    file1.write(txt)

# Close the file
file1.close()
