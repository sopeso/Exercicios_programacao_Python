# -*- coding: utf-8 -*-

def mdc(x, y):
    if x < y: # para ficar sempre o menor numero
        x,y==y,x
    if y==0:
        return x
    return mdc(y,x%y)


x = int(input("Digite x:"))
y = int(input("Digite y:"))
print(mdc(x, y))

