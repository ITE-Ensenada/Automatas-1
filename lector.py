#!/usr/bin/env python
import re
from htmlTags import dicc_html as dictionary
from bs4 import BeautifulSoup
html_file = open("index.html", "r")
index = html_file.read()
soup = BeautifulSoup(index, 'html.parser')

def token_isopen(token):
    for key,value in dictionary.items():
        if value == token:
            if token in [33,0,31]:
                pass
            elif token == 34:
                return 1   
            elif '/' in key:
                return 1
            else:
                return 0

#    if token.startswith("<", 0, 1) and "/" not in token:
 #       print("is open")
  #      return True
  #  elif "/" in token:
   #     print("close tag")
    #    return False
    
tokens = []
tags = re.findall(r'<[^>]+>', document)
#tags = html_doc.find_all(r'<[^>]+>')
for t in tags:
    s = t.split()
    bandera = 1
    for key,value in dictionary.items():
        if key in s[0]:
            print(f"\n{s[0]} \t=> {value}")
            print(token_isopen(key))
            bandera = 0
            tokens.append(value)
            break
    if bandera:
        print(f'\n{s[0]} \t=> -1')
        print("u dumb kid finish the fkn tag")

html_close = [0,31]
print(f"\n{tokens}")






