def soma(N):
    if N==1:
        return 1
    else:
        return N + soma(N - 1)
N = int(input("Digite N:"))
print(soma(N))