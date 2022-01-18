#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:01:08 2021

@author: alef

time: implementa funções que permitem utilizar o tempo gerado pelo sistema
datetime: implementa tipos de alto nível para realizar operações de data e
hora
"""

import time

# localtime() Retorna a data e hora local no formato
# de uma estrutura chamada struct_time, que é uma
# coleção com os itens: ano, mês, dia, hora, minuto,
# segundo, dia da semana, dia do ano e horário de verão
print(time.localtime())

# retorna data e hora como string, conforme a conf do sistema operacional
print(time.asctime())

# retorna o tempo do sistema em segundos
ts1 = time.time()

# converte segundos para struct_time
tt1 = time.gmtime(ts1)
print(ts1,'->',tt1)

# somando uma hora
tt2 = time.gmtime(ts1 + 3600.)

# converte struct_time para segundos
ts2 = time.mktime(tt2)
print(tt2,'->',ts2)


# retorna o tempo desde quando o programa
# iniciou, em segundos
print('O programa levou', time.process_time(), 
      'segundos até agora...')

print('O programa levou', time.get_clock_info('process_time').resolution, 
      'segundos até agora...')

# Contando os segundos
for i in range(5):
    # espera durante o número de segundos
    # especificado como parametro
    time.sleep(1)
    print(i+1,'segundos(s)')