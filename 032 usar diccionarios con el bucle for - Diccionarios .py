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


consulta2 = teclado1.get("Modelo"), teclado1["Precio"], teclado2["Modelo"], teclado2["Precio"]#en este lo que estamos haciendo es llamando a los modelo y precios de los 2 diccionarios que tenemos 
#tambien con el metodo get podemos llamar lo escrito en el diccionario 
print(consulta2)


print(teclado1)#asi de facil tambien podemos imprimir todo el diccionario completo

teclado1["Precio"] = "85"#estamos cambiando el precion del teclado desde otra linea 

print(teclado1.get("Precio"))

for x in teclado2:
    print(teclado2[x])# estamos imprimiendo el diccionario desde un for

    
for x in teclado2.values():#otra forma mas sencilla de imprimir el diccionario desde un for 
    print(x)

for x, y in teclado2.items():# de esta manera te lo imprime mejor ya que te da el modelo y el nombre, te da el objeto y su significado
    print(x,": ",y)
