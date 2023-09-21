# **************************************************************************************************************************** #

# Objetivo: Ler o nome e o sexo de uma pessoa e apresentar como saída uma mensagem personalizada.
# Data: 28/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados

nome = input('Qual é o seu nome: ').title()

sexo = input('Qual é o seu sexo: ').capitalize()

# Saída de dados

if sexo == 'Feminino':
    print('Bem-vinda Ilma. Sra.',nome)

elif sexo == 'Masculino':
    print('Bem-vindo Ilmo. Sr.',nome)

else:
    print('Dado inválido...')

