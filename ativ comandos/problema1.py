# -*- coding: utf-8 -*-
def populacao (num_habitantesA, taxa_crescimentoA, num_habitantesB, taxa_crescimentoB):
    anos = 0
    while num_habitantesA < num_habitantesB:
        num_habitantesA = num_habitantesA + (num_habitantesA * taxa_crescimentoA / 100)
        num_habitantesA = num_habitantesA + (num_habitantesB * taxa_b / 100)
        anos = anos + 1
    return anos

