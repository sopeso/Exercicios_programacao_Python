maiorlinha = ''
arquivo = open('texto.txt')

for linha in arquivo:
    for palavra in linha.split():
        if len(maiorpalavra) < len(palavra):
            maiorpalavra = palavra

arquivo.close()
print(maiorpalavra)
print(len(maiorpalavra))