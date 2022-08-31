# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR

numero = int(input('Informe um número inteiro: '))
if numero %2 == 0:
    print (f'O Número {numero} é \033[0;30;42mPAR\033[m!!')
else:
    print (f'O Número {numero} é \033[0;30;42mÍMPAR\033[m!!')