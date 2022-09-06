# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma = 0
media = 0
qtd_mulheres = 0
maior = 0
h_mais_velho = 0

for c in range(1, 5):
    nome = (input('Informe o Nome: '))
    sexo = str(input('Informe o Sexo [M] Masculino [F] Feminino: ').upper())
    idade = int(input('Informe a Idade: '))

    soma = soma + idade
    media = soma / idade

    if sexo == 'M' and idade > maior:
        maior = idade
        h_mais_velho = nome
    print(h_mais_velho) 

    if sexo == 'F' or idade <20:
        qtd_mulheres = qtd_mulheres +1
    print (qtd_mulheres)
    
print (f'Média das idade é de {media:.2f}.')
print (f'Nome do homem mais velho é {h_mais_velho}.')

if qtd_mulheres == 0:
    print('Não tem mulheres no grupo! ')

else:
    print(f'Ao todo {qtd_mulheres} mulheres com menos de 20 anos.')

