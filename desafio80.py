# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela. 

valores = list()
for cont in range(0, 5):
    digita_valor = int(input('Digite um valor: '))
    if cont == 0 or digita_valor > valores [-1]:
       valores.append(digita_valor)
       print('Adicionado ao final da lista...')

    else:
       pos = 0
       while pos < len(valores):
              if digita_valor <= valores[pos]:
                     valores.insert(pos, digita_valor)
                     print(f'Adicionado na posição {pos} da lista...')
                     break;
              pos = pos +1


print (f'Os valores digitados em ordem foram {valores}')