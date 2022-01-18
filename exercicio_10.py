#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 17:10:40 2021

@author: alef

split(fn, n), que quebra o arquivo fn em partes de n bytes e salva com
nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.

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

def split(file, n_bytes):
    
    statistic = statistic_of_file(file)
    number_arqs = int(statistic[0]/n_bytes)
    
    print('numero de arquivos: ', number_arqs)
    
    f = open(file, 'r')
    
    arq = f.readlines()
    
    print('original')
    print(arq)
    
    lista_nome = file.split('.')
    ini = 0
    fim = int(len(arq)/number_arqs)
    for i in range(number_arqs):
        print(lista_nome[0]+'_00'+str(i+1)+'.'+lista_nome[1])
        
        print(arq[ini:fim])
        ini = fim
        if( i + 2 < number_arqs):
            fim += int(len(arq)/number_arqs)
        else:
            fim = len(arq)

def join(file):
    pass


split('temp.txt', 1.0)