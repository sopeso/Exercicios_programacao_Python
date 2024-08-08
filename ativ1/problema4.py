numero=input("Digite um valor com 4 dígitos:\n")
numero=int(numero)

unidade=numero%10
uidade=int(unidade)

dezena=(numero%100)/10
dezena=int(dezena)

centena=(numero%1000)/100
centena=int(centena)

milhar=numero/1000
milhar=int(milhar)

invertido=1000 * unidade+ 100 * dezena + 10 * centena+milhar

print("Valor invertido:",invertido)