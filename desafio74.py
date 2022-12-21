# CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS E COLOCAR EM UMA TUPLA.
# DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMERO GERADO E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.

import random
menor_num = 0
maior_num = 0

print('Os números sorteados foram:')

lista_valores = (random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100))

print (lista_valores)

for pos, i in enumerate (lista_valores):
    
    if pos == 0:
        menor_num = i
        maior_num = i

    if i < menor_num:
        menor_num = i
        
    if i > maior_num:
        maior_num = i

print(f'O maior número sorteado foi {maior_num}.')
print(f'O menor número sorteado foi {menor_num}.') 


# OPERAÇÃO REALIZADA PELO GUANABARA

print(f'O maior número sorteado foi {max(lista_valores)}.')
print(f'O menor número sorteado foi {min(lista_valores)}.') 