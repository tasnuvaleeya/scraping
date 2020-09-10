from requests_html import HTML, HTMLSession
import csv
csv_file = open('cms_scraper.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video'])

session = HTMLSession()
r = session.get("https://coreyms.com/page/14")

articles = r.html.find('article')
for article in articles:

    headline = article.find('.entry-title-link', first=True).text
    print(headline)
    summary = article.find('.entry-content p', first=True).text
    print(summary)

    try:
        video_src = article.find('iframe', first=True).attrs['src']
        # print(video_src)
        video_id = video_src.split('/')[4]

        video_id = video_id.split('?')[0]
        # print(video_id)
        youtube_link = f'https://www.youtube.com/watch?v={video_id}'
    except Exception as e:
        youtube_link = None
    print(youtube_link)
    print()
    csv_writer.writerow([headline, summary, youtube_link])
csv_file.close()
