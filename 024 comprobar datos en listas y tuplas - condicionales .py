#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

entrada = input("introduce el nombre de un navegador:\n")

navegadores = ["chrome", "firefox", "opera", "safari"]
#print("chrome" in navegadores) #con este in lo que estamos pidiendo es que revise si chome esta dentro de la lista de navegadores

if entrada in navegadores:#este mensaje lo va a enviar si el navegador esta en la lista 
    print ("el navegador que buscas esta en la lista")

else: #enviamos este mensaje si el navegador no esta en la lista 
    print("El navegador no esta en la lista ")
