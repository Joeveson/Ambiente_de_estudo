# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogo de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep

print(f'\033[1;34m-=-\033[m'*6)
print('\033[1;33mCONTAGEM REGRESSIVA\033[m')
print(f'\033[1;34m-=-\033[m'*6)
for c in range(10, 0, -1):
    print (c)
    sleep(1)
print("\U0001F4A5\U0001F387\U0001F387\U0001F387")

