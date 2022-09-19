# cont = 1
# while cont <= 10:
#     print (f'{cont} -> ', end='')
#     cont = cont +1
# print('Acabou!')


# cont = 1
# while True:
#     print (f'{cont} -> ', end='')
#     cont = cont +1
# print('Acabou!')

n = 0
s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s = s + n
print(f'A soma vale {s}')