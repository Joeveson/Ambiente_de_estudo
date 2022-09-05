# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão. 

n = int(input('Informe um número: '))
r = int(input('Informe a razão: '))
for num in range(0, 10):
    print(n)
    n = n + 1 * r
