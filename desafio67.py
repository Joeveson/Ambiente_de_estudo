# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Informe um número para ver sua tabuada: '))
    if num <0:
        break
    for c in range (1,11):
        print(f'{num} x {c} = \033[1;31m{num*c}\033[m')

print('\033[1;33mO programa foi encerrado!!\033[m')
