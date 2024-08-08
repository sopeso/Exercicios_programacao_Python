# -*- coding: utf-8 -*-

print('Média: %.2f' % media)

distancias= []
for x in range(5):
    distancias = float(input())
    distancias.append(distancias)

distancias.remove(min(distancias))
distancias.remove(max(distancias))
media = mean(distancias)
print('Média: %.2f' % media)