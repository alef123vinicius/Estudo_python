#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 15:46:48 2021

@author: alef

Implementar um programa que receba um nome de arquivo e gere
estatísticas sobre o arquivo (número de caracteres, número de linhas e
número de palavras)

"""


def statistic_of_file(file):
    n_linhas = 0
    n_caract = 0
    n_words  = 0
    open_file = open(file)
    for item in open_file:
        # contar numero de palavras
        n_words += len(list(str(item).split(' ')))
        # contar numero de caracteres
        n_caract += len(str(item).replace(' ', '').replace('\n', ''))
        # contar numero de linha
        n_linhas += 1
        
    return n_caract,n_words,n_linhas
    

file = str(input('Insira o arquivo a ser verificado: '))

resp = statistic_of_file(file)
print('Caracteres: ', resp[0])
print('Palavras: ', resp[1])
print('Linhas: ', resp[2])