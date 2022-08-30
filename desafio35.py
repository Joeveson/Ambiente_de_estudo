# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1= float(input('Informe a primeira reta: '))
reta2= float(input('Informe a segunda reta: '))
reta3= float(input('Informe a terceira reta: '))

if reta1 == reta2 == reta3:
    print(f'Fórmula triângulo!') 
else:
    print(f'A fórmula não é triângulo!')