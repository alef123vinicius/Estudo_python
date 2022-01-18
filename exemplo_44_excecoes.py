#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:23:54 2021

@author: alef
"""

import traceback
import sys

try:
    print(1/0)
except ZeroDivisionError:
    print('Erro ao tentar dividir por zero')
    
# Teste receber o nome do arquivo
try:
    fn = input('Nome do arquivo:').strip()
    
    for i,s in enumerate(open(fn)):
        print(i + 1, s)
except:
    # mostre na tela
    trace = traceback.format_exc()
    
    # e salve num arquivo
    print('Aconteceu um erro:\n',trace)
    open('trace.log','a').write(trace)
    
    # encerre
    #sys.exit()