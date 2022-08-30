# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Informe o ano desejado: '))
if ano%400==0 or ano%100!=0 and ano%4==0:
    print (f'O ano informado foi {ano}, o ano informado tem 366 dias e ele é Bissexto!!!')
else:
    print (f'O ano informado foi {ano}, o ano informado tem 365 dias e não é Bissexto!!!')
