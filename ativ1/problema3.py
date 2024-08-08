tempo = input("Digite o valor do tempo em segundos:\n")
tempo = int(tempo)
horas = tempo/3600
horas = int(horas)
minutos = (tempo%3600)/60
minutos = int(minutos)
segundos = (tempo%3600)%60
segundos = int(segundos)
print('Valor convertido:', horas, "h" ,minutos,"min",segundos,"s")

