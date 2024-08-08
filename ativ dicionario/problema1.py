palavra = input('')
letracontador = {}
for letra in palavra:
    letracontador[letra] = letracontador.get(letra, 0) + 1

elementos = []
for letra, contador in letracontador.items():
    letras.append((contador, letra))
    
mais_frequente, letra_mais= max(elementos)
print(letra_mais)