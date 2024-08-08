def consumo (dist_percorrida , quant_litros):
    km_l= dist_percorrida / quant_litros
    if km_l < 8:
        return 'Venda o carro!'
    elif km_l >= 8 and km_l <= 12:
        return 'Econômico!'
    else:
        return 'Super econômico!'
    