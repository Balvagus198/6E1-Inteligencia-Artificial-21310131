#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

class Naves():#con la clase se crea el tronco de la clase la cual pode os dividir en subclases 
    peso = 2500
    largo = 50
    ancho = 20
    color1 = "Negro"
    color2 = "Plateado"
    motores = 4
    activada = False
    compuerta_principal = False
    sistema_defensa = True
    autodestruccion = False

    def encender(self):
        self.activada = True

    def apagar(self):
        self.activada = False

    def abrir_compuerta(self):
        self.compuerta_principal = True

    def cerrar_compuerta(self):
        self.compuerta_principal = False

    def desactivar_defensas(self):
        self.sistema_defensa = False

    def activar_defensas(self):
        self.sistema_defensa = True

    def activar_autodestrucion(self):
        self.autodestruccion = True
        mensaje = "Protocolo de autodestrucci�n activado..."
        print(mensaje)

    def estado_motores(self):
        if (self.activada):
            return "Motores trabajando al 100%."
        else:
            return "Motores apagados."

    def estado_compuerta(self):
        if (self.compuerta_principal):
            return "La compuerta est� abierta."
        else:
            return "La compuerta est� cerrada."

    def estado_defensa(self):#self hace referencia a cualquier objeto de la clase naves
        if (self.sistema_defensa):            
            return "El sistema de defensa est� activado."
        else:
            return "�Peligro! El sistema de defensa est� desactivado."
    
#Se crea el objeto nave1 perteneciente a la clase Naves.
    
nave1=Naves()

#Comandos (llamadas) al objeto.

#Enciende nave.
nave1.encender()

#Comprueba estado de los motores.
print(nave1.estado_motores())

#Apaga nave.
nave1.apagar()

#Comprueba estado de los motores.

print(nave1.estado_motores())

#Abre la compuerta.
nave1.abrir_compuerta()

#Comprueba el estado de la compuerta.
print(nave1.estado_compuerta())

#Cierra compuerta.
nave1.cerrar_compuerta()

#Comprueba el estado de la compuerta.
print(nave1.estado_compuerta())

#Comprueba el estado de la defensas.
print(nave1.estado_defensa())

#Desactiva las defensas.
nave1.desactivar_defensas()

#Comprueba el estado de la defensas.
print(nave1.estado_defensa())

#Ejecuta la autodestrucci�n de la nave.
nave1.activar_autodestrucion()
