# Crie um programa que leia o nome completo de uma pessoa e mostre: 
# O nome com todas as letras maiúsculas
# O nome com todas as letras minúsculas
# Quantas letras ao todo (sem considerar espaços)
# Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo: ')).strip()
tamanho = nome.split() 

print (f'Nome em maiúsculas: {nome.upper()}')
print (f'Nome em minúsculas: {nome.lower()}')
print (f'O nome completo ao todo sem considerar espaço é de {len(nome) - nome.count(" ")} letras')
print (f'O primeiro nome tem {len(tamanho[0])} letras.')