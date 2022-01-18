#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:50:46 2021

@author: alef

Instropecção ou reflexão é a capacidade do software de identificar 
e relatar suas próprias estruturas internas, tais como tipos, 
escopo de variáveis, métodos e atributos.


                 Função         Retorno
              type(objeto)  O tipo (classe) do objeto
                id(objeto)  O identificador do objeto
                  locals()  O dicionário de variáveis locais
                 globals()  O dicionário de variáveis globais
              vars(objeto)  O dicionário de símbolos do objeto
               len(objeto)  O tamanho do objeto
               dir(objeto)  A lista de estruturas do objeto
              help(objeto)  As Doc Strings do objeto
              repr(objeto)  A representação do objeto
isinstance(objeto, classe)  Verdadeiro se objeto deriva da classe
issubclass(subclasse, classe) Verdadeiro se subclasse herda classe
"""

from types import ModuleType

def info(n_obj):
    # cria uma referência ao objeto
    obj = globals()[n_obj]
    
    # Mostra informações sobre o objeto
    print('Nome do objeto: ', n_obj)
    print('Identificador: ', id(obj))
    print('Tipo: ', type(obj))
    print('Representação: ', repr(obj))
    
    # se for um modulo
    if isinstance(obj, ModuleType):
        print('Itens: ')
        for item in dir(obj):
            print(item)
        print()

# mostrando as informações
for n_obj in dir():
    info(n_obj)



s = ''
if isinstance(s, str):
    print('s é uma string')