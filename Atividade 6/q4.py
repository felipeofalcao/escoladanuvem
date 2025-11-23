"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""

import requests

moeda = input("Digite o código da moeda (ex: USD, EUR): ").upper()

par = f"{moeda}-BRL"
url = f"https://economia.awesomeapi.com.br/json/last/{par}"

try:
    resposta = requests.get(url, timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()

        chave = moeda + "BRL"

        if chave in dados:
            info = dados[chave]

            valor_atual = float(info["bid"])
            maxima = float(info["high"])
            minima = float(info["low"])
            atualizacao = info["create_date"]

            print(f"Moeda: {moeda}/BRL")
            print(f"Valor atual: {valor_atual}")
            print(f"Máxima do dia: {maxima}")
            print(f"Mínima do dia: {minima}")
            print(f"Última atualização: {atualizacao}")
        else:
            print("Moeda não encontrada na API.")
    else:
        print("Falha na consulta da moeda. Código de status:", resposta.status_code)

except requests.exceptions.RequestException:
    print("Falha na conexão com a API de câmbio.")
