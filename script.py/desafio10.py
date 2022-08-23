
# DESAFIO 10 - Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

real = float(input('Informe quantos reais você tem: R$'))
cotacao_dolar = 3.27
print (f'A Quantidade de reais informa é R${real}, convertido em dólar é US${real/cotacao_dolar:.2f}')