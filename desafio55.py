# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

menor_peso = 0
maior_peso = 0
for c in range(1, 6):
    peso = float(input('Informe o peso: '))
    if c == 1:
        maior_peso = peso
        menor_peso = peso
    else: 
        if peso > maior_peso:
            maior_peso = peso

        elif peso < menor_peso:
            menor_peso = peso

print(f'O maior peso foi {maior_peso:.2f}kg e o menor peso foi {menor_peso:.2f}kg.')