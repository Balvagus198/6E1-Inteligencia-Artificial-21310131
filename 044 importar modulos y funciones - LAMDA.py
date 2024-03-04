#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

#las funciones lamda se conoce tambien como funciones anonimas

import math#importamos math para las funciones matematicas

def area(radio):
    resultado = round(math.pi * radio * radio, 2)# la ventaja de utilizar el math es que no tenemos que declarar toda la numeracion de pi 
    print (resultado)

area(2)

area = lambda radio:round(math.pi * radio * radio, 2)#simplicar funciones cortas que solamente ocupen una linea

print(area(2))
