# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 
# 5!= 5x4x3x2x1 = 120

cont = 1
numero = int(input('Informe o número desejado: '))
sequeq = ''
print(f'O fatorial do número {numero}', end = '')

while numero > 0:
    cont = cont * numero
    sequeq = sequeq + str(numero)

    if numero > 1:
        sequeq = sequeq +' x '

    numero = numero - 1 

print(f' é:\n{sequeq} = {cont}')


# cont = 1
# numero = int(input('Informe o número desejado: '))
# sequencia = ''
# print(f'O fatorial do número {numero}',end = ' ')

# for sequec in range(numero,0, -1):
#     cont = cont * sequec
#     sequencia = sequencia + str(sequec)

#     if sequec > 1:
#         sequencia = sequencia +' x '

# print(f'é: {sequencia} = {cont}')