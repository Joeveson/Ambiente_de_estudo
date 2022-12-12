# CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA. 
# NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.



print ('\033[1;33m-\033[m'*42)
print ('\033[1;31m            LISTAGEM DE PREÇOS            \033[m')
print ('\033[1;33m-\033[m'*42)

lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livros', 34.90,)


for pos, item in enumerate (lista):
    if pos % 2 == 0:
        print (f'{item:.<32}' ,end='')
    else:
        print(f'\033[1;31mR$\033[m {item:7.2f}')

print ('\033[1;33m-\033[m'*42)