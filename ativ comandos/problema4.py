# -*- coding: utf-8 -*-

preco = float(input('Digite o preço do pão: '))

for i in range (0,51) :
    total= i * preco
    print('%d - R$ %.2f' % (i, total))