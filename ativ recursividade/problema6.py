def imprime_naturais_pares(N):
    if N == 0:
        print(N)
    elif N % 2 == 0:
        imprime_naturais_pares(N - 2)
    print()
    else:
    imprime_naturais_pares(N - 1)

N = int(input("Digite N: "))
imprime_naturais_pares(N)

