# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. DEPOIS MOSTRE:
# A)APENAS OS 5 PRIMEIROS COLOCADOS.
# B)OS ÚLTIMOS COLOCADOS DA TABELA
# C)UMA LISTA COM OS TIMES EM ORDEM.
# D)EM QUE POSIÇÃO NA TABELA ESTÁ O TIME DO FLAMENGO. 
print('\033[1;31m-=-\033[m'*17)
print('\033[1;33mCAMPEONATO BRASILEIRO DE FUTEBOL - SÉRIA A - 2022\033[m')
print('\033[1;31m-=-\033[m'*17)

tabela = (
'Palmeiras',
'Internacional',
'Fluminense',
'Corinthians',
'Flamengo',
'Athletico Paranaense',
'Atlético Mineiro',
'Fortaleza',
'São Paulo',
'América',
'Botafogo',
'Santos',
'Goiás',
'Red Bull Bragantino',
'Coritiba',
'Cuiabá',
'Ceará',
'Atlético',
'Avaí',
'Juventude',
)

for pos, time in enumerate (tabela):
    print (f'{pos+1}º {time}')

print('\033[1;31m-=-\033[m'*17)
print (f'\033[1;33m\nOs times Classificados para a Libertados são:\n\033[m')
print('\033[1;31m-=-\033[m'*17)
for time in tabela[0:5]:
    print(time)

print('\033[1;31m-=-\033[m'*17)
print (f'\033[1;33m\nOs times rebaixados para séria B são:\n\033[m')
print('\033[1;31m-=-\033[m'*17)
for time in tabela [-4:]:
    print(time)

print('\033[1;31m-=-\033[m'*17)
print(f'\n\033[1;33mTimes em Ordem Alfabética:\n\033[m')
print('\033[1;31m-=-\033[m'*17)
for time in sorted (tabela):
    print(time)

time_escolha = str(input('\n\033[1;33mInforme o nome do time para saber sua posição na tabela: \033[m'))
for pos, time in enumerate (tabela):
    if time_escolha not in tabela:
        print('\n\033[1;33mO time não está no Campeonato Brasileiro da Séria A - 2022\033[m')
        break

    if time == time_escolha: 
        print(f'\n\033[1;33mO time escolhido está na posição {pos+1}º\033[m')