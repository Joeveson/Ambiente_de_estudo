# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:

# A média de idade do grupo.
# Qual o nome do homem mais velho.
# Quantas mulheres têm menos de 20 anos.

soma = 0
count_m = 0
media = 0
maior = 0
homem_velho = ''

for c in range(1, 5):
    nome = (input('Informe o Nome: '))
    sexo = int(input('Informe o Sexo [1] Masculino [2] Feminino: ').upper())
    idade = int(input('Informe a Idade: '))



#     soma = soma + idade
#     media = soma / idade

#     if sexo == "1" and idade > maior:
#         maior = idade
#         homem_velho = nome
    
#     if sexo == "2" and idade <20:
#         count_m = count_m +1

# print (f'Média das idade é de {media:.2f}.')
# print (f'Nome do homem mais velho é {homem_velho}.')

# if count_m == 0:
#     print('Não tem mulheres no grupo! ')

# else:
#     print(f'Ao todo {count_m} mulheres com menor de 20 anos.')

