# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
# Ex: Ana Maria de Souza
# primeiro: Ana
# último = Souza

nome = str(input('Informe o Nome Completo: ').strip().lower().title())
parte = nome.split()
print (f'O primeiro nome é: {(parte[0])}')
print (f'O último nome é: {parte[len(parte)-1]}')