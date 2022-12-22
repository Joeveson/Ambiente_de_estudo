num = [2, 5, 9, 1]
num[2] = 3
num.append(7) # Adiciona o Número na Lista
num.sort() # Ordenada em forma crescente
num.sort(reverse=True) # Ordena de forma decrescente
num.insert(2, 0) # insere valores
num.pop() # elimina o ultimo valor se definir a casa é eliminado o número da casa. Exemplo num.pop(2)
num.remove(2) # elimina o número definido
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print(num)
print(f'Essa lista tem {len(num)} elementos.') # len = Quantidade de itens



valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

# valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)

# for v in valores:
#     print(f'{v}...', end='')
# print()

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista')

a = [2, 3, 4, 7]
b = a

print(f'Lista a: {a}')
print(f'Lista a: {b}')