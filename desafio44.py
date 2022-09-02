# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro / cheque 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

valor_prod = float(input('Informe o valor do produto: '))
print (f'-=-' * 10)
print ('INFORME A FORMA DE PAGAMENTO:\n\n1 - À vista\n2 - À vista no Cartão\n3 - 2x no cartão\n4 - 3x ou mais no cartão')
print (f'-=-' * 10)

forma_pag = int(input('Informe a forma de pagamento conforme tabela acima: '))

if forma_pag == 1:
    desconto = valor_prod - (valor_prod * 0.10)
    # valor_desc = valor_prod - desconto

elif forma_pag == 2:
    desconto = valor_prod - (valor_prod * 0.05)
    # valor_desc = valor_prod - desconto

elif forma_pag == 3:
    desconto = valor_prod
    parcela = desconto / 2
    # valor_desc = valor_prod - desconto
    print(f'\033[1;33mSua compra será parcelada em 2x de R${parcela:.2f}.\033[m')

elif forma_pag == 4:
    desconto = valor_prod + (valor_prod *0.20)
    total_parcelas = int(input('Quantas Parcelas? '))
    parcela = desconto / total_parcelas
    # valor_desc = valor_prod - desconto
    print(f'\033[1;33mSua compra será parcelada em {total_parcelas}x de R${parcela:.2f} COM JUROS.\033[m')

else:
    desconto = valor_prod
    print('\033[1;33mSelecione a forma de pagamento CORRETA!\033[m')


print (f'\033[1;33mA sua compra de R${valor_prod:.2f} vai custar R${desconto:.2f} no final.\033[m')