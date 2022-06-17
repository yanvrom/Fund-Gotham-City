from importandodados import *

def calculate(capital, taxa, n):
    m = capital*(1+taxa)**n
    return m


def mainfunction(start_date, end_date, capital, frequency):
    capital0 = capital

    #infosguardadas dia, capital, ganho
    retorno = [{'Date':start_date, 'Capital':capital, 'Amount earned':0}]

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
    return retorno


#Criando função que transforma de ano-mes-dia para dia/mes/ano

def transform(data):
    listadata = data.split('-')
    ano, mes, dia = listadata
    return f'{dia}/{mes}/{ano}'