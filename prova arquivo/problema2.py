n= int(input("Digite um inteiro:"))
arquivo = open('texto.txt')
for linha in arquivo:
    for palavra in linha.split():
            if len(palavra) <= n:
                print(palavra)

arquivo.close()