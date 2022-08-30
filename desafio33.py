# Faça um programa que leia três números e mostre qual é o maior e qual é o menor. 

n1 = float(input('Informe o Primeiro Número: '))
n2 = float(input('Informe o Segundo Número: '))
n3 = float(input('Informe o Terceiro Número: '))
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print (f'O maior número digitado foi {maior:.0f} ')
print (f'O menor número digitado foi {menor:.0f}.')