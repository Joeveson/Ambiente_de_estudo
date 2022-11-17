# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A- Quantas pessoas tem mais de 18 anos.
# B- Quantos homens foram cadastrados. 
# C- Quantas mulheres tem menos de 20 anos.

cont = 0
hom = 0
mul = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = ' '
    while sexo not in 'FM':
        print("""Informe seu sexo:  

        [F] = Feminino 
        [M] = Masculino
        """)
        sexo = str(input('Informe seu sexo: ').upper())
    op = 0
    while op != 1 and op != 2:
        print("""Deseja continuar ?

        [1] - SIM 
        [2] - NÃO
        """)
        op = int(input('Informe a opção de desejada: '))
        
    if idade > 18:
        cont = cont +1

    if sexo == 'M':
            hom = hom +1
 
    elif sexo == 'F':
            idade < 20
            mul = mul +1 

    if op != 1:
        print('Programa Encerrado.')
        break

print (f'Existe {cont} pessoa(s) com mais de 18 anos. \nForam cadastrados {hom} pessoa(s) do sexo Masculino. \nExiste {mul} pessoa(s) do sexo Feminino com menos de 20 anos.')