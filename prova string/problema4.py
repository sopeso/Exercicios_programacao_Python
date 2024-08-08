def exercicio4():
    palavra = input('Digite uma palavra: ')
    chave = int(input('Digite o valor da chave: '))

    resultado = []
    count = 0
    while count < len(palavra):
        if ord(palavra[count]) + chave <= ord('z'):
            resultado.append(chr(ord(palavra[count]) + chave))
        else:
            diferenca = ord(palavra[count]) + chave - ord('z')-1
            resultado.append(chr(ord('a') + diferenca))
        
        count = count + 1
    return ''.join(resultado)


resultado = exercicio4()

print("Resultado: " + resultado)