# Melhores o DESAFIO 61, perguntando para a o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos. 


numero = int(input('Informe um número: '))
razao = int(input('Informe a razão: '))
n = numero
mais_numero = 10
cont = 1
total = 0 

while mais_numero != 0:
    total = total + mais_numero

    while cont <= total:
        print(f'{n} →', end =' ')
        n = n + razao
        cont = cont + 1
    mais_numero = int(input('Quantos termos você quer mostrar a mais? '))

print(f'FIM, foram digitados {cont} termos.')
