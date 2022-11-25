lanche = ('Hambúrguer','Suco','Pizza','Pudin','Batata')
# Tuplas são imutáveis

for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posição {cont}.')

for comida in lanche:
    print(f'Eu vou comer {comida}.')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}.')

print('Comi pra caramba! :)')


# print(sorted(lanche))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print (c)

# print (c.count(5)) MOSTRA QUANTAS VEZES APARECEU O NÚMERO 5 
# print (c.index(8)) MOSTRA A POSIÇÃO QUE APRESENTA O NÚMERO DEFINIDO

