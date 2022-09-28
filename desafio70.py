# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A- Qual é o total de gastos na compra. 
# B- Quantos produtos custam mais de R$1000. 
# C- Qual é o nome do produto mais barato.

soma = 0
cont_prod = 0
prod_barato = ""
cont_preco = 1

while True:
    nome_prod = str(input('Informe o nome do Produto: '))
    preco_prod = float(input('Informe o preço do Produto: R$'))

    print("""Deseja continuar ?
    
    [1] - SIM
    [2] - NÃO         
    """)
    op = int(input('Informe a opção desejada: '))
    soma = soma + preco_prod
    if preco_prod > 1000:
        cont_prod = cont_prod + 1

    if  cont_prod == 1:
        menor = preco_prod
    
    if preco_prod <= menor:
        menor = preco_prod
        prod_barato = nome_prod
      
    if op != 1:
        print('Programa Encerrado.')
        break

print(f'Valor total de gastos foi de R${soma:.2f}')
print(f'{cont_prod} produto(s) custa mais de R$1000 reais.')
print(f'O menor produto foi {prod_barato}')