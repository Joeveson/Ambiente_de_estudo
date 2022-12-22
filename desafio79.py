# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.


num = []
while True:
    valor_dig = int(input('Digite um valor: '))
    if valor_dig in num:
        print('Valor duplicado, não vou adiconar.')
    else:
        num.append (valor_dig)
        print('Valor adicionado com sucesso...')

    opcao = str(input('Quer continuar? [S/N] '))

    if opcao in 'nN':
        break

print('-=-'*12)
print(f'Você digitou os valores {sorted(num)}')