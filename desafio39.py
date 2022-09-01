# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime

ano_nasc = int(input('Informe seu ano de nascimento: '))
ano = datetime.date.today()
print (f'O ano atual é \033[1;33m{ano.year}\033[m!')
idade_atual = ano.year - ano_nasc
print (f'Você tem \033[1;33m{idade_atual}\033[m anos.')
idade_permit = 18

if idade_atual < idade_permit:
    print (f'\033[1;33mATENÇÃO:\033[m Você ainda não tem idade suficiente para alistar no serviço militar, ainda falta \033[1;33m{(idade_permit-idade_atual)} anos\033[m.')

if idade_atual == idade_permit:
    print(f'\033[1;33mPARABÉNS:\033[m É hora de se alistar ao serviço militar.')

if idade_atual > idade_permit:
    print(f'\033[1;33mATENÇÃO:\033[m Você já passou do tempo do alistamento à \033[1;33m{(idade_atual-18)}\033[m anos! Você deveria se Alista no ano de \033[1;33m{(ano.year - (idade_atual-18))}\033.')

