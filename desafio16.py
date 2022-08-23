# DESAFIO 16 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
# Ex: Digite um número: 6.127
# O número 6.127 tem a parte inteira 6.

from math import floor
nreal = float(input('Digite um número real: '))
nint = floor(nreal)
print (f'O número informado é {nreal} e sua parte inteira é {nint}')