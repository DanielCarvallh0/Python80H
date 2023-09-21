# **************************************************************************************************************************** #

# Objetivo: Ler um valor numérico inteiro
# Data: 28/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados

valor = int(input('Digite o valor: '))


# Saída de dados


if valor < 1 or valor > 9:
    print('O valor está fora da faixa permitida')
else:
    print('O valor está na faixa permitida')

