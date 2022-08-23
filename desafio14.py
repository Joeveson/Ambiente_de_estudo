
# DESAFIO 14 - Escreva um programa que converte uma temperatura digitada em C° e converta para F°.

c = float(input('Informe a temperatura em Celsius: C°'))
f = 9 * c / 5 + 32 
print (f'A temperatura em Celsius é {c}C°, convertida para Fahrenheit é: {f:.1f}F°')