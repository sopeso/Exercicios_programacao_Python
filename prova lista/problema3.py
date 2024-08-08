
n= int(input("Digite a dimensão:"))


a= []
b= []


for i in range(n):
    l_lista = int(input())
    a.append(l_lista)

for i in range(n):
    l_lista = int(input())
    b.append(l_lista)


soma= 0
for i in range(n):
    soma= soma + (a[i]*b[i]) 

print("Produto Escalar:", soma)
    
