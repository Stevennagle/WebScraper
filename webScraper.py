#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

with open('example.html') as html_file:
	soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify())
#match = soup.title.text
#match = soup.div
match = soup.find('div', class_='footer')
print(match)
