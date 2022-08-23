# DESAFIO 13 - Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Informe o seu salário atual: R$'))
aumento = salario * 0.15 
aumento_salario = salario + aumento
print (f'O valor do salário com aumento de 15% é R${aumento_salario:.2f}, você teve aumento de R${aumento:.2f}')