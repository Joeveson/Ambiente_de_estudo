# Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.


valor = float(input('Informe o valor desejado para empréstimo: '))
salario = float(input('Informe sua renda mensal: '))
ano = int(input('Informe em quantos anos você deseja financiar o imóvel: '))
print (f'O valor desejado para empréstimo é de R${valor:.2f}, sua renda mensal é de R${salario:.2f}.')
meses = 12*ano
print (f'O seu apartamento será quitado em {ano} anos, em {meses} parcelas.')
parcela = valor/meses
print (f'O valor das suas parcelas é de R${parcela:.2f}')

if salario * 0.3 > parcela:  
    print(f'Parabéns, o seu emprestimo foi \033[1;31mAPROVADO!!!\033[m')
    print(f'Você pagará {parcela} prestações de R${parcela:.2f} por {ano} anos.')
else:
    print(f'Sinto muito, o seu empréstimo foi \033[1;31mRECUSADO.\033[m')
    