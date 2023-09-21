# **************************************************************************************************************************** #

# Objetivo: Organizar 3 valores numericos em ordem crescente.
# Data: 29/08/2023
# Versão 1.0

#***************************************************************************************************************************** #

# Entrada de dados

v1 = input('valor1: ').replace(',','.')

v2 = input('valor2: ').replace(',','.')

v3 = input('valor3: ').replace(',','.')


v1 = float(v1)
v2 = float(v2)
v3 = float(v3)


# Saída de dados

if v1 >= v2 and v1 >= v3:
    if v2 >= v3:
        print(v3,v2,v1)
    
    else:
        print(v2,v3,v1)

elif v2 >= v1 and v2 >= v3:
    if v1 >= v3:
        print(v3,v1,v2)
    
    else:
        print(v1,v3,v2)

elif v3 >= v1 and v3 >= v2:
    if v2 >= v1:
        print(v1,v2,v3)
    
    else:
        print(v2,v1,v3)
