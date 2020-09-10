from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('http://coreyms.com').text

soup = BeautifulSoup(source, 'lxml')

with open('cms_scrape.csv', 'w') as csv_file:
# csv_file = open()
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['headline', 'summary', 'video_link'])
    for article in soup.find_all('article'):

        # article = soup.article
        headline = article.h2.a.text
        print(headline)
        summary = article.find(class_='entry-content').p.text
        print(summary)

        try:

            video_src = article.find('iframe', class_='youtube-player')['src']
            video_id = video_src.split('/')[4]
            video_id = video_id.split('?')[0]


            yt_link = f'https://youtube.com/watch?v={video_id}'

        except Exception as e:
            yt_link = None

        print(yt_link)
        print()
        csv_writer.writerow([headline, summary, yt_link])
# csv_file.close()

# print(article.prettify())