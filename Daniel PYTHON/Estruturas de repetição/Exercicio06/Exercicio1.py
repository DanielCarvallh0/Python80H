# ******************************************************************************************************* #
# OBJETIVO:   Criar um sistema que gerencie números pares e impares
# Data: 11/09/2023
# Versão: 1.1
# ******************************************************************************************************* #


# ENTRADA DE DADOS

numero_inicial = input('Digite o número inicial: ')
numero_final = input('Digite o número final: ')

if numero_inicial == '' or numero_final == '':
    print('ERROR ! Preencha os campos ou não conseguirá efetuar o cálculo!')

else:
    numero_inicial = int(numero_inicial)
    numero_final = int(numero_final)

    if numero_inicial  < 0 or numero_inicial > 500 or numero_final < 100 or numero_final > 1000:
        print('ERROR ! Respeite o limite para o exercício...')

    elif numero_inicial > numero_final:
        print('ERROR ! o número inicial deve ser menor que o número final...')

    elif numero_inicial == numero_final:
        print('ERROR ! Os números não podem ser iguais...')

    else:
        contagem_pares = 0
        contagem_impares = 0
        num = numero_inicial
        nume = numero_inicial
        
        print('Lista de números pares: ')
        while num <= numero_final:
            if num % 2 == 0:
                print (num)
                contagem_pares += 1
            num +=1
        print('Números pares encontrados',contagem_pares)

        
        print('Lista de números ímpares: ')
        while nume <= numero_final:
            if nume % 2 == 1:
                print(nume)
                contagem_impares += 1
            nume += 1
        print('Números impares encontrados',contagem_impares)