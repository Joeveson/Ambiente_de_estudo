# Faça um programa que leia dois números inteiros  e compare-os, mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
print (f'Os dois valores informados foram \033[1;32m{n1} - {n2}\033[m.')
if n1 > n2:
    print(f'O \033[1;32mPRIMEIRO\033[m valor é o \033[1;32mMAIOR!\033[m ')
elif n2 > n1:
    print(f'O \033[1;32mSEGUNDO\033[m  valor é o \033[1;32mMAIOR!\033[m ')
elif n1 == n2: 
    print(f'Os dois valores são \033[1;32mIGUAIS!\033[m ')
