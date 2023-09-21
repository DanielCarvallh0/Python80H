# ******************************************************************************************************* #
# OBJETIVO:  Calcular o Fatorial de um número fornecido pelo usuário
# Data: 04/09/2023
# Versão: 1.0
# ******************************************************************************************************* #


# ENTRADA DE DADOS

fatorial = int(input('Número a ser fatorado: '))
numero = 1
calculo = 1


while  numero <= fatorial:
    calculo = calculo * numero

    print(calculo)

    numero += 1



