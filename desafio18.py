# DESAFIO 18 - Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Infome um ângulo qualquer: '))
rad = math.radians(ang)
sen = math.sin(rad)
co = math.cos(rad)
tan = math.tan(rad)
print (f'Se ângulo for {ang:.0f}°, o seno será {sen:.2f}, o cosseno será {co:.2f} e o tangente desse ângulo será {tan:.2f}.')