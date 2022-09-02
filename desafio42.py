# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print (f'-=-' * 10)
print (f'Analisador de Triângulos')
print (f'-=-' * 10)
reta1= float(input('Informe a primeira reta: '))
reta2= float(input('Informe a segunda reta: '))
reta3= float(input('Informe a terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print(f'\033[4;33mA Fórmula é um triângulo!\033[m') 

    if reta1 == reta2 == reta3 == reta1:
        print(f'\033[4;33mTriângulo Equilátero!\033[m') 

    elif reta1 == reta2 or reta2 == reta3 or reta3 ==reta1:
        print(f'\033[4;33mTriângulo Isósceles\033[m')

    elif reta1 != reta2 != reta3 != reta1:
        print(f'\033[4;33mTriângulo Escaleno!\033[m')
