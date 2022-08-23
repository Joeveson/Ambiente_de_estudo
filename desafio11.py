# DESAFIO 11 - Faça um programa que leia largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m2.

largura = float(input('Informe a Largura da Parede: ')) 
altura = float(input('Informe a Altura da Parede: '))
area = largura * altura 
tinta = area/2
print (f'Para pintar uma parede de {area} metros é necessário {tinta:.2f} litros de tinta.')
