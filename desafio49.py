# Refaça o DESAFIO 09, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

num = int(input('\033[1;31mInforme um número: \033[m'))

for c in range(1, 11):
    print(f'\033[1;33m{num} x {c} = {num*c}\033[m')