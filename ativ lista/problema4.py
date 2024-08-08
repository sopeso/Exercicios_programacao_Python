temperaturas= []
for i in range(12):
    temp= int(input())
    temperatura.append(temp)
media = sum(temperaturas) / 12
print('Média: %.2f' % media)
