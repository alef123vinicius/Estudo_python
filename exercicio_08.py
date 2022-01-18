#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:28:41 2021

@author: alef


Implementar um módulo com duas funções:
matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas
dimensões.
camel_case(s), que converte nomes para CamelCase.
"""

from my_module import matrix_sum, camel_case

print(matrix_sum(  [[30,20,10,],
                    [40,50,60,]],
                   [[30,20,10,],
                    [40,50,60,]],
                   [[30,20,10,],
                    [40,50,60,]],
                   [[30,20,10,],
                    [40,50,60,]]))

print(camel_case("ola tudo bem pessoas"))