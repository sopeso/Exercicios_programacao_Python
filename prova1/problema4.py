numero= int( input("Digite um inteiro de 4 algarismos:\n"))
unidade = int(numero % 10)
dezena = int((numero %100)/10)
centena = int((numero/100) %10)
milhar= int((numero/100)/10)
soma = unidade + dezena + centena + milhar
print ("Resultado:", soma)