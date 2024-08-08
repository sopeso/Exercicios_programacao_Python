salario= float(input("Digite o salário do Carlos: "))
poupanca= float( input("Digite o rendimento da poupança(%):"))
fixa= float( input("Digite o rendimento do fundo de renda fixa(%):"))
joao = 1/3 * salario

i = 1
while salario <= joao:
    salario = (salario*poupanca)* i
    joao = (joao *fixa)*i
    i += 1

print("Meses: %d" %(i))

