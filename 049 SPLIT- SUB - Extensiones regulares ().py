#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

import re#se puede utilizar para verificar si una cadena de caracteres contiene el patron de busqueda especificado

texto = "Bienvenido a programacion"

busqueda = re.sub(" ", "-", texto, 4)#agrega lo que necesites sustituir con el metodo count limitamos las coincidencias

print(busqueda)

busqueda = re.split("i",texto, 1)#divide la cadena de carecteres en un patron y borra de los resultados esto hace que solo te excluya 1

print(busqueda)
