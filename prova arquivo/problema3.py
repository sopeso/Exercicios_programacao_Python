arquivo = open('datas.txt')
datas = []
data_atual = [2020,10,5]
for linha in arquivo:
    nome, data = linha.split()
    print("Nome:", nome)
    dia, mes, ano = data.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    datas.append([ano,mes,dia])
    for i in datas:
        idade = data_atual[0] - i[0]
        if i[1] > data_atual[1]:
            idade = idade - 1
        elif i[1] == data_atual[1]:
            if i[2] > data_atual[2]:
                idade = idade - 1
    print("Idade:", idade, "anos")