# ************************************************************************************************************************************************* #
# Objetivo: Realizar a entrada do nome e 4 notas escolares de um aluno e apresentar a média e o status de aprovação do aluno.
# Data: 21/08/2023
# Versão: 2.1
# ************************************************************************************************************************************************* #

# Entrada de dados 
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
nota3 = float(input('Digite a nota3: '))
nota4 = float(input('Digite a nota4: '))
frequencia = int(input('Digite a frequencia do aluno: '))


# Processamento

media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída de dados

# Versão 1.0

# if media >= 7:
#     print('A média do aluno', nome, 'foi de: ',media)
#     print('O aluno está aprovado!')

# else:
#     print('A média do aluno ', nome, 'foi de: ', media)
#     print('O aluno está reprovado!')


# Versão 2.0

# if media >= 7:
#     if frequencia >= 75:
#         print('A média do aluno', nome, 'foi de: ',media)
#         print('O aluno está aprovado!')

#     else:
#         print('Aluno reprovado por frequência!')

# else:
#     print('A média do aluno ', nome, 'foi de: ', media)
#     print('O aluno está reprovado!')


# Versão 2.1


# if media >= 7 and frequencia >= 75:
#     print('O aluno está aprovado!')

# else:
#     print('O aluno está reprovado!')


if nota1>10 or nota1<0 or nota2>10 or nota2<0 or nota3>10 or nota3<0 or nota4>10 or nota4<0 or frequencia <0 or frequencia >100:
#     print('dado invalido')

# else:
#     if media >= 7 and frequencia >= 75:
#         print('O aluno está aprovado!')

#     else:
#         print('O aluno está reprovado!')


# if nota1 <= 10 and nota1 >=0 and nota2 <= 10 and nota2 >=0 and nota3 <= 10 and nota3 >=0 and nota4 <= 10 and nota4 >=0 and frequencia >=0 and frequencia <= 100:

#     if media >= 7 and frequencia >= 75:
#         print('aluno aprovado',media,frequencia)
    
#     else:
#         print('aluno reprovado!',media,frequencia)

# else: 
#     print('dado invalido',media,frequencia)
        
