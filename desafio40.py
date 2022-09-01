# Crie um programa que leia duas notas de um aluno e calcula sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
med = (n1+n2)/2 
print (f'A sua média foi de {med} pontos.')

if med < 5.0:
    print('Você está REPROVADO!')
if med >= 5.0 and med < 6.9:
    print('Você está de Recuperação')
if med >= 7.0:
    print('Você está APROVADO!')