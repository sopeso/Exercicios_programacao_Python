# -*- coding: utf-8 -*-
endereco= input()
endereco_blocos= endereco.split('.')
validade= "Valido"

for bloco in endereco_blocos:
    bloco =int(bloco)
    if bloco < 0 or bloco> 255:
        validade= "Inválido"
    break
print(validade)
    
