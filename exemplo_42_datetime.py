#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:22:28 2021

@author: alef
"""

import datetime

# datetime() recebe como parâmetros:
# ano, mês, dia, hora, minuto, segundo
# e retorna um objeto do tipo datetime
dt = datetime.datetime(2021,12,31,23,59,59)

# Objeto date e time podem ser criados
# a partir de um objeto datetime
data = dt.date()
hora = dt.time()

# quanto tempo falta para 31/12/2020
dd = dt - dt.today()

print('Data:', data)
print('Hora:', hora)
print('Quanto tempo falta para 31/12/2021:',
      str(dd).replace('days', 'dias'))