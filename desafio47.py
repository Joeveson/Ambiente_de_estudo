# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print(f'\033[1;34m-=-\033[m'*8)
print('\033[1;33mNÚMEROS PARES DE 0 A 50\033[m')
print(f'\033[1;34m-=-\033[m'*8)

for c in range(1, 51):
    if c %2 == 0:
        print(c)
print('ESSES SÃO OS NÚMEROS PAR DE 0 A 50.')

