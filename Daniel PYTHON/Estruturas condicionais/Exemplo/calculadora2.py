# **************************************************************************************************************************** #
# Objetivo: Realizar o cálculo de 4 operações matemáticas
# Data: 24/08/2023
# Versão 1.0
#***************************************************************************************************************************** #

# Entrada de dados

valor1 = input('Digite o Valor 1: ').replace(',','.')
valor2 = input('Digite o valor 2: ').replace(',','.')
operacao = input('Escolha a operação a ser realizada [SOMAR | SUBTRAIR | MULTIPLICAR | DIVIDIR]: ').upper()
resultado = ''

# Processamento

if not(valor1.isnumeric()) or not(valor2.isnumeric()):
    print('ERROR! EXPLODINDO SEU PC EM 3 SEGUNDOS... ')

else:
    if valor1 == '' or valor2 == '':
        print('ERROR!')
    else:

        valor1 = float(valor1)
        valor2 = float(valor2)


        if operacao == 'SOMAR':
            resultado = valor1 + valor2
        elif operacao == 'SUBTRAIR':
            resultado = valor1 - valor2
        elif operacao == 'MULTIPLICAR':
            resultado = valor1 * valor2
        elif operacao == 'DIVIDIR':

            if valor2 == 0:
                print('Não existe divisão por 0.')
            else:
                resultado = valor1 / valor2
        else:
            print('ERROR, EXPLODINDO SEU PC EM 5 SEGUNDOS...')

        # Saída de dados


        print(resultado)

