#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

teclado1 = {#Estamos creando un diccionario que la gran ventaja en cambio a las lstas es que en estas se le puede dar un titulo del area a la que esta dirigida por ejemblo marca,modelo, precio en el mismo y nombrandolos tal cual te da el resultado 
    "categoria" : "Teclados",
    "Modelo": "HyperX Alloy FPS Pro",
    "Precio": "89.99"
    }

teclado2 = {
    "categoria" : "Teclados",
    "Modelo": "corsair K55 RGB",
    "Precio": "59.99"
    }

consulta1 = teclado1["Modelo"]#con este estamos llamando al diccionario 1(teclado1) y que nos diga especificamente el modelo de este

print(consulta1)

consulta2 = teclado1["Modelo"], teclado1["Precio"], teclado2["Modelo"], teclado2["Precio"]#en este lo que estamos haciendo es llamando a los modelo y precios de los 2 diccionarios que tenemos 

print(consulta2)

muestrateclado = dict(teclado1)#con el metodo dict vamos a mostrar todo lo que este en el diccionario asignado 

print(muestrateclado)
