#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

x=1

while x <= 10:# lo que tiene el ciclo while es que se ejecutara tantas veces como sea cierto lo escrito 
    print(x)
    x += 1# agrega 1 cada que se ejecuta el bucle

frase = "lo que escribas lo repito: "
frase += "\nIntroduce el comando'salir' para finalizar el programa.\n"

mensaje = ""

while mensaje != "salir":#Bucle infinito hasta que escribas la palabra salir 
    mensaje = input(frase)
    print(mensaje)

print ("se ha salido del bucle")
