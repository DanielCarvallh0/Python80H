# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Realizar a conversão de graus Celcius Faherenheit.
# Data: 14 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #


# Entrada de dados.

celcius = input('Digite o valor em graus Celcius a ser convertido: ')

# Processamento 
celcius = float(celcius.replace(',','.'))
faherenheit = (9* celcius + 160) / 5

# Saída de dados

print('O valor convertido é: ', faherenheit, 'º F')
