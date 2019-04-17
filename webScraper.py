#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text
soup = BeautifulSoup(source, 'lxml')

#setup for storing the data locally
csv_file = open('cms_webScraper.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline','summary','video_link'])


#loop through web site content
for article in soup.find_all('article'):
	headline = article.h2.a.text
	print(headline)

	summary = article.find('div', class_='entry-content').p.text
	print(summary)

	#in case of exceptions
	try:
		vid_src = article.find('iframe', class_='youtube-player')['src']

		vid_id = vid_src.split('/')[4]
		vid_id = vid_id.split('?')[0]

		yt_link = f'https://youtube.com/watch?v={vid_id}'

	except Exception as e:
		#"pass" will ignore layout exceptions
		yt_link = None

	print(yt_link)
	print()

	csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
