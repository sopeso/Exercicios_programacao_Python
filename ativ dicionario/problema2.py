
palavra = input('')
letra2contador = {}
for letra in palavra:
    if letra in "aeiou":
        letra2contador[letra] = letra2contador.get(letra, 0) + 1

elementos = []
for letra, contador in letra2contador.items():
    elementos.append((contador, letra))
    
mais_frequente, letra_mais= max(elementos)
print(letra_mais)


