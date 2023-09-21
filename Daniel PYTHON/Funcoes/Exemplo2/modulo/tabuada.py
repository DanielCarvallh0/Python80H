# ******************************************************************************************************* #
# OBJETIVO:  Criar um sistema para gerenciar o cálculo de uma tabuada
# Data: 05/09/2023
# Versão: 1.0
# ******************************************************************************************************* #


# ENTRADA DE DADOS

def calcular_tabuada(tabuada_inicial, tabuada_final, contador_inicial, contador_final):

    tab_inicial = tabuada_inicial
    tab_final = tabuada_final
    cont_inicial = contador_inicial
    cont_final = contador_final
    resultado = 0
    status = False

    if tab_inicial == '' or tab_final == '' or cont_inicial == '' or cont_final == '':
        print('ERROR! PC EXPLODINDO EM 3 SEGUNDOS...')

    elif int(tab_inicial) < 2 or int(tab_inicial) > 100 or int(tab_final) < 2 or int(tab_final) > 100:
        print('ERROR! PC EXPLODINDO EM 3 SEGUNDOS...')

    elif int(cont_inicial) < 1 or int(cont_inicial) > 50 or int(cont_final) < 1 or int(cont_final) > 50:
        print('ERROR! PC EXPLODINDO EM 3 SEGUNDOS...')

    else:
        
        cont_inicial = int(cont_inicial)
        cont_final = int(cont_final)
        tab_inicial = int(tab_inicial)
        tab_final = int(tab_final)

        while tab_inicial <= tab_final:
            print('TABUADA DO ', tab_inicial)

            while cont_inicial <= cont_final:
                status = True
                resultado = tab_inicial * cont_inicial
                print(tab_inicial, 'X', cont_inicial, '=', resultado)

                cont_inicial += 1

            cont_inicial = int(contador_inicial) # RETORNA O CONT_INICIAL AO VALOR DE ORIGEM

            tab_inicial += 1

    return status # RETORNA UM BOOLEANO (TRUE) SE A TABUADA FOR PROCESSADA OU (FALSE) CASO A TABUADA NAO TENHA SIDO PROCESSADA...


















