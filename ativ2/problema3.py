idade= int(input("Digite a idade:\n"))
tempo= int (input("Digite o tempo de contribuição:\n"))
sexo= str(input ("Digite o sexo (M/F):\n"))

if (sexo == 'M' and idade >= 60 and tempo >= 35) or (sexo == 'F' and idade >= 55 and tempo >= 30):
    print('Pode aposentar')
elif (sexo == 'M' and idade >= 65) or (sexo == 'f' and idade >= 60):
    print('Pode aposentar')
else:
    print('Não pode aposentar')
