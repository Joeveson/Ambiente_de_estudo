# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print (f'-=-' * 10)
print (f'Analisador de Triângulos')
print (f'-=-' * 10)
reta1= float(input('Informe a primeira reta: '))
reta2= float(input('Informe a segunda reta: '))
reta3= float(input('Informe a terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'A Fórmula é um triângulo!') 
else:
    print(f'A fórmula não é triângulo')