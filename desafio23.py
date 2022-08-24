# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
# Ex: Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1 

numero = int(input('Informe um número entre 0 a 9999: '))

unidade = numero // 1%10
dezena = numero // 10%10
centena = numero // 100%10
milhar = numero // 1000%10

print (f'O número informado foi {numero}')
print (f'A unidade do número é {unidade}')
print (f'A dezena do número é {dezena}')
print (f'A centena do número é {centena}')
print (f'A milhar do número é {milhar}.')