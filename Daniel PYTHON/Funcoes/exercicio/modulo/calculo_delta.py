# ******************************************************************************************************* #
# OBJETIVO:  Calcular as duas raizes da equação de 2° grau
# Data: 14/09/2023
# Versão: 1.0
# ******************************************************************************************************* #


# AX² + BX + C = 0

# 1. CALCULAR O DELTA
# DELTA = B² - 4AC

# 2. CALCULAR X1 E X2
# X = (- B + OU - RAIZ(DELTA)) / (2 * A)

# 3. REGRAS
# A = NÃO PODE SER 0. SE O USUÁRIO DIGITAR 0 O VALOR TEM QUE SE TORNAR 1.
# DELTA = NÃO PODE SER NEGATIVO SE FOR EXIBA UMA MENSAGEM. "NÃO HÁ RAIZES NEGATIVAS"... TERMINE O PROGRAMA.




# IMPORTS

from math import sqrt
import sys


def calculo_delta(variavel_a, variavel_b, variavel_c):
    a = variavel_a
    b = variavel_b
    c = variavel_c

    if a == 0:
        a = 1

    delta = (b * b) - (4 * a * c)  

    if delta < 0: 
        print('NÃO HÁ RAIZES NEGATIVAS!')
        sys.exit()

    return delta

# print(calculo_delta(2,3,-5))

def calculo_x1_e_x2(variavel_a, variavel_b, variavel_c):
    a = variavel_a
    b = variavel_b
    c = variavel_c

    if a == 0:
        a = 1
        
    x_mais = (- b + sqrt(calculo_delta(a,b,c))) / (2 * a)

    x_menos = (- b - sqrt(calculo_delta(a,b,c))) / (2 * a)

    return x_mais, x_menos


if __name__ == "__main__":
    a = 2
    b = 3
    c = -5
    print(calculo_x1_e_x2(a,b,c))




