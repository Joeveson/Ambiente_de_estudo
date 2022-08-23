# DESAFIO 17 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt
co = float (input('Informe o comprimento do cateto oposto: '))
ca = float (input('Informe o comprimento do Cateto adjacente: '))
hi = (co**2) + (ca**2)
hi = sqrt(hi)
print (f'O comprimento da hipotenusa é {hi:.2f}')
