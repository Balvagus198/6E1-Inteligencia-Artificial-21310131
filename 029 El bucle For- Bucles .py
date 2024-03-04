#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

cursos = ["Python", "Java", "COBOL", "HTML"]

for x in cursos:#ejecutara todo lo que contenga dentro de la oracion o lista 
    if x == "COBOL":
        continue#se salta cobol y tambien se puede utilizar break para cerrar el bucle 
    print (x)
