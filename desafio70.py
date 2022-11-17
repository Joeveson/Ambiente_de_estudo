# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
# A- Qual é o total de gastos na compra. 
# B- Quantos produtos custam mais de R$1000. 
# C- Qual é o nome do produto mais barato.

soma = 0
cont_prod = 0
prod_barato = ''
menor = 0
maior_mil = 0

while True:
    nome_prod = str(input('Informe o nome do Produto: '))
    preco_prod = float(input('Informe o preço do Produto: R$'))
    soma = soma + preco_prod
    cont_prod = cont_prod +1

    if preco_prod > 1000:
        maior_mil = maior_mil + 1    

    if  cont_prod == 1 or preco_prod < menor:
        menor = preco_prod
        prod_barato = nome_prod

    op = 0
    while op != 1 and op != 2:
        print("""Deseja continuar ?
        
        [1] - SIM
        [2] - NÃO         
        """)
        op = int(input('Informe a opção desejada: '))
          
    if op != 1:
        print('Programa Encerrado.')
        break

print(f'Valor total de gastos foi de R${soma:.2f}')
print(f'{maior_mil} produto(s) custou mais de R$1000 reais.')
print(f'O menor produto foi {prod_barato} que custa R${menor:.2f}')