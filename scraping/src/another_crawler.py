from requests_html import HTMLSession, HTML

with open('simple.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)
    html.render()

match = html.find('#footer', first=True)

print(match.html)

# session = HTMLSession()
# r= session.get('https://coreyms.com/')
#
# for link in r.html.links:
# # for link in r.html.absolute_links:
#     print(link)