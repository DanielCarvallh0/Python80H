# ******************************************************************************************************* #
# OBJETIVO:  Elaborar um programa que efetue a leitura de valores positivos inteiros até que um valor negativo seja informado.
# Ao final deverão ser apresentados o maior e o menor valores informados pelo usuário.
# Data: 05/09/2023
# Versão: 1.1
# ******************************************************************************************************* #


# ENTRADA DE DADOS

maior = 0
menor = 1000
valor = int(input('Digite o valor pode ser positivo ou negativo mas o número tem que ser inteiro: '))

# PROCESSAMENTO

while valor >= 0:

    if maior < valor:
        maior = valor

    if valor < menor:
        menor = valor


    valor = int(input('Digite o valor pode ser positivo ou negativo mas o número tem que ser inteiro: '))

# SAÍDA DE DADOS

print('O maior valor é ',maior)
print('O menor valor é ',menor)







        





    
        

