# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. no Final, mostre quantos números foram digitados e qual foi a soma entre eles. (Desconsiderar o Flag)

from itertools import count


n = 1
cont = 0
cont_n = 0

while n != 999:
    n = int (input('Informe um número: '))
    cont = n + cont
    cont_n = cont_n +1

print(f'Foram informados {cont_n} números e a soma deles é {cont}.')
