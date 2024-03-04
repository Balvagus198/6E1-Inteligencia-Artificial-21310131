#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

class usuarios():

    def __init__(self, nombre, pin):
        self.nombre=nombre
        self.pin=pin

    def saludo(self):
            print("saludos " + self.nombre + ". iniciaste secion correctamente. ")

    def despedida(self):
            print(self.nombre + ", cerraste la sesion ")

usuario1 = usuarios("Toni", "1234")#debido al init nos pedira obligatoriamente un nombre y un pin

usuario2 = usuarios("Julia", "3692")

usuario1.saludo()
usuario2.saludo()
usuario1.despedida()
