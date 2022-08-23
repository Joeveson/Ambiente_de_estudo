# DESAFIO 15 - Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado. 

km = float(input('Informe a quantidade de quilômetros percorrida: '))
dia = int(input('Informe a quantidade de dias que o carro foi alugado: '))
total = (60*dia) + (0.15*km)
print (f'A quantidade de quilômetros rodados foi {km:.0f}km, foi alugado por {dia} dias e o valor total do aluguel foi de {total:.2f}R$')