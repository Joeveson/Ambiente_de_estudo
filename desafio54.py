# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

ano = datetime.date.today()
menor_idade = 0
maior_idade = 0
print(f'O ano atual é {ano.year}')
for ano_nascimento in range(1, 8):
    ano_nascimento = int(input('Informe a data de nascimento: '))
    idade_atual = ano.year - ano_nascimento
    if idade_atual > 21:
        print(f'Você é maior de idade {idade_atual}.')
        maior_idade = maior_idade + 1

    elif idade_atual < 21:
        print(f'Você não é maior de idade {idade_atual}.')
        menor_idade = menor_idade +1

print(f'\033[1;31mAo todo tivemos {maior_idade} maiores e {menor_idade} menores de idade.\033[m')