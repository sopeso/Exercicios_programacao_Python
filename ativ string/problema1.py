# -*- coding: utf-8 -*-

digite_o_nome = input("")
separando = digite_o_nome.rfind(' ')
formatado = digite_o_nome[separando + 1: ] + ', ' + digite_o_nome[ : separando]
print("Nome formatado:", formatado)
