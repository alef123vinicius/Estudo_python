#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:11:39 2021

@author: alef
"""

import os
import sys
import platform

def uid():
    """
    uid() -> retorna a identificação do usuário
    corrente ou None se não for possível identificar
    """
    
    # Variáveis de ambiente para cada
    # Sistema operacional
    us = {'Windows': 'USERNAME',
          'Linux': 'USER'}
    
    u = us.get(platform.system())
    return os.environ.get(u)

print('Usuário: ', uid())
print('Plataforma: ', platform.platform())
print('Diretório corrente: ', os.path.abspath(os.curdir))
exep, exef = os.path.split(sys.executable)
print('Executável: ', exef)
print('Diretório do executável: ', exep)