velocidade=input("Digite sua velocidade inicial\n")
velocidade=float(velocidade)
aceleracao= input("Digite sua aceleracao\n")
aceleracao=float(aceleracao)
tempo=input("Digite seu tempo\n")
tempo=float(tempo)
velocidadefinal=velocidade+(aceleracao*tempo)
velocidadefinal=float(velocidadefinal)
distancia=(velocidade*tempo)+((aceleracao*tempo**2)/2)
distancia=float(distancia)
print("Velocidade Final:","%.2f"%velocidadefinal,"Distância Percorrida","%.2f"%distancia)