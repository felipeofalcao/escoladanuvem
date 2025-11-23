"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
"""

import requests

url = "https://randomuser.me/api/"

try:
    resposta = requests.get(url, timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados["results"][0]

        nome = f'{usuario["name"]["first"]} {usuario["name"]["last"]}'
        email = usuario["email"]
        pais = usuario["location"]["country"]

        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")
    else:
        print("Falha ao buscar usuário. Código de status:", resposta.status_code)

except requests.exceptions.RequestException:
    print("Falha na conexão com a API.")
