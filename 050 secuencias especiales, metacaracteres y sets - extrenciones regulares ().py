#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

import re#se puede utilizar para verificar si una cadena de caracteres contiene el patron de busqueda especificado

texto = " 12551 Bienvenido a programacion Bienvenida"

busqueda = re.findall("\D", texto)#ignora los numeros

print(busqueda)

busqueda = re.findall("programa..on", texto)# busca la palabra con las semejanzas

print(busqueda)

busqueda = re.findall("Bienvenido|Bienvenida", texto)# busca las 2 palabras

print(busqueda)


