"""
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import requests

cep = input("Digite o CEP (somente números): ")

url = f"https://viacep.com.br/ws/{cep}/json/"

try:
    resposta = requests.get(url, timeout=5)

    if resposta.status_code == 200:
        dados = resposta.json()

        if "erro" in dados:
            print("CEP não encontrado.")
        else:
            logradouro = dados.get("logradouro", "Não informado")
            bairro = dados.get("bairro", "Não informado")
            cidade = dados.get("localidade", "Não informado")
            estado = dados.get("uf", "Não informado")

            print(f"Logradouro: {logradouro}")
            print(f"Bairro: {bairro}")
            print(f"Cidade: {cidade}")
            print(f"Estado: {estado}")
    else:
        print("Falha na consulta do CEP. Código de status:", resposta.status_code)

except requests.exceptions.RequestException:
    print("Falha na conexão com a API do CEP.")
