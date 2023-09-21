# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Realizar a conversão de real para dólar.
# Data: 17 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #


# Entrada de dados.

valor_cotacao = input('Insira aqui o valor do dólar atualmente: ').replace(',','.')

quantidade_convertida = input('Insira aqui o valor a ser convertido: ').replace(',','.')

# Processamento.

conversao =  float(quantidade_convertida) / float(valor_cotacao)

# Saída de dados.

print('Após converter seu dinheiro você ficou com: ', conversao,'USD, Dólares')