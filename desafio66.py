# Crie um Programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

n = 0
s = 0
cont = 0
while True:
    n = int(input('Informe um número inteiro: '))
    if n == 999:
        break
    s = s + n
    cont = cont +1
print (f'Foram digitados \033[1;31m{cont}\033[m números.')
print (f'A soma dos números é \033[1;31m{s}\033[m.')
print ('\033[1;31mPROGRAMA ENCERRADO!\033[m')
