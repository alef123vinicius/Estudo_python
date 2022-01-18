#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 16:29:09 2021

@author: alef

Implementar uma função que leia um arquivo e retorne uma lista de tuplas
com os dados (o separador de campo do arquivo é vírgula), eliminando as
linhas vazias. Caso ocorra algum problema, imprima uma mensagem de
aviso e encerre o programa.
"""


def ler_arquivo(nome_arquivo):
    try:
        arq  = open(nome_arquivo, 'r')
        tuplas = arq.readlines()
        resposta = []
        for t in tuplas:
            if(t != '' and t != '\n'):
                resposta.append((t))
        return resposta
    except IOError:
        print('Erro ao abrir arquivo: ', nome_arquivo)

print(ler_arquivo('arq.txt'))
    
