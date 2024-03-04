#!/usr/bin/env python
# -*- coding: cp1252 -*-
# -*- coding 850 -*-
# -*- coding: utf-8 -*-
#las palabras de arriba de arriba son por tema de codificacion porque si no no podria escribir acentos

import datetime, locale #importar el modulo datetime para agarrar la fecha exacta y tambien importamos otro modulo

locale.setlocale(locale.LC_ALL, "es-ES")# lo traducimos al español

fecha = datetime.datetime.now()#tomamos la fecha del dia de hoy 

print(fecha.strftime("%D"))
