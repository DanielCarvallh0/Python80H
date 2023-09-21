# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Cálcula dois números nas quatro operações básicas.
# Data: 17 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #


# Entrada de dados.

a = float(input('Insira o valor de A: ').replace(',','.'))

b = float(input('Insira o valor de B: ').replace(',','.'))

# Processamento.

calculo_adicao = a + b
calculo_subtracao = a - b
calculo_multiplicacao = a * b
calculo_divisao = a / b

# Saída de dados.

print('\nAdição: ', calculo_adicao,'\nSubtração: ', calculo_subtracao,'\nMultiplicação: ', calculo_multiplicacao,'\nDivisão: ', calculo_divisao)



