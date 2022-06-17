from importandodados import *
from functions import calculate
start_date = 0
end_date = 0
frequency = 0

#entradas
while start_date not in dias:
    start_date = input('Start date: ')
while end_date not in dias:
    end_date = input('End date: ')

capital = float(input('Capital: '))

while frequency not in ['day', 'month', 'year']:
    frequency = input('Frequency: ')

#infosguardadas dia, capital, ganho
retorno = [{'Date':start_date, 'Capital':capital, 'Amount earned':0}]

capital0 = capital
indiceinicial = dias.index(start_date)
indicefinal = dias.index(end_date)

if frequency == 'day':
    for i in range(indiceinicial+1, indicefinal+1):
        capital = calculate(capital, float(taxas[i])/100, 1)
        retorno.append({'Date':dias[i], 'Capital':capital, 'Amount earned':(capital-capital0)})

elif frequency == 'month':
    for i in range(indiceinicial+1, indicefinal+1):
        capital = calculate(capital, float(taxas[i])/100, 1)
        if i != indicefinal:
            if dias[i][4] != dias[i+1][4]:
                retorno.append({'Date':dias[i], 'Capital':capital, 'Amount earned':(capital-capital0)})
        else:
            retorno.append({'Date':dias[i], 'Capital':capital, 'Amount earned':(capital-capital0)})

elif frequency == 'year':
    for i in range(indiceinicial+1, indicefinal+1):
        capital = calculate(capital, float(taxas[i])/100, 1)
        if i != indicefinal:
            if dias[i][9] != dias[i+1][9]:
                retorno.append({'Date':dias[i], 'Capital':capital, 'Amount earned':(capital-capital0)})
        else:
            retorno.append({'Date':dias[i], 'Capital':capital, 'Amount earned':(capital-capital0)})

with open(f'retorno/start({start_date[0:2]}-{start_date[3:5]}-{start_date[6-10]})_end({end_date[0:2]}-{end_date[3:5]}-{end_date[6-10]})_{capital0}_{frequency}.txt', 'w') as arquivo:
    arquivo.write(str(retorno))