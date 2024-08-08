
rna = input('Digite o RNA: ')


dict = {"UUU": "Phe", "CUU": "Leu", "UUA": "Leu","AAG":"Lisina","UCU":"Ser","UAU":"Tyr","CAA":"Gln" }

codon_list = []
for i in range(0, len(rna), 3):
    codon_list.append(rna[i] + rna[i+1] + rna[i+2])
    
result = []
for x in codon_list:
    translation = dict.get(x)

    result.append(translation)
lista_em_texto = '-'.join(map(str, result))
print("Cadeia de Aminoácidos:",lista_em_texto)
