# DESAFIO 19 - Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
alu = (input('Informe o nome do Primeiro Aluno: '), input('Informe o nome do Segundo Aluno: '), input('Informe o nome do Terceiro Aluno: '),input('Informe o nome do Quarto Aluno: '))
ler = random.choice(alu)
print (f'O aluno selecionado foi {ler}.')