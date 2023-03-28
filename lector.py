#!/usr/bin/env python
from bs4 import BeautifulSoup
import re

dicc_html = {
    "!<DOCTYPE>": 0,
    "html" : 10,
    "/html": 11,
    "head" : 12,
    "/head": 13,
    "body" : 14,
    "/body":15,
    "title": 16,
    "/title":17,
    "p": 30,
    "br":31 ,
    "hr":32,
    "<!--":33,
    "-->":34,
    "div":35,
    "h1":20,
    "h2":21,
    "h3":22,
    "h4":23,
    "h5":24,
    "h6":25,
}

html_doc = """<html><head></head>
<body>
<p class="title"><b>The Dormouse's story</b>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p>
<a>
<p class="story">...</p>
"""

"""
1-> [html,10],head,/head
2-> body
3-> p,b,/b
4-> p

"""
def busca_token(etiqueta):
    pass

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup)
print(soup.prettify())
print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.title.parent.name)
#if soup.title.string:
#    print("Si tiene contenido el titulo")
#else:
#    print("No tiene titulo salte de aqui")
count = 1
for tag in soup.find_all():
    print(f"{count}-> {tag.name}")
    count = count + 1

tags = re.findall(r'<[^>]+>',html_doc)
for t in tags:
    print(t)







    