# -*- coding: utf-8 -*-

def imprime_naturais_impares(n):
    if n == 1:
        print(n)
    elif n % 2 == 0:
        imprime_naturais_impares(n - 1)		
    else:
        print(n)
        imprime_naturais_impares(n - 2)

n = int(input())
imprime_naturais_impares(n)
