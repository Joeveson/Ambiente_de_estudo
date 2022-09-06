# Melhores o jogo do DESAFIO 28 onde computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('-=-' * 22)
print('\033[1;31mCOMPUTADOR:\033[m VOU PENSAR EM UM NÚMERO ENTRE 0 E 10. TENTE ADIVINHAR!')
print('-=-' * 22)
 
valor = randint(0,10)
cont = 1

valor_informado = int(input('DIGITE UM NÚMERO ENTRE 0 E 10: '))
# print(f'O NUMÉRO ESCOLHIDO POR VOCÊ FOI \033[1;33m{valor_informado}\033[m.')
while valor != valor_informado:
    valor_informado = int(input(f'\033[1;31mVOCÊ ERROU!!\033[m\nDIGITE UM NÚMERO ENTRE 0 E 10: '))
    cont = cont +1

print(f'PARABÉNS, VOCÊ ACERTOU!\nVOCÊ DIGITOU \033[1;33m{cont}x\033[m PARA ACERTA O NÚMERO QUE O COMPUTADOR PENSOU!')
print(f'O NUMÉRO ESCOLHIDO PELO COMPUTADOR FOI \033[1;33m{valor}\033[m.')
