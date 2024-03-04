#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

x = 100
y = 200
z = 300
if x < y:
    print("x es menor que y. \n")# aqui el print mostraba error ya que anteriormente no contaba con la tabulavcion y al momento de agregarla esta ya funciona

print ("Se esta ejecutando el if\n\n") if x > y else print("se ejecuta el else\n\n")#con esta linea estamos poniendo un if y un else en la misma linea esto para ahorrar codigo

if x < y or z > y:# con el or se debe cumplir por lo menos una de las 2 condiciones y con el and se deben cumplir las 2
    print("Se cumple el if de las dos condiciones \n\n")

else:# en dado caso que no se cumplan las condiciones acordadas aparecera el siguiente mensaje
    print("no se ejecuta el if de las dos condicciones\n\n")

if x < y:# el if se ejecutara solamente si tiene una accion de por medio en este caso se utiliza el pass para no poner un print
    pass
