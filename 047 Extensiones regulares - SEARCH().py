#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

import re#se puede utilizar para verificar si una cadena de caracteres contiene el patron de busqueda especificado

texto = "Bienvenido a programacion"

busqueda = re.search("Bienvenido",texto)# busca coincidencias ya sea espacios en blanco o letras o palabras pero debe ser especificamente lo que buscas ya sean minusculas o mayusculas

print(busqueda)
