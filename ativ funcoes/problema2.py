def pagamento(hora, quantidade):
	salario = hora * quantidade
	if salario <= 900: 
		return salario
	elif salario > 900 and salario <= 1500:
		desconto = salario * 0.05
		return salario - desconto
	elif salario > 1500 and salario <= 2500:
		desconto = salario * 0.1
		return salario - desconto
	else:
		desconto = salario * 0.2
		return salario - desconto

    
