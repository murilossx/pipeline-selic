import requests

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados/ultimos/10?formato=json"
resposta = requests.get(url)
dados = resposta.json()

print(dados)