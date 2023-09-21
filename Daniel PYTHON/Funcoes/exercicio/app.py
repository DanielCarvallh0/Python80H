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

# from math import sqrt
# sys.path.insert(1,'./modulo')
# import calculo_delta


import modulo.calculo_delta as r2

# ENTRADA DE DADOS

valor_a = float(input('Digite o valor a: '))

valor_b = float(input('Digite o valor b: '))

valor_c = float(input('Digite o valor c: '))

raiz_mais , raiz_menos = r2.calculo_x1_e_x2(valor_a, valor_b, valor_c)

print('O resultado da equação foi de:',raiz_mais,'e',raiz_menos)