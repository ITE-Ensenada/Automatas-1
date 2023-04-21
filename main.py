#!/usr/bin/env python
import re
from tokens import dicc_html

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

with open("index.html", 'r', encoding='utf-8-sig') as f:
    html_doc = f.read()
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
