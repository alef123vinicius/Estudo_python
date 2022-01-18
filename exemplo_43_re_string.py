#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 12:28:22 2021

@author: alef

Ponto (.): Em modo padrão, significa qualquer caractere, menos o de
nova linha.
▪ Circunflexo (^): Em modo padrão, significa inicio da string.
▪ Cifrão ($): Em modo padrão, significa fim da string.
▪ Contra-barra (\): Caractere de escape, permite usar caracteres especiais
como se fossem comuns.
- Colchetes ([]): Qualquer caractere dos listados entre os colchetes.
- Asterisco (*): Zero ou mais ocorrências da expressão anterior.
- Mais (+): Uma ou mais ocorrências da expressão anterior.
- Interrogação (?): Zero ou uma ocorrência da expressão anterior.
- Chaves ({n}): n ocorrências da expressão anterior.
- Barra vertical (|): “ou” lógico.
- Parenteses (()): Delimitam um grupo de expressões.
- \d: Dígito. Equivale a [0-9].
- \D: Não dígito. Equivale a [^0-9].
- \s: Qualquer caractere de espaçamento ([ \t\n\r\f\v]).
- \S: Qualquer caractere que não seja de espaçamento.([^ \t\n\r\f\v]).
- \w: Caractere alfanumérico ou sublinhado ([a-zA-Z0-9_]).
- \W: Caractere que não seja alfanumérico ou sublinhado ([^a-zA-Z0-
9_]).
"""

import re

# a expressão é compilada e pdoe ser usada mais de uma vez
rex = re.compile('\w+')

bandas = 'Yes, Genesis & Camel'
# encontra as ocorrencias que atendem a expressão
print(bandas, '->', rex.findall(bandas))

# identifica as ocorrencias em suas variações
bjork = re.compile('[Bb]j[öo]rk')
for m in ('Björk', 'björk', 'Biork', 'Bjork', 'bjork'):
    
    # localiza as ocorrencias no inicio da string
    # para localizar em quanlquer parte use search()
    print(m,'->',bool(bjork.match(m)))
    
# substituindo texto
texto = 'A próxima faixa é Stairway to Heaven'
print(texto, '->', re.sub('[Ss]tairway [Tt]o [Hh]eaven', 'The Rover', texto))

# dividindo texto
bandas = 'Tool, Porcupine Tree e NIN'
print(bandas,'->',re.split(',?\s+e?\s+', bandas))