#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:29:36 2021

@author: alef
"""

def matrix_sum(*matrices):
    matriz_resposta = []
    for l in range(len(matrices[0])):
        new_line = []
        for c in range(len(matrices[l][0])):
            soma_col = 0
            for m in matrices:
                soma_col += m[l][c]
            new_line.append(soma_col)
        matriz_resposta.append(new_line)
    return matriz_resposta    

def camel_case(s):
    list_names = s.split(" ")
    camel_reponse = ""
    for name in list_names:
        camel_reponse += name.capitalize()
        
    return camel_reponse


