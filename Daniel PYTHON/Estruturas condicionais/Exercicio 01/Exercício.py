# **************************************************************************************************************************** #

# Objetivo: Ler dois valores numéricos inteiro e apresentar o resultado da diferença do maior valor pelo menor valor. 
# Data: 28/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados

numero1 = int(input('Digite o valor númerico: '))

numero2 = int(input('Digite o valor númerico: '))

# Processamento / Saída de dados

if numero1 > numero2:
    calculo = numero1 - numero2
    print('A diferença é de ', calculo)

else:
    calculo = numero2 - numero1
    print('A diferença é de ', calculo)




