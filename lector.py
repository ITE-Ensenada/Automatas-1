#!/usr/bin/env python
import re

dicc_html = {
    "!<DOCTYPE>": 0,
     "<html>": 10,
    "</html>": 11,
    "<head>": 12,
    "</head>": 13,
    "<body>": 14,
    "</body>":15,
    "<title>": 16,
    "</title>":17,
    "<p>": 30,
    "</p>": 31,
    "<br>":32 ,
    "<hr>":33,
    "</hr>": 34,
    "<!--":35,
    "-->":36,
    "<div>":37,
    "</div>": 38,
    "<h1>": 40,
    "</h1>": 41,
    "<h2>": 42,
    "</h2>": 43,
    "<h3>": 44,
    "</h3>": 45,
    "<h4>": 46,
    "</h4>": 47,
    "<h5>": 48,
    "</h5>": 49,
    "<h6>": 50,
    "</h6>": 51,
    "<a>": 52,
    "</a>": 53,
    "<b>": 54,
    "</b>": 55,
    }

html_doc = """
<html><head></head>
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

tags = re.findall(r'<[^>]+>', html_doc)
for t in tags:
    s = t.split()
    for key,value in dicc_html.items():
        if key in s[0]:
            print(f"{s[0]} \t=> {value}")
            bandera = 0
            break
    if bandera:
        print(f'{s[0]} \t=> -1')







