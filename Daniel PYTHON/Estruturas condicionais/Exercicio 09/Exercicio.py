# **************************************************************************************************************************** #

# Objetivo: 
# Data: 29/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados

valor = input('Valor da venda: ').replace(',','.')
codigo = input('Por favor insira o código da venda: ')


# Processamento

valor = float(valor)


if codigo == '1':
    print('Á vista, com 8%,de desconto...')
    desconto = valor - (0.08 * valor)
    print('Com o desconto você vai pagar somente',desconto)

elif codigo == '2':
    print('Á vista no cartão, 4%, de desconto...')
    desconto = valor - (0.04 * valor)
    print('Com o desconto você vai pagar somente',desconto)

elif codigo == '3':
    print('Em 2x, preço normal sem juros')

elif codigo == '4':
    print('Em 4x, preço acrescido de 8%')
    desconto = valor + (0.08 * valor)
    print('Com o essa opção você vai pagar',desconto)

else:
    print('OPÇÃO INVÁLIDA!')


