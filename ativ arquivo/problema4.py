arquivo = open ('datas.txt',"r")#função do python para abrir arquivos
datas= []
for linha in arquivo: #ler uma linha por vez
    dia, mes, ano = linha.split("/") #separar linha em tres componente (dia, mes e ano), de acordo com a /
    dia= int(dia) #converter tudo para inteiro para ficar mais fácil de comparar depois
    mes= int (mes)
    ano= int (ano)
    data= [ano,mes,dia] #colocou data como uma lista de 3 elementos, ano primeiro ppis para achar data mais recente seria sópegar a data com maior ano-> depois maior mês-> depois maior dia
    datas.append(data)
data_maisrecente= max(datas)
ano, mes, dia= data_maisrecente
print(f"{dia:02d}/{mes:02d}/{ano}")
    