pedro = float (input ("Digite o valor que o Pedro apostou:\n"))
joao = float (input ("Digite o valor que o João apostou:\n"))
marcela = float (input ("Digite o valor que a Marcela apostou:\n"))
premio = float (input ("Digite o valor do prêmio:\n"))
parcela = pedro + joao + marcela
pe = (pedro/parcela)*premio
jo= (joao/parcela)*premio
ma= (marcela/parcela)*premio
print ("Prêmio do Pedro:\n", "%.2f"% pe, "Prêmio do João:\n", "%.2f"% jo, "Prêmio da Marcela:\n", "%.2f"% ma) 