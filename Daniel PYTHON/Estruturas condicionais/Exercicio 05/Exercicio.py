# **************************************************************************************************************************** #

# Objetivo: Descobrir a média de um aluno pelas notas e dizer se está aprovado ou reprovado...
# Data: 28/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados

nome = input('Digite o nome do aluno: ').title()

nota1 = input('Digite a nota1 do aluno: ').replace(',','.')

nota2 = input('Digite a nota2 do aluno: ').replace(',','.')

nota3 = input('Digite a nota3 do aluno: ').replace(',','.')

nota4 = input('Digite a nota4 do aluno: ').replace(',','.')

# Processamento

nota1 = float(nota1)
nota2 = float(nota2)
nota3 = float(nota3)
nota4 = float(nota4)

media = (nota1 + nota2 + nota3 + nota4) / 4

# Saída de dados

if nota1 > 10 or nota1 < 0 or nota2 > 10 or nota2 < 0 or nota3 > 10 or nota3 < 0 or nota4 > 10 or nota4 <0:
    print('ERROR!')

else:
    if media >= 7:
        print(nome , 'Aprovado! Média: ',media)

    elif media >= 4:
        print(nome , 'Ficou de exame por ter essa média: ',media)
        exame = float(input('Nota de exame: '))
        calculo = (exame + media) / 2
        if calculo >= 5:
            print(nome , 'Aprovado em exame! Média: ',calculo)
        else:
            print(nome , 'Reprovado em exame!Média: ', calculo)

    else:
        print(nome , 'Reprovado! Média: ',media)



