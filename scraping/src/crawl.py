from bs4 import BeautifulSoup
import requests
import csv
#
# source = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').text
# soup = BeautifulSoup(source, 'html.parser')
# print(soup.prettify())

with open('simple_html.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')


for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()

# article = soup.find('div', class_='article')
# print(article)

