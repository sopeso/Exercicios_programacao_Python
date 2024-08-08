inicial = input( "Digite o valor do investimento inicial:\n")
inicial = float (inicial)
juros = input ("Digite a taxa de juros anual:\n")
juros = float (juros)
tempo = input( "Digite o período do investimento em anos: \n")
tempo = int (tempo)
vf= inicial * (1 + (juros * 0.01)) ** tempo
print( "Valor futuro:","%.2f"% vf)