#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

class usuarios:

    def __init__(usuario, nombre, edad):#en vez del self agregamos la palabra usuario para sustituirlo
        usuario.nombre = nombre
        usuario.edad = edad

    def muestra_datos(datos):#en vez del self agregamos la palabra datos para sustiruirlo
        print("El nombre de usuario es: " + datos.nombre, datos.edad)

usuario1 = usuarios("julian", 56)#agregando datos a la clase usuario
usuario1.muestra_datos()

usuario1.edad = 65#cambiando el valor de la edad del usuario 1
usuario1.muestra_datos()
