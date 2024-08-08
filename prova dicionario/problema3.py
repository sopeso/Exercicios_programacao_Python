arquivo = open('tempos.txt')

nomes = []
tempos = []
for i in arquivo:
    i = i.split(" ")
    for j in i:
        j = j.replace("\n", "")
        inteiro=int(j)
        if j.isnumeric() == True:
            tempos.append(inteiro)
        else: 
            nomes.append(j)
#tamanho
x = 0
y = 5
#medias
medias = []
while True:
    media = sum(nomes[x:y])/5
    medias.append(media)
    x = y
    if y >= len(tempos):
        break
    y += 5
    
dicionario = {}
for i in range(0, len(means)):
    dicionario[nomes[i]] = means[i]
meansord = []
for item in sorted(dic, key = dic.get):
    meansord.append(dic[item])
    namesord = []
    for i in meansord:
        for k, v in dic.items():
            if i == v:
                namesord.append(k) 

count1 = nums.index(min(nums))
if count1 < 3:
     print("Melhor volta: %s-%i segundos" % (names[0], nums[coun1t]))
if count1 >= 3 and count1 < 6:
    print("Melhor volta: %s-%i segundos" % (names[1], nums[count1]))
if count1 >= 6 and count1 < 9:
    print("Melhor volta: %s-%i segundos" % (names[2], nums[count1]))
if count1 >= 9:
    print("Melhor volta: %s-%i segundos" % (names[4], nums[count1]))

print("Classificação final: ")

count2 = 1
for i in range(0, len(meansord)):
    print("%i-%s-%.2f" % (count2, namesord[i], meansord[i]))
    count2 +=1

arquivo.close()
