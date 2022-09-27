# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A- Quantas pessoas tem mais de 18 anos.
# B- Quantos homens foram cadastrados. 
# C- Quantas mulheres tem menos de 20 anos.

cont = 0
while True:
    idade = int(input('Informe sua idade: '))
    print("""Informe seu sexo:  
    [F] = Feminino 
    [M] = Masculino
    """)
    sexo = str(input('Informe seu sexo: ').upper())
    if idade > 18:
        cont = cont +1
        print (f'Existe {cont} pessoa(s) com mais de 18 anos.')
    
    if sexo == 'H':
        cont = cont +1
        print (f'Foram cadastrados {cont} Homen(s).')
 
    if sexo == 'M':
        idade > 20
        cont = cont +1
        print (f'Existe {cont} mulhere(s) com menos de 20 anos.')