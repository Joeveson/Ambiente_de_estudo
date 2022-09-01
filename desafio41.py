# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de uma atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIN
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

import datetime

ano_nasc = int(input('Informe o seu Ano de nascimento: '))
ano = datetime.date.today()
print (f'O ano atual é \033[1;33m{ano.year}\033[m!')
idade_atual = ano.year - ano_nasc
print (f'Você tem \033[1;33m{idade_atual}\033[m anos.')

if idade_atual <= 9:
    print(f'Você é da categoria \033[1;33mMIRIN\033[m.')

elif idade_atual > 9 and idade_atual <= 14:
    print(f'Você é da categoria \033[1;33mINFANTIL\033[m.')

elif idade_atual  > 14 and idade_atual <= 19:
    print(f'Você é da categoria \033[1;33mJUNIOR\033[m.')

elif idade_atual == 20:
    print(f'Você é da categoria \033[1;33mSÊNIOR\033[m.')

elif idade_atual > 20:
    print(f'Você é da categoria \033[1;33mMASTER\033[m.')
