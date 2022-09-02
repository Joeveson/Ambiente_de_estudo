# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

numero = int(input('Informe um número inteiro: '))
print ('1 - Binário')
print ('2 - Octal')
print ('3 - Hexadecimal')
escolha = int(input('Informe a base de conversão: '))

if escolha == 1:
    print(f'O numéro informado foi {numero}! A base de conversão informada foi Binário, sendo o valor {bin(numero)[2:]}')

elif escolha == 2:
    print(f'O numéro informado foi {numero}! A base de conversão informada foi Octal, sendo o valor {oct(numero)[2:]}')

elif escolha == 3:
     print(f'O numéro informado foi {numero}! A base de conversão informada foi Hexadecimal, sendo o valor {hex(numero)[2:]}')

else:
    print(f'O número informado não é \033[1;32mVÁLIDO!!!\033[m')
