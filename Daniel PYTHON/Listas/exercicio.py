# ********************************************************************************************* #
# Objetivo: Criar uma agenda com base nas requisições solicitadas.
# Data: 21/09/2023
# Versão: 1.0
# ********************************************************************************************* #

import os
import sys

os.system('cls')

print('\nAGENDA')

cadastro = {}
while True:
    menu = int(input('\n1. Cadastro\n2. Buscar usuário\n3. Lista dos usuários\n4. Sair\n\nOpção: '))

    if menu == 1:
        nome = input('\nPor favor, Digite o Nome: ').capitalize()
        email = input('Por favor, Digite o email: ')
        numero = input('Por favor, Digite o numero: ')
        
        cadastro[nome] = {'nome': nome, 'email': email, 'numero': numero}

    elif menu == 2:
        os.system('cls')
        busca = input('Digite o Nome de quem deseja procurar: ').capitalize()

        for chave in cadastro.keys():

            if chave == busca:
                print('Nome: ',cadastro[busca]['nome'])
                print('Email: ',cadastro[busca]['email'])
                print('Telefone: ',cadastro[busca]['numero'])

            else:
                print('error')

    elif menu == 3:
        os.system('cls')
        if cadastro != '':
            for chave in cadastro.values():
                print('\n',chave['nome'])
                print(chave['email'])
                print(chave['numero'])

        else:
            print('')

    elif menu == 4:
        sys.exit()

    else:
        print('\nINSIRA UMA DAS OPÇÕES VÁLIDAS ACIMA')
