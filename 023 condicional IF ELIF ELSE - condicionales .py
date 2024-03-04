#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

edad = int(input("¿cual es tu edad? \n"))#con esta linea lo que estamos realizando es guardando la variable que elm usuario escriba en el tablero y la esta guardando en la variable edad

if edad <=0:
    print("nadie puede tener esa edad.")

elif edad >= 1 and edad <=17: #and significa simplemen te "y" y lo que estamos diciendo es que mientras edad sea mayor o igual que 1 y menor o igual que 17 se ejecutara esta condicion
    print("Eres menor de edad. ")

elif edad <= 100:#esta linea solo es para saber si es menor o igual que 100 se ejecutara y mayor que 18 porque se descartaron los menores de 18 en la linea anterior
    print("Eres mayor de edad")

else:
    print("edad no valida")


