v= []

for i in range(10):
    numero = int(input())
    v.append(numero)

m= (sum (v)/ 10)
n= 10
soma=0
l=[]

for t in range(0,10) :
    calculo= (v [t] - m)**2
    l.append(calculo)

soma= sum( l)

d =((1/(n-1))* soma)** 0.5
print("Desvio Padrão:", format(d, '.2f'))

