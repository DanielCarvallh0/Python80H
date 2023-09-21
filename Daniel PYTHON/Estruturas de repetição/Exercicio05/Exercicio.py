# ******************************************************************************************************* #
# OBJETIVO:  Criar um sistema para gerenciar o cálculo de uma tabuada
# Data: 05/09/2023
# Versão: 1.0
# ******************************************************************************************************* #


# ENTRADA DE DADOS

tab_inicial = input('Digite a tabuada inicial: ')
tab_final = input('Digite a tabuada final: ')
numero_inicial = input('Digite o número inical da tabuada: ')
numero_final = input('Digite o número final da tabuada: ')
tinicio = 0
ninicio = 0

# PRCESSAMENTO

if tab_inicial == '' or tab_final == '' or numero_final == '' or numero_inicial == '':
    print('ERROR ! Preencha os campos ou não conseguirá efetuar o cálculo!')

else:
    tab_inicial = int(tab_inicial)
    tab_final = int(tab_final)
    numero_inicial = int(numero_inicial)
    numero_final = int(numero_final)

    if tab_inicial  < 2 or tab_inicial > 100 or tab_final < 2 or tab_final > 100:
        print('ERROR ! As tabuadas tem que ser entre 2 e 100. Corrija...')

    elif numero_inicial < 1 or numero_inicial > 50 or numero_final < 1 or numero_final > 50:
        print('ERROR ! Os números tem que ser entre 1 e 50. Corrija...')

    else:
        print('tudo correto!')

    while tab_inicial <= tab_final:
        print('\nTabuada do ', tab_inicial,'\n')
        tinicio = tab_inicial
        ninicio = numero_inicial
        while ninicio <= numero_final:

            resultado = tinicio * ninicio  
            print(tinicio, 'X', ninicio, '=', resultado,'\n')
            
            ninicio += 1

        tab_inicial += 1



