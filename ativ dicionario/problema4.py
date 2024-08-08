dicionario = {}
lista_numeros = int(input())
while lista_numeros != -1:
    dicionario[lista_numeros] = dicionario.get(lista_numeros, 0) + 1
    lista_numeros = int(input())

lista_numeros = []
for S, U in dicionario.items():
    lista_numeros.append((U, S))
lista_numeros.sort(reverse=True)
for CADA in lista_numeros:
    print(CADA[1])
    break