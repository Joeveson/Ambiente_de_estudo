# Escreva um programa que leia  a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite

velocidade = float(input('Informe a velocidade do carro: '))
if velocidade >=80:
    print(f'Você ultrapassou a velocidade permitidade, você foi multado! ')
    valor = (velocidade - 80) * 7.0
    print (f'A multa vai custar {valor:.2f}R$.')
else:
    print(f'Você é um motorista exemplar!!!')