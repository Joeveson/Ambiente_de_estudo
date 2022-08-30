# nome = str(input('Qual é seu nome? '))
# if nome == 'Gustavo':
#     print (f'Que nome lindo você tem!')
# else:
#     print (f'Seu nome é tão normal!')
# print (f'Bom dia {nome}!')

n1 = float (input('Digite a primeira Nota: '))
n2 = float (input('Digite a segunda Nota: '))
m = (n1+n2)/2
print (f'A sua média foi {m:.1f}')
if m >= 6.0:
    print (f'Sua média foi boa! Parabéns!!!')
else:
    print (f'Sua média foi ruim! Estude mais!!!')