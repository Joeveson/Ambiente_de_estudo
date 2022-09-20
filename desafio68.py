# Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de 0 vitórias consecutivas que ele conquistou no final do jogo. 

from random import randint

print('-=-'*12)
print('\033[1;31mSISTEMA:\033[m VAMOS JOGAR PAR OU ÍMPAR ? ')
print('-=-'*12)
cont = 0

while True:
    escolha = randint(0,10)

    num = int(input('\033[1;33mDigite um número.\033[m OBS: Rage de 0 a 10: '))
    selecione = str(input('Impar ou Par:').upper())
    result = num + escolha
    print(f'O número escolhido pelo sistema foi {escolha}.')
    print(f'A soma dos valores foram {result}.')
    if result%2 == 0:
       print(f'A soma dos valores deram PAR!')
    else:
        print(f'A soma dos valores deram IMPAR!!')

    if result%2 == 0:       
        if selecione == 'PAR':
            print('Você Ganhou!')
        
        else:
            print('O Sistema Ganhou!')
            break
    else:
        if selecione == 'IMPAR':
            print('Você Ganhou!')
        else:
            print('O sistema ganhou!')
            break

    cont = cont +1
print(f'Você teve o total de {cont} vitórias.')