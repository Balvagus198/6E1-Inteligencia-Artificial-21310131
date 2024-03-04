#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

class nombreclase():#asi creamos una clase vacia (con el pass)
    pass

class usuarios:

    def __init__(usuario, nombre, edad):#en vez del self agregamos la palabra usuario 
        usuario.nombre = nombre
        usuario.edad = edad

    def muestra_datos(datos):#en vez del self agregamos la palabra datos para sustiruirlo
        print("El nombre de usuario es: " + datos.nombre, + "y tiene", datos.edad)

usuario1 = usuarios("julian", 56)#agregando datos a la clase usuario
print(usuario1.nombre, usuario1.edad)

del usuario1.edad
#print(usuario1.nombre, usuario1.edad) el usuario ya no tiene edad porque se elimino

del usuario1
#print(usuario1.nombre, usuario1.edad) aqui se elimina todo el contenido de la clase

