# DESAFIO 20 - O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada. 

import random
aluno1 = input('Informe o nome do Primeiro Aluno: ')
aluno2 = input ('Informe o nome do Segundo Aluno: ')
aluno3 = input ('Informe o nome do Terceiro Aluno: ')
aluno4 = input ('Informe o nome do Quarto Aluno: ')
list = [aluno1, aluno2, aluno3, aluno4]
ordem = random.shuffle(list)
print (f'A ordem de apresentação é: {list}.')