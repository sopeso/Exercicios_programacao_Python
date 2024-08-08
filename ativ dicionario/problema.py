alunonotas={}
while True:
    nome= input()
    nome= nome.strip()
    if not nome:
        break
    nota1=float(input())
    nota2=float(input())
    
    if nome in alunonotas:
        alunonotas[nome].extend([nota1,nota2])
    else:
        alunonotas[nome]=[nota1,nota2]
alunomedia={}
for nome, notas in alunonotas.items():
    alunomedia[nome] = sum(notas)/len(notas)
    
notas=[]
for aluno, meia in alunomedia.items():
    notas.append((media,aluno))
notas,sort(reverse= True)

for media, aluno in notas:
    print(f"{aluno} - {media:.02f}')