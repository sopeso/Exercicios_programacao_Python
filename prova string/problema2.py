def exercicio2():
    palavra1 = str(input("Digite a primeira palavra: "))
    palavra2 = str(input("Digite a segunda palavra: "))

    maiorTamanhoDePalavra = len(palavra1)

    if len(palavra2) > len(palavra1):
        maiorTamanhoDePalavra = len(palavra2)

    count = 0
    resultado = []
    while count < maiorTamanhoDePalavra:
        if len(palavra1) > count:
            resultado.append(palavra1[count])

        if len(palavra2) > count:
            resultado.append(palavra2[count])

        count = count + 1

    return ''.join(resultado)

resultado = exercicio2()

print("Combinação:",resultado)