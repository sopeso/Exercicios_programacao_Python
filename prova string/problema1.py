


numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
dois = numero1 + numero2
dois = str(dois)


zero = dois.find('0')

if zero >= 0:
    
    n1 = dois[0:a]
    n2 = dois[zero+1:]
    nvn_soma = n1 + n2
    zero = nvn_soma.find('0')
    while zero >= 0:
        n1 = nvn_soma[0:zero]
        n2 = nvn_soma[zero+1:]
        nvn = n1 + n2
        zero = nvn.find('0')
        
    print("Resultado:",nvn)

else: print("Resultado:", dois)