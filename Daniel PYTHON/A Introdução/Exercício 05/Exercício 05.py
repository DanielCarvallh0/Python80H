# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Efetuar o cálculo do valor de uma prestação em atraso
# Data: 15 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #


# Entrada de dados.

valor = input('Qual seria o valor da prestação: ')
taxa = input('Qual seria a taxa: ')
tempo = int(input('E o tempo era qual mesmo, em dias por favor: '))

# Processamento.

valor = float(valor.replace(',','.'))
taxa = float(taxa.replace(',','.'))
prestacao = valor + (valor * (taxa / 100) * tempo)

# Saída de dados.

print('Após o cálculo a prestação ficou: ',f'{prestacao:.2f}')
