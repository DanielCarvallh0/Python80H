
# *******************************************************************************************************************************************
# Objetivo: Sistema de uma calculadora.
# Versão 1.0 22/08/23
# *******************************************************************************************************************************************


# Entrada de dados


valor1 = input('Digite o número: ').replace(',','.')

valor2 = input('Digite o número: ').replace(',','.')

operacao = input('Qual das operações voce quer usar\n\nSoma\nSubtração\nMultiplicação\nDivisão\nEscolha: ').title()

#processamento

if operacao == 'Soma':
    if valor1 == '' or valor2 == '':
        print('Insira um valor válido para o cálculo, tente novamente')

    else:
        soma = float(valor1) + float(valor2)
        print('O resultado do cálculo foi de:', soma)

if operacao == 'Subtração':
    if valor1 == '' or valor2 == '':
        print('Insira um valor válido para o cálculo, tente novamente')
    else:
        sub = float(valor1) - float(valor2)
        print('O resultado do cálculo foi de:', sub)

if operacao == 'Multiplicação':
    if valor1 == '' or valor2 == '':
        print('Insira um valor válido para o cálculo, tente novamente')
    else:
        mult = float(valor1) * float(valor2)
        print('O resultado do cálculo foi de:', mult)

if valor2 == '0':
    print('Impossivel dividir por 0 tente novamente.')

else:
    if operacao == 'Divisão':
        if valor1 == '' or valor2 == '':
            print('Insira um valor válido para o cálculo, tente novamente')
        else:    
            div = float(valor1) / float(valor2)
            print('O resultado do cálculo foi de:', div)



