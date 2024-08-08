velocidademax= int(input("Digite o valor da velocidade máxima:\n"))
registrada = int(input ("Digite o valor da velocidade registrada:\n"))

cinquentaporcento = velocidademax + (velocidademax * 0.50)
vinteporcento = velocidademax + (velocidademax * 0.20)

if registrada >= cinquentaporcento :
    print ('Infração Gravíssima')
elif registrada > vinteporcento :
    print ( 'Infração Grave' )
elif registrada <= velocidademax :
    print ( 'Sem Infração' )
else:
    print ( 'Infração Média' )