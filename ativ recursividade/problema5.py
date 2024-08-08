def imprime_naturais(N):
    if N==0:
        print(N)
    else:
        imprime_naturais(N - 1)
        print(N)

n = int(input("Digite N: "))
imprime_naturais(N)