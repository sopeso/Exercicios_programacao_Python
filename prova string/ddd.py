def exercicio2():
    palavra1 = str(input("escreva a palavra1: "))
    palavra2 = str(input("escreva a palavra2: "))

    maiorTamanhoDePalavra = len(palavra1)

    if len(palavra2) > len(palavra1):
        maiorTamanhoDePalavra = len(palavra2)

    count = 0
    resultado = ""
    while count < maiorTamanhoDePalavra:
        if len(palavra1) < count:
            resultado = resultado + palavra1[count]
            print(palavra1[count])

        if len(palavra2) < count:
            print(palavra2[count])
            resultado = resultado + palavra2[count]
        

        count = count +1
        return(resultado)

    
resultado = exercicio2()
print(resultado)