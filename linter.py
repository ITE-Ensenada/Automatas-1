#!/usr/bin/env python
import re
import tokens
dicc_html = {
    "!<DOCTYPE>": 0,
    "<html" : 10,
    "</html": 11,
    "<head" : 12,
    "</head": 13,
    "<body" : 14,
    "</body": 15,
    "<title": 16,
    "</title":17,
    "<p": 30,
    "<br":31 ,
    "<hr":32,
    "<!--":33,
    "-->":34,
    "<div":35,
    "<h1":20,
    "<h2":21,
    "<h3":22,
    "<h4":23,
    "<h5":24,
    "<h6":25,
    "<a":26,
    "</a":27,
}
"""
0 -> abre
1 -> cierra
2 -> neutron
3 - > desconocido
"""
#recibe un token y te devuelve true si es una etiqueta abierta
def token_isopen(token):
    for key,value in dicc_html.items():
        if value == token:
            if token in [0,31]:
                return 2
                pass
            elif token == 34:
                return 1
            elif '/' in key:
                return 1
            else:
                return 0

html_doc = open("index.html",'r') 
tokens = []
tags = re.findall(r'<[^>]+>',html_doc)
for t in tags:
    s = t.split()
    bandera = 1 
    for key,value in dicc_html.items():
        if key in s[0]:
            print(f"{s[0]} \t\t=>  {value}")
            bandera = 0
            tokens.append(value)
            break
    if bandera:
        print(f"{s[0]} \t\t=> -1")

html_close = [0,31]        
print(tokens)

