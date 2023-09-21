# ******************************************************************************************************* #
# OBJETIVO:  Criar um sistema para gerenciar o cálculo de uma tabuada
# Data: 05/09/2023
# Versão: 1.0
# ******************************************************************************************************* #

# IMPORTS

import sys 

sys.path.insert(1,'./modulo')

import tabuada

# ENTRADA DE DADOS

status = False

while not(status):

    numero_tabuada = input('Digite o número da tabuada inicial: ')  
    numero_tabuada_final = input('Digite o número da tabuada final: ')
    contador_inicio = input('Digite o número do contador inicial: ')
    contador_fim = input('Digite o número do contador final: ')

    # PROCESSAMENTO

    status = tabuada.calcular_tabuada(numero_tabuada,numero_tabuada_final,contador_inicio,contador_fim)

