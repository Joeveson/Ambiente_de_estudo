# Faça um programa que leia 5 valores númericos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


num = [int(input('Digite um valor para a posição 0: ')),
       int(input('Digite um valor para a posição 1: ')),
       int(input('Digite um valor para a posição 2: ')),
       int(input('Digite um valor para a posição 3: ')),
       int(input('Digite um valor para a posição 4: '))]

print('-=-'*14)

print(f'Você digitou os valores: {num}')

print(f'O maior número digitado foi {max(num)} nas posições', end=' ')

for pos in range (0, len(num)):
    if num [pos] == max(num):
        print (f'{pos}...', end='')
    
print()
print(f'O menor número digitado foi {min(num)} nas posições', end=' ')

for pos in range (0, len(num)):
    if num [pos] == min(num):
        print (f'{pos}...', end='')
print()