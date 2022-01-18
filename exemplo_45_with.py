#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:36:38 2021

@author: alef
"""

import random 

# cria um arquivo com 25 números randômicos
with open('temp2.txt', 'w') as temp:
    for y in range(5):
        for x in range(5):
            # grava a saida do comando no arquivo indicado
            print('%.2f' % random.random())
        print()

# exibe o conteúdo do arquivo
with open('temp2.txt') as temp:
    for i in temp:
        print(i)

#print(file=temp)