#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

x=0

while x < 10:# lo que tiene el ciclo while es que se ejecutara tantas veces como sea cierto lo escrito 
#        break  =este sirve para tronar el while sin necesidad de que falle la condicion
    x += 1# agrega 1 cada que se ejecuta el bucle
    if x == 5 or x == 7:
        continue #lo que hace es ssaltar a los que tu mandas con el if 
    print(x)

else:
    print ("Saliendo del while")
