# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0 
num = int(input('Informe um número inteiro para saber se é número primo: '))
# div = []
for a in range(1, num + 1):
    if num % a == 0:
        print('\033[33m', end =' ')
        cont = cont + 1
        # div.append(a+1)
    else:
        print('\033[31m', end =' ')
    print(f'{a}', end='')

print (f'\n\033[mO numero {num} foi divisível {cont} vezes.')

if cont ==2:
    print('Ele é PRIMO!')
else:
    print('Não é PRIMO!')
