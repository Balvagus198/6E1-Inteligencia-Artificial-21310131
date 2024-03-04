#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

def colores (**kwargs):#nota en los diccionarios los elementos se llaman 'keywords' y sus valores 'values'
    print("Este es el color " + kwargs ["color1"]+ ".")

colores(color1="rojo", color2="azul", color3="verde", color4="amarillo")


def colores(color="rojo"):
    print("mi color favorito es el " + color)

colores("azul")#este lom que esta haciendo es que esta ignorando por completo el rojo que ya tenia predeterminado 
