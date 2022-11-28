# DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
# A) QUANTAS VEZES APARECEU O VALOR 9.
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3. 
# C) QUAIS FORAM OS NÚMEROS PARES.

n1 = int(input('Informe o primeiro valor: '))
n2 = int(input('Informe o segundo valor: '))
n3 = int(input('Informe o terceiro valor: '))
n4 = int(input('Informe o quarto valor: '))
cont = 1
par = 0
valores = (n1, n2, n3, n4)

print (f'O valores informados foram: \n{valores}')
print (f'O número 9 apareceu {valores.count(9)} vezes.')
print (f'O valor três apareceu na posição {valores.index(3)+1}.')

print ('Os números pares são:')
for par in (valores):
    if par % 2 == 0:
        print (par)