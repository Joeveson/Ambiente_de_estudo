# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o valor do seu salário: '))
if salario > 1250:
    aumento = salario * 0.10 
    print (f'O salário informado foi {salario:.2f}R$, o qual é superior a 1.250,00 R$. De acordo com o aumento adotado pela empresa você teve aumento de {aumento:.2f}R$, totalizando {(salario)+(aumento):.2f}R$. O seu aumento foi de 10%.')
else:
    aumento = salario * 0.15
    print (f'O salário informado foi {salario:.2f}R$, o qual é inferior a 1.250,00 R$. De acordo com o aumento adotado pela empresa você teve aumento de {aumento:.2f}R$, totalizando {(salario)+(aumento):.2f}R$. O seu aumento foi de 15%.')