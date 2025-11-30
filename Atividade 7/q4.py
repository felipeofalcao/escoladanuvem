"""
4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""

import json

def main():
    nome_arquivo = input("Informe o nome do arquivo JSON (ex: dados.json): ")

    dados = {
        "pessoas": [
            {"nome": "Ana",   "idade": 25, "cidade": "João Pessoa"},
            {"nome": "Bruno", "idade": 30, "cidade": "Campina Grande"},
            {"nome": "Carla", "idade": 22, "cidade": "Recife"},
        ]
    }

    try:
        with open(nome_arquivo, mode="w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print(f"Arquivo JSON '{nome_arquivo}' salvo com sucesso.")
    except Exception as e:
        print(f"Falha ao salvar o arquivo JSON: {e}")
        return

    try:
        with open(nome_arquivo, mode="r", encoding="utf-8") as f:
            dados_lidos = json.load(f)

        print("\nDados lidos do arquivo JSON:")
        for pessoa in dados_lidos.get("pessoas", []):
            print(f"Nome: {pessoa.get('nome')}, Idade: {pessoa.get('idade')}, Cidade: {pessoa.get('cidade')}")

    except FileNotFoundError:
        print("Erro: arquivo JSON não encontrado.")
    except json.JSONDecodeError:
        print("Falha ao ler o arquivo JSON: conteúdo inválido.")
    except Exception as e:
        print(f"Falha ao ler o arquivo JSON: {e}")

if __name__ == "__main__":
    main()
