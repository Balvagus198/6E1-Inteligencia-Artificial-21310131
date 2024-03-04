#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

colores =["rojo", "azul", "verde", "amarillo"]#el metodo append solo agrega elementos al final de la lista

colores.sort(reverse=True)#en esta linea el sort lo que hace es ordenar la lista alfabeticamente y el reverse=true lo que hace es que la lista la pone alrevez, estos cambios son permanentes 

print(sorted(colores))#en dado caso que no requieras que los cambios sean permanentes puedes utilizar el metodo sorted que los pone alfabeticamente sin que los cambios sean peramnentes 
