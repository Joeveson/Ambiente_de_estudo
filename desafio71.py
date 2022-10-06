# Crie um programa que simule o funcionamento de um caixa eletrônico. No ínicio, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
# OBS: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-=-'*20)
print('CAIXA ELETRÔNICO')
print('-=-'*20)

valor = int(input('Informe o valor do Saque: '))
total = valor
cedula = 100
totalcedu = 0

while True:
    if total >= cedula:
        total = total - cedula
        totalcedu = totalcedu +1
    
    else:
        if totalcedu > 0:
            print(f'Total de {totalcedu} cédulas de R$ {cedula}')
        
        if cedula == 100:
            cedula = 50
        
        elif cedula == 50:
            cedula = 20
        
        elif cedula == 20:
            cedula = 10
        
        elif cedula == 10:
            cedula = 1
        totalcedu = 0

        if total == 0:
            break

print ('Saque realizado com sucesso, volte sempre!')