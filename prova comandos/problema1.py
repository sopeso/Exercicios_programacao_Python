# -*- coding: utf-8 -*-
def soma_divisores (n):
    soma= 0
    for i in range(1, n-1):
        if n % i == 0:
            soma = soma + i
            print ( soma)
print( "Resultado:",soma)