# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar os valores. 

menu = ('''Digite uma opção para continuar:
[1] - SIM
[2] - Não
''')
n=1
contagem = 0
soma = 0

while n != 2:
    operacao = int(input('Informe um número inteiro: '))

    contagem = contagem +1
    soma = soma + operacao

    if contagem == 1:
        maior = operacao
        menor = operacao
    else:
        if operacao > maior:
            maior = operacao

        if operacao < menor:
            menor = operacao
    print(menu)
    n = int(input('Informe a opção desejada: '))

    while n != 2 and n != 1:
        print('Opção inválida, digite um número válido.')
        print(menu)
        n = int(input('Informe a opção desejada: '))
        

print(f'A média dos valores é {soma/contagem}.')
print(f'O maior valor é {maior} e o menor valor é {menor}.')