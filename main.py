import requests
import csv

data_inicial = "01/01/2023"
data_final = "31/12/2025"
url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json&dataInicial={data_inicial}&dataFinal={data_final}"
resposta = requests.get(url)
dados = resposta.json()

print(f"Registros coletados: {len(dados)}")

for dado in dados:
    print(f"{dado['data']} -> {dado['valor']}")


print("\nDatas com Selic acima de 14%:")
for dado in dados:
    if float(dado["valor"]) > 14:
        print(f"{dado['data']} -> {dado['valor']}%")

soma = 0
for dado in dados:
    soma += float(dado["valor"])

media = soma / len(dados)
print(f"\nMédia da Selic no período: {media:.2f}%")

headers = ["data", "valor"]

with open("selic.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(dados)
    
print("CSV exportado pra pasta.")
