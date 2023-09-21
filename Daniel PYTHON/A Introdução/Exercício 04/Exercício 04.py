# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Efetuar o cálculo da quantidade de combustível que gasta em uma viagem.
# Data: 15 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #

# Entrada de dados.

tempo_gasto = input('Qual foi a duração da viagem\nEm minutos por favor: ')

velocidade_media_percorrida = input('Qual foi a velocidade média que vocês usaram no trajeto: ')


# Processamento.

tempo_gasto = float(tempo_gasto) / 60

velocidade_media_percorrida = float(velocidade_media_percorrida.replace(',','.'))

distancia = tempo_gasto * velocidade_media_percorrida
litros_usados = distancia / 12

# Saída de dados.
print('A velocidade média foi de: 'f'{velocidade_media_percorrida:.0f}'' KM/H\nO tempo que vocês gastaram foi de: 'f'{tempo_gasto:.0f}'' H\nE a distância percorrida foi de: 'f'{distancia:.0f}'' KM\nA quantidade de litros usados foi de: 'f'{litros_usados:.0f}'' Litros\n')

