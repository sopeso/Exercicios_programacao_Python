while True:
    linha = float(input("Digite um número:"))
    if linha <= 0:
        max=max(linha)
        min=min(linha)
        print("Maior:",max)
        print("Menor:", min)
        break
    print(linha)