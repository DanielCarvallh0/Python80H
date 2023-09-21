# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Efetuar o cálculo do valor de uma prestação em atraso.
# Data: 15 - 08 - 2023
# Versão: 1.0
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #


# Entrada de dados.
a = int(input('Digite o valor: '))
b = int(input('Digite o valor: '))
c = int(input('Digite o valor: '))
d = int(input('Digite o valor: '))

# Processamento.

calculo_adicao = a + b
calculo_adicao1 = a + c
calculo_adicao2 = a + d
calculo_adicao3 = b + c
calculo_adicao4 = b + d
calculo_adicao5 = c + d

calculo_multiplicacao = a * b
calculo_multiplicacao1 = a * c
calculo_multiplicacao2 = a * d
calculo_multiplicacao3 = b * c
calculo_multiplicacao4 = b * d
calculo_multiplicacao5 = c * d

# Saída de dados.

print ('O resultado dos calculos foram de\nAdicção:\nCálculo A + B =' , calculo_adicao , '\nCálculo A + C = ' , calculo_adicao1 , '\nCálculo A + D = ' ,
         calculo_adicao2 , '\nCálculo B + C = ' , calculo_adicao3 , '\nCálculo B + D = ' , calculo_adicao4 , '\nCálculo C + D = ' , calculo_adicao5)

print ('O resultado dos calculos foram de\nMultiplicação:\nCálculo A x B =' , calculo_multiplicacao , '\nCálculo A x C = ' , calculo_multiplicacao1 , '\nCálculo A x D = ' ,
        calculo_multiplicacao2 , '\nCálculo B x C = ' , calculo_multiplicacao3 , '\nCálculo B x D = ' , calculo_multiplicacao4 , '\nCálculo C x D = ' , calculo_multiplicacao5)
