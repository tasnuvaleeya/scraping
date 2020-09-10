from bs4 import BeautifulSoup
import requests
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
# print(soup.prettify())

soup = BeautifulSoup('<b class="boldest checked" id="hi hello">Extremely bold</b>', 'html.parser')
tag = soup.b
# print(type(tag))
# tag.name = "blockquote"
# print(tag['class'])
# print(soup)
# print(tag.attrs)
# tag['id'] = 'very-bold'
# tag['another-attr'] = 1
#
# del tag['id']
# print(tag)

rel_soup = BeautifulSoup('<p id=\'my id\' class=\'class1 class2\'>Back to the <a rel="index">homepage</a></p>', 'html.parser')
# rel_soup.a['rel'] = ['contents', 'index']
# no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html', multi_valued_attributes=None)
print(rel_soup.p.get_attribute_list('id'))
print(rel_soup.p.get_attribute_list('class'))
