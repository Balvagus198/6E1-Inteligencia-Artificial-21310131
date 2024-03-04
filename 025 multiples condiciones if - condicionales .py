#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

print("saludos guerrero, ¿Que deseas comprar?\n\n" +
      "Items disponibles\n\n" +
      "Espadas:\n\n" +
      "1 Espadas Nivel 1: 150 Monedas de oro.\n" +
      "2 Espadas Nivel 2: 1200 Monedas de oro. \n\n" +
      "Escudos: \n\n" +
      "3 Escudo Nivel 1: 100 Monedas de oro. \n" +
      "4 Escudo Nivel 2: 750 Monedas de oro. \n")
#en el print lo que estamos haciendo es que el usuario mire que articulos estan disponibles

comprar = [3]#realizamos una lista vacia

dinero = 1500 

EspadaLV1 = 150

EspadaLV2 = 1200

EscudoLV1 = 100

EscudoLV2 = 750

#le dimos los valores en el programa a cada objeto 

if 0 in comprar or comprar == []:#si el jugador introduce un 0 se cumplira esta condicion y ademas se puede cumplir si la lista esta vacia
    print("Especifique un numero entre 1 y 4. ")

if 1 in comprar:
    dinero = dinero - EspadaLV1

if 2 in comprar:
    dinero = dinero - EspadaLV2

if 3 in comprar:
    dinero = dinero - EscudoLV1

if 4 in comprar:
    dinero = dinero - EscudoLV2

else:
    print("Especifica un numero entre 1 y 4 ")

#los if anteriores lo que estan realizando es disminuyendo el dinero del usuario al momento de comprar algo

if dinero < 0:# esta imprimiendo cuando el usuario no cuenta con suficiente dinero 
    print("No tienes el suficiente dinero")

if comprar == [1] or comprar == [2] or comprar == [3] or comprar == [4]:
    print("Te quedan " + str(dinero)+ " Monedas de oro")#aqui lo que estamos haciendo es imprimir cuantas monedas de oro le quedan despues de ya haber gastado en comprar algo y el str lo que esta haciendo es cambiando el numero por string
    print("Se añadio el/los objeto/s a tu inventario")

