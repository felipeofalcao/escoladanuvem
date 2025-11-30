"""
2 - Crie um programa que cria um arquivo  com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""


def main():
    nome_arquivo = input("Informe o nome do arquivo para salvar (ex: pessoas.txt): ")

    pessoas = [
        {"nome": "Ana",    "idade": 25, "cidade": "João Pessoa"},
        {"nome": "Bruno",  "idade": 30, "cidade": "Campina Grande"},
        {"nome": "Carla",  "idade": 22, "cidade": "Recife"},
        {"nome": "Diego",  "idade": 28, "cidade": "Natal"},
    ]

    try:
        with open(nome_arquivo, mode="w", encoding="utf-8") as f:
            f.write(f"{'NOME':20}\t{'IDADE':5}\t{'CIDADE'}\n")
            f.write("-" * 50 + "\n")

            for p in pessoas:
                f.write(f"{p['nome']:20}\t{p['idade']:5}\t{p['cidade']}\n")

        print(f"Arquivo '{nome_arquivo}' salvo com sucesso.")

    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

if __name__ == "__main__":
    main()
