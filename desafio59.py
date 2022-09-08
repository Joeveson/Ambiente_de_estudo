# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar 
# [3] maior 
# [4] novos números 
# [5] sair do programa

# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
# maior = 0
# menor = 0
menu = ('''
Informe operação desejada:
\n[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos Números
[5] Sair''')
print(menu)
operacao = int(input('Informe a operação desejada: '))

while operacao != 5:
    if operacao > 5:
        print('ERRO: Digite uma opção válida.')
        operacao = int(input('Informe a operação desejada: '))

    elif operacao < 0:
        print('ERRO: Digite uma opção válida.')
        operacao = int(input('Informe a operação desejada: '))

    else:    
        if operacao == 1:
            operacao = n1 + n2
            print(f'A soma dos números {n1}+{n2} é igual a {operacao}.')
            operacao = int(input('Informe a operação desejada: '))

        if operacao == 2:
            operacao = n1 * n2
            print(f'A mulplicação dos números {n1}x{n2} é igual a {operacao}.')
            operacao = int(input('Informe a operação desejada: '))

        if operacao == 3:
            if n1 > n2:
            # maior = n1
            # menor = n2
                print(n1)
                operacao = int(input('Informe a operação desejada: '))
            if n2 > n1:
            # menor = n1
            # maior = n2
                print(n2)
                operacao = int(input('Informe a operação desejada: '))
            else:
                print('Os números informados são iguais.')
                operacao = int(input('Informe a operação desejada: '))
        if operacao == 4:
            new_n1 = int(input('Informe o novo primeiro número: '))
            new_n2 = int(input('Informe o novo segundo número: '))
            n1 = new_n1
            n2 = new_n2
            print(menu)
            operacao = int(input('Informe a operação desejada: '))
print('\033[1;31mPrograma encerrado!\033[m')
