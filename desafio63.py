# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de fibonacci. 

# Ex: 0 - 1 - 2 - 3 - 5 - 8 

numero = int(input('Informe a quantidade de números da Sequência de Fibonacci que você deseja: '))
a = 0
b = 1
print(f'{a} → {b} → ', end='') 
count = 3

while count <= numero:
    c = a + b
    print(f'{c} → ', end='')
    a = b
    b = c
    count = count + 1 

print('FIM')
