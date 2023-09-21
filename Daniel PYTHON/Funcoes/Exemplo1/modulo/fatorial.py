# ******************************************************************************************************* #
# OBJETIVO:  Arquivo responsável por gerar o cálculo do fatorial
# Data: 11/09/2023
# Versão: 1.0
# ******************************************************************************************************* #

def calcularFatorial (numeroDoFatorial):

    numeroFatorial = numeroDoFatorial

    contador = 1
    fatorial = 1

    while  contador <= numeroFatorial:
        fatorial = fatorial * contador

        contador += 1
        
    return fatorial

