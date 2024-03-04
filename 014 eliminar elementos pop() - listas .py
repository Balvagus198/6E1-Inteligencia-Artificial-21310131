#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

colores =["rojo", "azul", "verde", "amarillo"]

guardalista = colores.pop(0)#al aplicarle el metodo pop a eliminado el color rojo
print(colores)#este print solo saca los colores quitando el rojo ya que esta eliminado 

print("El color eliminado de la lista es el: " + guardalista)#con pop se consigue eliminar un elemento y guardarlo en una variable 
