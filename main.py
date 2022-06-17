from importandodados import *
from functions import *


start_date = 0
end_date = 0
frequency = 0

#entradas
while start_date not in dias:
        start_date = input('Start date: ')

while end_date not in dias:
    end_date = input('End date: ')
    if end_date in dias:
        if dias.index(end_date) < dias.index(start_date):
            end_date = 0

capital = float(input('Capital: '))
capital0 = capital
while frequency not in ['day', 'month', 'year']:
    frequency = input('Frequency: ')

retorno = mainfunction(start_date, end_date, capital, frequency)

with open(f'retorno/start({start_date[0:2]}-{start_date[3:5]}-{start_date[6-10]})_end({end_date[0:2]}-{end_date[3:5]}-{end_date[6-10]})_{capital0}_{frequency}.txt', 'w') as arquivo:
    arquivo.write(str(retorno))