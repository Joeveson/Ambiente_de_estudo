# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores. 

numero = int(input('INFORME UM NÚMERO: '))
media = 0
maior_valor = 0
menor_valor = 0
cont = 0
menu = ('''VOCÊ DESEJA CONTINUAR?
[1] SIM
[2] NÃO
''')
print(menu)
operacao = int(input('INFORME A OPÇÃO DESEJADA: '))


while operacao != 2:
    if operacao > 2:
        print('ERRO: DIGITE UMA OPÇÃO VÁLIDA.')
        operacao = int(input('INFORME A OPÇÃO DESEJADA: '))

    elif operacao <= 0:
        print('ERRO: DIGITE UMA OPÇÃO VÁLIDA.')
        operacao = int(input('INFORME A OPÇÃO DESEJADA: '))

    else:
        if operacao == 1:
            new_operacao = int(input('INFORME UM NOVO NÚMERO: '))
            numero = new_operacao
        print(menu)
        operacao = int(input('INFORME A OPÇÃO DESEJADA: '))

        if operacao ==2:
            print('OPERAÇÃO ENCERRADA.')
            if numero > numero:
                maior_valor == numero

            if numero < numero:
                menor_valor == numero

            else:
                cont = cont +1
                media = numero / cont



print(f'A média dos valores é {media}')
print(f'O maior valor é {maior_valor} e o menor valor é {menor_valor}')

