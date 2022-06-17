from importandodados import *
from functions import calculate, mainfunction

inicio = dias.index('03/01/2000')
fim  = dias.index('31/03/2022')
diaspossiveis = dias[inicio:(fim+1)]
#Como o valor inicial do capital não importa, usarei 10000.

rendimentos = []
intervalo = []

for i in range(0, len(diaspossiveis) - 500):
    retorno = mainfunction(diaspossiveis[i], diaspossiveis[i+499], 10000, 'day')
    rendimentos.append(retorno[499]['Capital'])
    intervalo.append({'start_day':diaspossiveis[i], 'end_day':diaspossiveis[i+499]})

best = max(rendimentos)
indexmax = rendimentos.index(best)

print(f'The best window to invest: {intervalo[indexmax]}')