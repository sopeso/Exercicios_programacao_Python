# -*- coding: utf-8 -*-
"""ProjetoFinal2020_SophiaAraujo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HAn6PQG4FLU6SwOLthovHI5WViXbYyzE

### Introdução à Programação de Computadores - 2020/2

# **Projeto Prático Final**


Professores:

*   Jefersson Alex dos Santos - jefersson@dcc.ufmg.br
*   João Guilherme Maia de Menezes - jgmm@dcc.ufmg.br

------------------

# Introdução
---------------
Neste projeto realizaremos a manipulação de um grande arquivo de dados reais.
Trata-se de dados e estatísticas sobre economia mineral no Brasil gerados pelo Departamento Nacional de Produção Mineral, vinculado ao Ministério de Minas e Energia. Os dados utilizados estão disponíveis em [www.dnpm.gov.br](http://www.dnpm.gov.br/dnpm/publicacoes/serie-estatisticas-e-economia-mineral/estatisticas-e-economia-mineral "Estatísticas e Economia Mineral")

Mais especificamente, analisamos os dados referentes ao recolhimento do CFEM (Compensação Financeira pela Exploração de Recursos Minerais), acessíveis publicamente [aqui](https://app.dnpm.gov.br/DadosAbertos/ARRECADACAO/Cfem.csv).
O CFEM é um imposto pago pelas empresas ou pessoas físicas a União, aos Estados, Distrito Federal e Município pela utilização econômica dos recursos minerais.




Tarefa 0 - Leitura dos dados
---------

**Essa está pronta! :-)**

Na célula abaixo baixamos e implementamos uma função para leitura do arquivo CSV. A função retorna uma lista com os registros dos dados e uma outra lista que corresponde aos rótulos (nome das colunas). Essa função será utilizada nas próximas tarefas.
Depois, a função implementada <code>le_dados</code> é testada imprimindo os rótulos, a primeira linha dos dados e o número total de registros. Também criamos um dicionário <code>reg</code> pra facilitar o acesso aos registros.
"""

# Baixando os dados do site oficial (link alternativo abaixo)
!wget https://app.dnpm.gov.br/DadosAbertos/ARRECADACAO/Cfem.csv

# Funcao que le os dados de um arquivo CSV e retorna a lista de rótulos (nome das colunas) e os dados.
# Estamos levando em consideracao que todos os dados do arquivo cabem na memória do computador.
def le_dados(filename):
    # Abrindo o arquivo.
    # Utilizamos o parametro 'encoding' para indicar que o arquivo possui uma codificacao especifica.
    # Isso garante que os acentos e caracteres especiais sejam lidos adequadamente.
    file = open(filename, 'r', encoding='ISO-8859-1')

    # Criando uma lista vazia para armazenar todos os dados do arquivo
    dados = []

    # Para cada linha do arquivo, realizamos as seguintes operacoes:
    # (1) removemos o caractere '\n' do final da linha
    # (2) substituimos as ',' por ';' para evitar problemas com a separacao da parte decimal de valores.
    # (3) removemos as aspas extras
    # (4) transformamos a linha em uma lista
    # (5) adicionamos a lista de itens na lista 'dados'
    for line in file:
        dados.append(line.rstrip().replace('","','";"').replace('"','').split(';'))

    # Separando a primeira linha do arquivo para uma lista separada de 'rotulos'
    rotulos = dados.pop(0)

    return rotulos, dados

############# BLOCO PRINCIPAL DO PROGRAMA #############
rotulos, dados = le_dados("Cfem.csv")

print (rotulos, '\n')
print (dados[0])
print ("Número total de registros: %d" % (len(dados)))

# Criando dicionario pra facilitar acesso aos registros
index = 0
reg = {}
for d in rotulos:
  reg[d] = index
  index=index+1

print(reg)

"""Tarefa 1 - Evolução da arrecadação ao longo dos anos
---------

**Agora é com você!**

Implemente funções para gerar um gráfico de arrecadação do CFEM no Estado de Minas Gerais ao longo dos anos (2003 a 2021 em milhões de reais).


"""

# Implemente seu código aqui!

#questão 1
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def arrecadacaoporano(dados):
    arrecadar = dict() #criando um dicionário
    for parte in dados:
        if parte[9] == 'MG':
            arrecadar[parte[0]] = float(parte[13].replace(',','.')) +arrecadar.get(parte[0], 0.0 )

    conj = [] #criando lista
    for data, valor in arrecadar.items():
        conj.append((data,valor))
    conj.sort()
    return conj

def plotea_serie(conj):
    parte1 = []
    parte2 = []
    for parte in conj:
        parte1.append(parte[0])
        parte2.append(parte[1]/(10**6))
    parte2.pop(0)
    parte1.pop(0)


    plt.plot(parte1,parte2) #plotando gráfico
    #argumentos gráfico
    plt.ylabel('Arrecadação (em milhões de reais) em MG')
    plt.grid(True)
    plt.xticks(rotation=60)
    plt.show()


plotea_serie(arrecadacaoporano(dados))

"""Tarefa 2 - Extração de bauxita por estado entre 2015 e 2020
---------

Implemente um código capaz de plotar um gráfico de barras que mostra a extração de bauxita por estado brasileiro entre os anos de 2015 e 2020.
"""

# Implemente seu código aqui!

#pergunta2

import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def extracaominerio_p_estado(dados, minerio, inicio, fim):
    producao_por_estado = dict() #criando um dicionario
    if fim < inicio:
        return None

    for parte in dados:
        ano = int(parte[0]) #pegando o ano nos dados
        if ano >= inicio and ano <= fim:
            if minerio == parte[8] and parte[12] != '':
                producao_por_estado[parte[9]] =  float(parte[12].replace(',','.'))+ producao_por_estado.get(parte[9], 0.0 )
                unidade = parte[11]

    return producao_por_estado, unidade


def plot_extracao_minerio_estado(dados, minerio, inicio, fim):
    producao_por_estado, un = extracaominerio_p_estado(dados, minerio, inicio, fim)

    est = list()
    quant = list()

    for parte1, parte2 in sorted(producao_por_estado.items(), reverse=True, key=itemgetter(1)):
        est.append(parte1)
        quant.append(float(parte2)/(10**6))
    xx = np.arange(len(quant))
    plt.bar(xx, quant, width=0.65, color='b')
    plt.title('Extração de ' + minerio + ' por estado entre ' + str(inicio) + ' e ' +  str(fim))
    plt.ylabel('(em milhões de ' + un + ')')
    plt.xticks(xx, est)
    plt.show()

plot_extracao_minerio_estado(dados, "BAUXITA", 2015, 2020)

"""Tarefa 3 - Extração de ouro por estado nos últimos dez anos.
---------

Implemente códigos para gerar um gráfico de barras que mostra a extração de ouro (**'OURO'**) por estado nos últimos dez anos completos (de 2010 até 2020) na célula abaixo.
Sugestão: utilize funções implementadas nas tarefas anteriores.
"""

# Faça seu código da Tarefa 3 aqui


##pergunta 3

import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def extracaominerio_p_estado(dados, minerio, inicio, fim):
    producao_estado = dict() #criando dicionário

    if fim < inicio:
        return None

    for parte in dados:
        data = int(parte[0])
        if data <= fim and data >= inicio:
            if minerio == parte[8] and parte[12] != '':
                producao_estado[parte[9]] = float(parte[12].replace(',','.'))+ producao_estado.get(parte[9], 0.0 )
                unid = parte[11]

    return producao_estado, unid


def plota_extracaominerio_p_estado(dados, minerio, inicio, fim):
    producao_estado, xx = extracaominerio_p_estado(dados, minerio, inicio, fim)

    estados = list()
    quants = list()
    for parte1, parte2 in sorted(producao_estado.items(), key=itemgetter(1),reverse=True):
        estados.append(parte1)
        quants.append(float(parte2)/(10**6))
    ttt = np.arange(len(quants))
    plt.bar(ttt, quants, width=0.65, color='b')
    plt.title('Extração de ' + minerio + ' por estado entre ' + str(inicio) + ' e ' +  str(fim))
    plt.ylabel('(em milhões de ' + xx + ')')
    plt.xticks(ttt, estados)
    plt.show()

plota_extracaominerio_p_estado(dados, "OURO", 2010, 2020)

"""Tarefa 4 - Evolução da extração de FERRO em Minas Gerais e Pará.
---------

Implemente códigos para plotar um gráfico que mostra a evolução da extração de ferro (**'FERRO'**) nos estados de Minas Gerais e Pará (de 1991 até 2019). Sugestão: copie e altere as funções implementadas na Tarefa 1. Utilize as funções que você implementou para plotar o gráfico final.
"""

# Faça seu código da Tarefa 4 aqui
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

#pergunta 4

def extracao_por_ano_pa(dados):
    extracao = dict()
    for parte in dados:
        if parte[9] == "PA" and parte[8] == "FERRO" and parte[12] != '':
            extracao[parte[0]] = extracao.get(parte[0], 0.0 ) + float(parte[12].replace(',','.'))

    lista2 = list()
    for data, quant in extracao.items():
        if data >= '1991' and data <= '2021':
            lista2.append((data,quant))
    lista2.sort()
    return lista2


def extracao_anual_mg(dados):

    extracao = dict()

    for parte in dados:
        if parte[9] == "MG" and parte[8] == "FERRO" and parte[12] != '':
            extracao[parte[0]] = extracao.get(parte[0], 0.0 ) + float(parte[12].replace(',','.'))

    lista1 = list()
    for data, quant in extracao.items():
        if data >= '1991' and data <= '2021':
            lista1.append((data,quant))
    lista1.sort()
    return lista1

def plot_serie(lista1, lista2):
   l1= list()
   z1 = list()
   l2= list()
   z2 = list()
   for parte in lista1:
     l1.append(parte[0])
     z1.append(parte[1]/(10**6))
   for parte in lista2:
     l2.append(parte[0])
     z2.append(parte[1]/(10**6))

#parte gráfica
   plt.plot(l1,z1, label = 'MG', color="r")
   plt.plot(l2,z2, label = 'PA', color="b")
   plt.ylabel('Extração (em milhões de kg) por ano')
   plt.legend()
   plt.grid(True)
   plt.xticks(rotation=60)
   plt.title("Evolução da extração de FERRO nos estados de MG e PA")
   plt.show()


plot_serie(extracao_anual_mg(dados), extracao_por_ano_pa(dados))

"""Tarefa 5 - Percentual de arrecadação dos Estados da Região Sul no ano de 2019 por tipo de minério extraído.
---------

Implemente um código para plotar um gráfico de "pizza" que mostra o percentual de arrecadação de cada tipo de minério extraído pelos estados da Região Sul no ano de 2019. Utilize o mesmo código para plotar o mesmo gráfico para o Estado de Minas Gerais.

Sugestão 1: use os exemplos da documentação do matplotlib para fazer o gráfico: [Basic Pie Chart!](http://matplotlib.org/gallery/pie_and_polar_charts/pie_features.html#sphx-glr-gallery-pie-and-polar-charts-pie-features-py")

Sugestão 2: por questão de visualização, mostre apenas os  minérios mais frequentes e agrupe os menos frequentes em uma categoria "Outros". Seja criativo, as regras para agrupamento ficam a seu critério. =)

"""

# Faça seu código da Tarefa 5 aqui
import numpy as np
import matplotlib.pyplot as plt
from operator import itemgetter

def arrecadacaoanual_sul(dados):

    arrecadacao = dict()

    for parte in dados:
        if parte[9] in ['PR', 'SC', 'RS'] and parte[0] == "2019" :
            arrecadacao[parte[8]] = arrecadacao.get(parte[8], 0.0 ) + float(parte[13].replace(',','.'))

    lista = list()
    for r, s in arrecadacao.items():
        lista.append((r, s))
    lista.sort()
    return lista


def plotserie_sul(lista):

    x = list()
    y =list()

    for parte in sorted(lista,reverse=True,key= itemgetter(1)):
        x.append(parte[0])
        y.append(parte[1]/(10**6))

    outros = list()
    dicionario = dict()
    cont = 0
    while cont != len(x)-1:
        if y[cont] >=1.1:
          dicionario[x[cont]] = dicionario.get(x[cont], 0.0) + y[cont]
          cont = cont+ 1
        if y[cont] < 1.1:
          outros.append(y[cont])
          cont = cont + 1
        if cont == len(x)-1:
          soma = sum(outros)
          dicionario["OUTROS"] = soma
          break

    labels = dicionario.keys()
    sizes = dicionario.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Percentual de Arrecadação por Tipo de Minério na Região Sul 2019")

    plt.show()

def arrecadacaoanual_mg(dados):

    arrecadacao = dict()

    for parte in dados:
        if parte[9] == 'MG' and parte[0] == "2019":
            arrecadacao[parte[8]] = arrecadacao.get(parte[8], 0.0 ) + float(parte[13].replace(',','.'))

    lista = []
    for r, s in arrecadacao.items():
        lista.append((r, s))
    lista.sort()
    return lista


def plotserie_mg(lista):

    x = []
    y = []

    for parte in sorted(lista,reverse=True,key= itemgetter(1)):
        x.append(parte[0])
        y.append(parte[1]/(10**6))

    outros = []
    dicionario = dict()
    cont = 0
    while cont != len(x)-1:
        if y[cont] >= 100:
            dicionario[x[cont]] = dicionario.get(x[cont], 0.0) + y[cont]
            cont = cont+ 1
        if y[cont] < 100:
            outros.append(y[cont])
            cont = cont + 1
        if cont == len(x)-1:
            soma = sum(outros)
            dicionario["OUTROS"] = soma
            break

    labels = dicionario.keys()
    sizes = dicionario.values()
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Percentual de Arrecadação por Tipo de Minério em Minas Gerais EM 2019")

    plt.show()

plotserie_sul(arrecadacaoanual_sul(dados))
plotserie_mg(arrecadacaoanual_mg(dados))