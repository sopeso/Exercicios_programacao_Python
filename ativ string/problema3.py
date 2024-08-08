def palindromo (palavra):
    index=0
    while index <len(palavra):
        tamanho = len(palavra)
        metade = int(tamanho / 2)

        for index in range(metade):
            if palavra[index] != palavra[tamanho - index - 1]:
                return False
            index = index + 1
            return True
        
palavra= input(" ")

if palindromo(palavra):
    print('É palíndromo')
else:
    print('Não é palíndromo')

