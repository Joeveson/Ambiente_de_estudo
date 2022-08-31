# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
from datetime import date
ano = int(input('Qual o ano você quer Analisar? Coloque 0 para Analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano%400==0 or ano%100!=0 and ano%4==0:
    print (f'O ano informado foi {ano}, o ano informado tem 366 dias e \033[33;40mele é Bissexto!!!\033[m')
else:
    print (f'O ano informado foi {ano}, o ano informado tem 365 dias e \033[33;40mnão é Bissexto!!!\033[m')
