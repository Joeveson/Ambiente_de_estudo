# DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
# A) QUANTAS VEZES APARECEU O VALOR 9.
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3. 
# C) QUAIS FORAM OS NÚMEROS PARES.

num = (int(input('Informe o primeiro valor: ')),
       int(input('Informe o segundo valor: ')),
       int(input('Informe o segundo valor: ')),
       int(input('Informe o segundo valor: ')))

cont = 1
par = 0

print (f'O valores informados foram: \n{num}')
print (f'O número 9 apareceu {num.count(9)} vezes.')
if 3 in num:
    print (f'O valor três apareceu na posição {num.index(3)+1}.')
else:
    print (f'O valor 3 não foi digitado em nenhuma posição.')
print ('Os números pares são: ', end='')
for par in num:
    if par % 2 == 0:
        print(par, end=' ')
