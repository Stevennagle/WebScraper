#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

#Pulling info from example.html
#with open('example.html') as html_file:
#	soup = BeautifulSoup(html_file, 'lxml')

#print(soup.prettify())
#match = soup.title.text
#match = soup.div
#match = soup.find('div', class_='footer')

#for article in soup.find_all('div', class_='article'):
#	headline = article.h2.a.text
#	print(headline)

#	summary = article.p.text
#	print(summary)
#	print()

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')
#print(soup.prettify())

article = soup.find('article')
#print(article.prettify())

#headline = article.h2.a.text
#print(headline)

#summary = article.find('div', class_='entry-content').p.text
#print(summary)


#-->Extracting Youtube Urls
vid_src = article.find('iframe', class_='youtube-player')['src']
#print(vid_src)

#Broken into a list
#vid_id = vid_src.split('/')
#print(vid_id)

vid_id = vid_src.split('/')[4]
vid_id = vid_id.split('?')[0]
#print(vid_id)

yt_link = f'https://youtube.com/watch?v={vid_id}'
print(yt_link)
