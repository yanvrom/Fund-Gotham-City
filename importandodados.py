import json, requests

response = requests.get("https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json&dataInicial=dd/mm/yy&dataFinal=dd/mm/yy")

dicselic = json.loads(response.text)

#mudando a base de dados para um unico dicionário em que as chaves sao as datas e as keys os valores da taxa.

selic_per_day = {}

for element in dicselic:
    selic_per_day[element['data']] = element['valor']