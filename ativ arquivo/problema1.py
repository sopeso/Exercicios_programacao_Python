maiorlinha = ''

find = open('texto.txt')

for linha in find:
    if len(maiorlinha) < len(linha):
        maiorlinha = linha

find.close()
print(maiorlinha, end='')
print(len(maiorlinha))