# Faça um programa que calcula a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
for num in range(0, 500):
    if num %2 != 0:
        if num %3 ==0:
            s = s + num

print(f'A soma dos múltiplos é: \033[1;33m{s}\033[m')