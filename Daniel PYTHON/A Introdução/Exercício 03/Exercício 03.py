# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Calcular e apresentar o valor do volume de uma lata de óleo.
# Data: 15 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #

# Entrada de dados.

valor_raio = input('Qual seria o valor do raio: ')

valor_altura = input('Qual seria a altura da lata: ')

# Processamento.

valor_raio = float(valor_raio.replace(',','.'))
valor_altura = float(valor_altura.replace(',','.'))


volume = 3.14159 * valor_raio ** 2 * valor_altura

# Saída de dados

print('O volume da lata é', f'{volume:.0f}')
