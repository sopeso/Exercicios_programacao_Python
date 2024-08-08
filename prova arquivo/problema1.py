arquivo = open ('notas.txt',"r")

for linha in arquivo:
    campos= linha.split()
    nome= campos[0]
    notas=[]
    for nota in campos[1:]:
        notas.append(float(nota))
    media= sum(notas)/len(notas)
    media= float(media)
    maior= max(media)
    menor= min(media)
print(maior, end= '')
print(menor, end= '')

#ou
arquivo = open('notas.txt')
maior=0
menor=0
media=[]

for linha in arquivo:
    dados= linha.split()
    nome = dados[0]
    notas = dados[1:]
    soma = 0
    for nota in notas:
        soma = soma + float(nota)
    media.append(soma / 4)

maior= max(media)
menor= min(media)

print("{:.2f}".format(maior))
print("{:.2f}".format(menor))
