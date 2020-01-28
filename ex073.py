'''
Desafio 073
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do brasileiro
de futebol, na ordem de colocação. Depois mostre:

A - Apenas os 5 primeiros colocados.
B - Os últimos 4 colocados da tabela
C - Uma lista com os times em ordem alfabética.
D - Em que posição na tabela está o time Chapecoense
'''


times = ('Classificação Brasileirão 2018','Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará','Vasco','Sport','América-MG','Vitória','Paraná')
print('Lista de times do Brasileirão 2018 {}'.format(times[1:]))
print('\nOs 5 primeiros colocados são: {}'.format(times[1:6]))
print('\nOs 4 últimos colocados são: {}'.format(times[17:]))
print('\nTimes em ordem alfábetica {}'.format(sorted(times)))
print('\nO Chapecoense está na {}a posição.'.format(times.index('Chapecoense')))
