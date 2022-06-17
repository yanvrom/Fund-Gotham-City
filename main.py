from importandodados import *
from functions import calculate

start_date = input('Start date: ')

end_date = input('End date: ')

capital = float(input('Capital: '))

frequency = input('Frequency: ')

#infosguardadas dia, capital, ganho
retorno = []

capital0 = capital
if frequency == 'day':
    indiceinicial = dias.index(start_date)
    indicefinal = dias.index(end_date)
    for i in range(indiceinicial, indicefinal+1):
        capital = calculate(capital, float(taxas[i])/100, 1)
        retorno.append({'Date':dias[i], 'Capital':capital, 'Amount earned':(capital-capital0)})