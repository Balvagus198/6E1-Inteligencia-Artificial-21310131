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
    "Precio": "59.99",
    "id" : "001"
    }


print(len(teclado1)+len(teclado2))# este metodo solo nos sirve para saber la longitud de nuestro diccionario

teclado1.pop("categoria")#con este borramos el elemento categoria completo del diccionario
print(teclado1)

del teclado1["Precio"]#con este borramos precio completo del diccionario 
print(teclado1)


teclado1.clear()#elimina el diccionario
print(teclado1)

teclado1["color"] = "negro"#asi agregamos una categoria y una descripcion
print(teclado1)

tecladocopia = teclado2.copy()#estamos copiando todo el teclado 2 y tambien se puede hacer con el metodo dict
print(tecladocopia)

teclado3 = dict(categoria = "teclados",#el metodo dict tambien sirve para crear diccionarios nuevos 
                modelo = "Razer Cynosa Chroma",
                Precio = "59.99")
print(teclado3)

teclado4 = ("categoria", "Modelo", "Precio")
vacia = "Valor vacio"

teclado4 = dict.fromkeys(teclado4,vacia)# agregamos un string en cada uno de los elementos 
print(teclado4)

vistateclado = teclado2.keys()#nos muestra nomas la categoria 

print(vistateclado)

if "id" teclado2: #busca una categoria especifica
    print("eñ producto tiene un id identificado")
else
    print("El teclado non tiene un id")



    

