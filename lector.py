""" este programa casi hace algo"""
#!/usr/bin/env python
import re
from htmlTags import dicc_html as dictionary
<<<<<<< HEAD
=======
from bs4 import BeautifulSoup
html_file = open("index.html", 'r')
index = html_file.read()
soup = BeautifulSoup(index, 'html.parser')
>>>>>>> 965aafa8d5473fa803515bf4bfcb0a152b3d60ff

def token_isopen(token):
    """ tokens """
    for key, value in dictionary.items():
        if value == token:
            if token in [33,0,31]:
                pass
            elif token == 34:
                return 1
            elif '/' in key:
                return 1
            else:
                return 0
<<<<<<< HEAD

#    if token.startswith("<", 0, 1) and "/" not in token:
#       print("is open")
#      return True
#  elif "/" in token:
#     print("close tag")
#    return False

with open("index.html", "r", encoding='utf-8-sig') as f:
    html_doc = f.read()

tokens = []
tags = re.findall(r'<[^>]+>', html_doc)
#tags = html_doc.find_all(r'<[^>]+>')
=======
tokens = []
doc = ""
tags = re.findall(r'<[^>]+>', doc)
>>>>>>> 965aafa8d5473fa803515bf4bfcb0a152b3d60ff
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

html_close = [0,31]
print(f"\n{tokens}")
