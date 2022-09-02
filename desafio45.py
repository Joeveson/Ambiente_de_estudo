# Crie um programa que faça o computador jogar jokenpô com você.

from random import choice
from time import sleep

print (f'\033[1;33m-=-\033[m' * 7)
print('\033[1;36mVAMOS JOGAR JOKEMPÔ!\033[m')
print (f'\033[1;33m-=-\033[m' * 7)

print (f'\033[1;33;45m1 - SIM - 2 - NÃO\033[m')
n = int(input('Informe a opção desejada: '))
sort = choice (["pedra","papel","tesoura"])

if n ==1:
    print('\033[1;33;44mEscolha "pedra, papel, tesoura"\033[m')
    print (f'\033[1;33m-=-\033[m' * 7)
    escolher = str(input('\033[1;33;44mEscolha:\033[m').lower())
    sleep(1)
    print('\033[1;31mJO\033[m')
    sleep(2)
    print('\033[1;32mKEM\033[m')
    sleep(2)
    print('\033[1;33mPÔ!!\033[m')
    print (f'\033[1;33m-=-\033[m' * 7)
    print(f'\033[1;33;45mO computador escolheu {sort}\033[m')
    print(f'\033[1;33;44mVocê escolheu {escolher}\033[m')
    print (f'\033[1;33m-=-\033[m' * 7)
    if sort == escolher:
        print ('\033[1;31mATENÇÃO: O jogo deu empate. JOGUE NOVAMENTE!\033[m')
        print (f'\033[1;33m-=-\033[m' * 7)
    else:
        jogador = f'{sort} {escolher}'
        if "tesoura papel" == jogador or "papel tesoura" == jogador:
            ganhou = "tesoura"
        elif "pedra tesoura" == jogador or "tesoura pedra" == jogador:
            ganhou = "pedra"
        elif "pedra papel" == jogador or "papel pedra" == jogador:
            ganhou = "papel"

        if ganhou == sort:
            print ('\033[1;33;45mCOMPUTADOR GANHOU!\033[m')
            print (f'\033[1;33m-=-\033[m' * 7)
        else:
            print ('\033[1;33;44mVOCÊ GANHOU!\033[m')
            print (f'\033[1;33m-=-\033[m' * 7)
elif n ==2:
    print('\033[1;36mOK, podemos jogar outra hora!\033[m')

else:
    print('\033[1;31mATENÇÃO: Escolha uma opção válida!\033[m')