#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

def funcion1():
    variable1 = "variable dentro de una funcion. "
    print(variable1)

    def funcion2():
        variable1 = "He cambiado el valor de la funcion."
        print(variable1)

    funcion2()

funcion1()
#primero se imprime el valor de la funcion uno y despues la 2 porque primero va con la principal y despues con la anidada

variable1 = "variable fuera de la funcion esta variable es global"
def funcion3():
    variable1 = "variable dentro de la funcion"
    print(variable1)

funcion3()

print (variable1)#se imprimen las dos variables  la de dentro de la funcion y la de afuera 


def funcion5():
    global num1#esta creando la variable local en una variable global
    num1 = 10

funcion5()

print(num1)
