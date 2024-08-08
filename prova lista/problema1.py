
numeros = []
for i in range(10):
    numero = int(input())
    numeros.append(numero)
    
a= numeros[0:5]
b= numeros[5:10]

new_list = []
for element in a:
    if element in b:
        new_list.append(element)
        
print("Interseção:",new_list)
    
#nota 0.8