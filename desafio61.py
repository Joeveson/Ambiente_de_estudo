# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

n = int(input('Informe um número: '))
r = int(input('Informe a razão: '))
num = (n + (10-1) * r)
cont = n

while cont <= num:
    print(cont)
    cont = cont + r