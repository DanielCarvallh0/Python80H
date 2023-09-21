# ******************************************************************************************************* #
# OBJETIVO:  Calcular o Fatorial de um número fornecido pelo usuário
# Data: 11/09/2023
# Versão: 2.0
# ******************************************************************************************************* #

import sys 

sys.path.insert(1, './modulo')

import fatorial
# ENTRADA DE DADOS

fatorial1 = int(input('Número a ser fatorado: '))

resultado = fatorial.calcularFatorial(fatorial1)

print(fatorial1, '=', resultado)

