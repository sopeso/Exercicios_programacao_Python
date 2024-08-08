# -*- coding: utf-8 -*-
def soma(m,n):
    if m==n:
        return m
    if m>n:
        return -1
    return m + soma(m + 1, n)
m = int(input("Digite m"))
n = int(input("Digite n"))
print(soma(m, n))