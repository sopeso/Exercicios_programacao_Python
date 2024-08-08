def calcula_valor (preco, quantidade, tipo_combustivel):
	if tipo_combustivel == 'a':
		if quantidade <= 20:
			preco_litro_desconto = preco - (preco* 0.03)			
		else:
			preco_litro_desconto = preco - (preco * 0.05)
		total = preco_litro_desconto * quantidade
		return total			
	else:
		if quantidade <= 20:
			preco_litro_desconto = preco - (preco * 0.04)			
		else:
			preco_litro_desconto = preco - (preco * 0.06)
		total = preco_litro_desconto * quantidade
		return total