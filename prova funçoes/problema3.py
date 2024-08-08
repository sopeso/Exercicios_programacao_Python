# -- coding: utf-8 --
def estacionamento(hora_entrada, minuto_entrada, hora_saida, minuto_saida):
  hora_saida_em_min = hora_saida * 60
  hora_saida_minuto_final = hora_saida_em_min + minuto_saida
  
  hora_ent_em_min = hora_entrada * 60
  hora_ent_minuto_final = hora_ent_em_min + minuto_entrada

  tempo_estac = hora_saida_minuto_final - hora_ent_minuto_final
  #print(tempo_estac)

  if tempo_estac > 0:
    tempo_estac
  else:
    tempo_estac = tempo_estac + 24*60

  if tempo_estac % 60 !=0:
    horas_a_pagar = int(tempo_estac/60) + 1
   
  else:
    horas_a_pagar = int(tempo_estac/60)
   # return horas_a_pagar 
  
  if horas_a_pagar <= 2:
    valor_a_pagar = horas_a_pagar
    return valor_a_pagar
  elif 2 < horas_a_pagar <=4:
      valor_a_pagar = horas_a_pagar * 1.40
      return valor_a_pagar
  else:
    valor_a_pagar = horas_a_pagar * 2
    return valor_a_pagar