#Primer Programa

from ast import parse
from datetime import date
print('Today´s date is: ' + str(date.today()) )

#Convertidor de unidades
parsec = 11
lightyears = 0
#1 parsec es 3.26156 años luz
lightyears = parsec * 3.26156
print(str(parsec) + " parsec, is " + str(lightyears) + " lightyears")
