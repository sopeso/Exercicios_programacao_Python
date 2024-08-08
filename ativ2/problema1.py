numero = int(input("Digite o primeiro inteiro:\n"))
numero2 = int(input("Digite o segundo inteiro:\n"))
numero3 = int(input("Digite o terceiro inteiro:\n"))
numero4 = int(input("Digite o quarto inteiro:\n"))
numero5 = int(input("Digite o quinto inteiro:\n"))

print("Maior:",max(numero,numero2,numero3,numero4,numero5))
print("Menor:",min(numero,numero2,numero3,numero4,numero5))

#Soma dos valores divisiveis por 3

numero = numero % 3
numero2 = numero2 % 3
numero3 = numero3 % 3
numero4 = numero4 % 3
numero5 = numero5 % 3

x=0

if numero == 0:
    x= x+1
    
if numero2 == 0:
    x= x+1    

if numero3 == 0:
    x= x+1
    
if numero4 == 0:
    x= x+1
    
if numero5 == 0:
    x= x+1

print("Quantidade de divisíveis por 3: ", x)

