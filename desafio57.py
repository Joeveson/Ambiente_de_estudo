# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Informe o sexo: [M/F] ').upper())
    # print(sexo)
    if sexo != 'F' and sexo != 'M':
        print('OPÇÃO ERRADA. DIGITE NOVAMENTE!')
    else:
       print('SEXO VALIDADO!')
