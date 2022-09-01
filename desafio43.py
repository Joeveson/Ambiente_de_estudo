# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua Altura: '))
imc = peso/altura**2
print (f'O IMC informado foi \033[1;33;44m{imc:.1f}\033[m')

if imc < 18.5:
    print(f'\033[1;33mAbaixo do peso!\033[m')

elif imc == 18.5 or imc < 25:
    print('\033[1;33mPeso ideal!\033[m')

elif imc == 25 or imc < 30:
    print('\033[1;33mSobrepeso!\033[m')

elif imc == 30 or imc <40:
    print('\033[1;33mObesidade!\033[m')

elif imc > 40:
    print('\033[1;33mObersidade Móbida!\033[m')