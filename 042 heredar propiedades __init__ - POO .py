#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

class nombreclase():#asi creamos una clase vacia (con el pass)
    pass

class usuarios:

    def __init__(self, nombre, edad):#en vez del self agregamos la palabra usuario 
        self.nombre = nombre
        self.edad = edad

    def muestra_datos(datos):#en vez del self agregamos la palabra datos para sustiruirlo
        print("El nombre de usuario es: " + datos.nombre, "y tiene", datos.edad)

usuario1 = usuarios("julian", 56)#agregando datos a la clase usuario

usuario1.muestra_datos()


class usuarios_premium(usuarios):#asi estamos creando una clase secundaria (clase hijo) que es a base de la clase padre usuarios
    def __init__(self, nombre, edad, instagram):#sirve para dar un estado inicial al objeto y usa los objetos de la clase derivada, olvido el init de la clase padre 
        usuarios.__init__(self, nombre, edad)#con nuestro init de esta linea agregamos lo de la clase padre que tambien utilizaremos en esta clase
        #self.nombre = nombre
        #self.edad = edad
        self.instagram = instagram
#cada tipo de usuario tiene sus propias propiedades
    def muestra_datos_premium(self):
       print("El nombre del usuario es: " + self.nombre, "y tiene", self.edad, "años. su instagram es: ", self.instagram)

usuario2 = usuarios_premium("Elvira", 23, "elvira_23")

usuario2.muestra_datos_premium()
