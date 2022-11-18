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