
# DESAFIO 12 - Faça um algoritmo que leia preço de uma produto e mostre seu novo preço com 5% de desconto.

produto = float(input('Informe o preço do Produto: R$'))
desc = produto * 0.05
prod_desc = produto - desc
print (f'O valor do produto com desconto de 5% é R${prod_desc:.2f}, você economizou R${desc:.2f}')
