# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro / cheque 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

from itertools import product


valor_prod = float(input('Informe o valor do produto: '))
print (f'-=-' * 10)
print ('INFORME A FORMA DE PAGAMENTO:\n\n1 - À vista\n2 - À vista no Cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão')
print (f'-=-' * 10)

forma_pag = int(input('Informe a forma de pagamento conforme tabela acima: '))

if forma_pag == 1:
    desconto = valor_prod - (valor_prod * 0.10)
    valor_desc = valor_prod - desconto
    print (f'\033[1;33mO valor do seu produto é de R${valor_prod:.2f}! Você optou pela forma de pagamento à vista no dinheiro, o desconto foi de 10% = R${valor_desc:.2f} somando o valor total para pagamento de R${desconto:.2f}\033[m')

elif forma_pag == 2:
    desconto = valor_prod - (valor_prod * 0.05)
    valor_desc = valor_prod - desconto
    print (f'\033[1;33mO valor do seu produto é de R${valor_prod:.2f}! Você optou pela forma de pagamento à vista no dinheiro, o desconto foi de 5% = R${valor_desc:.2f} somando o valor total para pagamento de R${desconto:.2f}\033[m')

elif forma_pag == 3:
    print(f'\033[1;33mO valor do seu produto é de R${valor_prod:.2f}.\033[m')

elif forma_pag == 4:
    valor_pg = valor_prod + (valor_prod *0.20)
    juros = valor_pg - valor_prod
    print(f'\033[1;33mO valor do seu produto é de R${valor_prod:.2f}, sendo acrescentado 20% de acordo com a forma de pagamento, somando a mais R${juros:.2f} somando o valor total de {valor_pg:.2f}\033[m')

else:
    print('\033[1;33mSelecione a forma de pagamento CORRETA!\033[m')