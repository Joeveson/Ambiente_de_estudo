# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

cont = 0 
num = int(input('Informe um número inteiro para saber se é número primo: '))
div = []
for a in range(num):
    if num%(a+1) == 0:
        cont = cont + 1
        div.append(a+1)

if cont == 2:
    print (f'O numero é primo divisivel por {div}')
else:
    print (f'O numero não é primo pois é divisivel por {div}')
