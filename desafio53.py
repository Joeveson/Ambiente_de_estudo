# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo desconsiderando os espaços.

# FRASE QUE VOCÊ PODE LER DE TRÁS PRA FRENTE - DA FRENTE PRA TRÁS
# EX: APOS A SOPA / A SACADA DA CASA / A TORRE DA DERROTA / O LOBO AMA O BOLO / ANOTARAM A DATA DA MARATONA 

frase = str(input('Informe a frase: ').upper())
frase = frase.replace(" ",'')
inverte = frase[::-1]
if inverte == frase:
    print('A frase é um palídromo.')
else:
    print('A frase não é um palídromo.')

print(f'A frase que você digitou invertida fica da seguinte forma: {inverte}')