# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número pensado pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 

import random
valor = [0, 1 , 2 , 3 , 4 , 5]
pensar = random.choice(valor)
valorinformado = int(input('Informe um número inteiro de 0 a 5: '))
if valor == valorinformado:
    print (f'O número informado foi {pensar}.Você venceu o Programa!!!')
else:
    print (f'O número informado foi {pensar}. Você perdeu para o programa!!!')
