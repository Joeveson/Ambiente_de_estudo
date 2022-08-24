# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Informe o Nome da Pessoa:').upper().strip())
compara = 'SILVA' in nome
print (f'O nome informado foi {nome}.\nO nome tem a palavra SILVA? {compara}')