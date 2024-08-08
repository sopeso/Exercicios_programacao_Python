salario= float(input("Digite o valor do salário:"))

novosalario = 0.0
if salario <= 280:
    novosalario = salario + salario * 0.20
    
elif salario > 280 and salario <= 700:
    novosalario = salario + salario * 0.15


elif salario > 700 and salario <= 1500:
    novosalario= salario + salario * 0.10

else:
   novosalario = salario + salario * 0.05

reajuste= novosalario - salario
print('Valor do aumento: %.2f' % reajuste)
print('Novo salário: %.2f' % novosalario)