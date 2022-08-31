# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número pensado pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu. 

from random import randint
from time import sleep
valor = randint(0, 5)
print (f'-=-' * 20)
print (f' Vou pensar em um número entre 0 e 5.\n Tente adivinhar!')
print (f'-=-' * 20)
valorinformado = int(input(' Em que número eu pensei? '))
print (f' PROCESSANDO...')
sleep(3)
if valorinformado == valor:
    print (f' O número informado foi {valor}.\n PARABÉNS! Você venceu o Programa!!!')
else:
    print (f' GANHEI! O número informado por você foi {valorinformado}.\n O número que eu pensei foi {valor} Você perdeu para o programa!!!')
