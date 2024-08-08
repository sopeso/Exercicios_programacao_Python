arquivo = open ('notas.txt',"r")

for linha in arquivo:
    campos= linha.split()
    nome= campos[0]
    notas=[]
    for nota in campos[1:]:
        notas.append(float(nota))
    media= sum(notas)/len(notas)
    if media >= 60.0:
        print('Nome: %s - Média: %.2f' % (nome, media))
arquivo.close()