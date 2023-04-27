#!/usr/bin/env python
import re
from tokens import dicc_html

#0 -> abre
#1 -> cierra
#2 -> neutron
#3 - > desconocido

def token_isopen(token):
    """recibe un token y te devuelve true si es una etiqueta abierta"""
    for key,value in dicc_html.items():
        if value == token:
            if token in [0,20]:
                return 2
            if token == 34:
                return 1
            if '/' in key:
                return 1
        else:
            return 0
        return value
with open("index.html", "r", encoding='utf-8-sig') as f:
    html_doc = f.read()
tokens = []
tags = re.findall(r'<[^>]+>',html_doc)
for t in tags:
    s = t.split()
    BANDERA = 1
    for key,value in dicc_html.items():
        if key in s[0]:
            print(f"{s[0]} \t\t=>  {value}")
            BANDERA = 0
            tokens.append(value)
            break
    if BANDERA:
        print(f"{s[0]} \t\t=> -1")

html_close = [0,31]
print(tokens)
