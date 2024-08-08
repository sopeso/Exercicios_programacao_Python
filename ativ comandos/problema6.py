
numero = int(input('Digite um inteiro n: '))
x = 1
y = 1
for i in range(2, numero):
    z = x + y
    x = y
    y = z

print(y)