#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:35:53 2021

@author: alef
"""

import os.path

# modulo de instropecção amigável
import inspect

print('Objeto: ', inspect.getmodule(os.path))

print('Classe?', inspect.isclass(str))

# Lista todas as funções que existem em os.path

print('Membros: ')

for name, struct in inspect.getmembers(os.path):
    
    if inspect.isfunction(struct):
        print(name)