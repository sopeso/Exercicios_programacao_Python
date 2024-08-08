n = int(input('Digite um inteiro n:'))
n_divisores = 2
for i in range(2, n):
    if n % i == 0:
        n_divisores = n_divisores + 1

if n_divisores == 2 and n >= 2:
    print('É primo')
else:
    print('Não é primo')
