#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

for x in range (5,25,2):#por defecto esta duncion lo hace desde el 0 y se pude poner desde que rango quieres  y desde cuantos savanzas como por ejemplo saltos de 2 en 2
    print(x)

print("Lista de numeros:\n")

numeros = [2,4,6,8,16,32,64,128]#lista de numeros

for x in range (len(numeros)):#contiene el range  y aparte la funcion len 
    print("Número de operaciones -> ", x, "Multiplicacion ->", numeros [x], "Resultado: ->", numeros [x] * numeros [x])#lo que esta hacieno es sacar la potencia
    
for x in range (10):
    print(x)
else:
    print("se acabo el for")

num1 =["1","2","3","4","5"]
num2 = "0"

for x in num1:
    for y in num2:
        print (x + y)
#este lo que hace es unir los dos for o mas, puedes agregar los for que requieras 
