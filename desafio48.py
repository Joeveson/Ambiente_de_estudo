# Faça um programa que calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
count = 0
s = 0
for num in range(0, 500):
    if num %2 != 0:
        if num %3 ==0:
            count = count +1
            s = s + num

print(f'A soma de todos \033[1;33m{count}\033[m valores solicitados é: \033[1;33m{s}\033[m')