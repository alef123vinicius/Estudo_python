#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 11:40:56 2021

@author: alef
"""

import sys
import subprocess

# ping
param = '-c'
# no windows
if sys.platform == 'win32':
    cmd = '-n'
    
# local para testar
host = '127.0.0.1'

# Comunicaão com outro processo
# um pipe com stdout do comando
command = ['ping', param, '1', host]

# utilizando o call que chama o Popen
# forma generica de execução de processos
py = subprocess.call(command)
print(py)

# Executando o Popen diretamente e ativa o retorno completo do ping
# permite comunicação com o processo do s.o.
print(subprocess.Popen(command, stdout=subprocess.PIPE).stdout.read())
