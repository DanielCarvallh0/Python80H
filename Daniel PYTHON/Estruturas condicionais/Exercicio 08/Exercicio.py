# **************************************************************************************************************************** #

# Objetivo: Sistema para calcular o IMC de uma pessoa.
# Data: 29/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados


peso = input('Digite seu peso: ').replace(',','.')

altura = input('Digite sua altura: ').replace(',','.')

peso = float(peso)
altura = float(altura)

# Processamento

imc = peso / (altura * altura)


# Saída de dados

if imc < 16:
    print('Seu imc resultou em :', imc,'\nMagreza Grau III')
    
elif imc <= 16.9:
    print('Seu imc resultou em :', imc,'\nMagreza Grau II')

elif imc < 18.5:
    print('Seu imc resultou em :', imc,'\nMagreza Grau I')

elif imc < 25:
    print('Seu imc resultou em :', imc,'\nAdequado')

elif imc < 30:
    print('Seu imc resultou em :', imc,'\nPré-Obeso')

elif imc < 35:
    print('Seu imc resultou em :', imc,'\nObesidade Grau I')

elif imc < 40:
    print('Seu imc resultou em :', imc,'\nObesidade Grau II')

elif imc >= 40:
    print('Seu imc resultou em :', imc,'\nObesidade Grau III')

