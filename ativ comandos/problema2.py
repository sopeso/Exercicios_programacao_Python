# -*- coding: utf-8 -*-


numero = int(input('Digite um inteiro: '))
print('Tabuada de %d:' % numero)
for i in [1,2,3,4,5,6,7,8,9,10] :
    print('%d x %d = %d' % (numero, i, numero * i))
