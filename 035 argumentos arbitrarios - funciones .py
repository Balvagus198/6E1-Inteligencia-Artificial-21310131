#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

def alumnos(*agrs):
    print("el ultimo alumno es " + agrs[3], "y el primero es " + agrs[0] + ".")

alumnos("Andrea", "ana", "andres", "antonio")

def alumnos_profesores(profesor, sustituto, *args):#creamos argumentos que se utilizan en base a una lista y con ayuda de un for se va completando la lista 
    print("profesor: " + profesor)
    print("sustituto: " + sustituto)
    for x in args:
        print("alumno: " + x)
        
lista=["Andrea", "ana", "andres", "antonio"]

alumnos_profesores("antonio", "amador", *lista)

