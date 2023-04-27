""" algo creo que ocupa mas texto"""

vector = [10,11,43,1,2]
print(vector)
dicc = {
    "nombre":"Guillermo alejandro chavez sanchez",
    "edad":41,
    "grado": "profe",
    "luckynumbers":vector
}
agenda = {

    "datos": dicc
}


print(dicc)

for key,value in dicc.items():
    print(key, ' : ', value)

print(agenda)
