# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Informe o nome da cidade: ').strip().upper())
compara = 'SANTO' in cidade
print (f'A cidade começa com SANTO? {compara}.')