# CRIE UM PROGRAMA QUE TENHA UM TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS). DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.

lista = ('AVIAO', 'ELEFANTE', 'BOLA', 'PEIXE', 'FUTEBOL', 'BELISCAO', 'PAPEL', 'BASQUETE', 'CONTROLE', 'TRISTE', 'GATO', 'GOLFE', 'TESOURA', 'COLHER', 'PULAR', 'GALINHA', 'SAPO', 'ESPIRITO', 'MARTELO')
vogais = 'AEIOU'

for palavra in lista:
    print (f'Na palavra {palavra} temos ' ,end='')
    for vogal in palavra:
    
        if vogal in vogais:
            print (f'{vogal} ' ,end='')
    
    print()