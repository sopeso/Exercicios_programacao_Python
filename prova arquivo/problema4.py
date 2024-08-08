arquivo = open('frases.txt','r')
numero_palidromos= 0
for linha in arquivo:
    linha= linha.lower().replace(' ','').replace('\n','')
    invertida= linha[::-1]
    if linha == invertida:
        numero_palidromos= numero_palidromos+1
    
print("Quantidade de palíndromos:", numero_palidromos)