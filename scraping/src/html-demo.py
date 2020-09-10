from requests_html import HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
# print(html.html)
articles = html.find('div.article')# 'div' is a css selector

for article in articles:
    # match = html.find('a', first=True)  # 'a' is a css selector
    headline = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
# print(article.text)
    print(headline)
    print(summary)
    print()
# print(html.text)