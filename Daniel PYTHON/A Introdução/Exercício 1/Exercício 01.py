# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #
# Objetivo: Realizar o cálculo da média de 4 notas de um aluno.
# Data: 14 - 08 - 2023
# Versão: 1.1
# ♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥ #

# ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 

# Armazenando o nome do aluno.

nome_aluno = input('Qual o nome do aluno? ')

#Armazenando as notas do aluno.

nota1 = input('Nota 1: ')
nota2 = input('Nota 2: ')
nota3 = input('Nota 3: ')
nota4 = input('Nota 4: ')

#Somando as notas.
nota1 = float(nota1.replace(',','.'))
nota2 = float(nota2.replace(',','.'))
nota3 = float(nota3.replace(',','.'))
nota4 = float(nota4.replace(',','.'))

media =(nota1+nota2+nota3+nota4) / 4

#Exibindo o nome do aluno e as notas.

print('\033[46m o Aluno ', nome_aluno,'ficou com a média de ' , f'{media:_.1f}' ,'ficou na recuperação \033[m')

# ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ 
