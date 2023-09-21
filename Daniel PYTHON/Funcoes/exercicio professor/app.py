'''
Auto: Tux
Objetivo: Calcular as duas raízes da eq. do 2º grau
          chamando o arquivo equação_segundo_grau.py
Data: 14/09/2023 
Versão: 1.0
'''

import modulo.equacao_segundo_grau as r2
import os

os.system('cls')

inputs = [int(i) for i in input('Digite 3 números: ').split(',')]

x1, x2 = r2.calcular_raizes(inputs[0], inputs[1], inputs[2])
print("O valor de x1 = ", x1)
print("O valor de x2 = ", x2)












.+