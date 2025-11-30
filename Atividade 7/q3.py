"""
3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro.
"""


def main():
    nome_arquivo = input("Informe o nome do arquivo de texto para leitura: ")

    try:
        with open(nome_arquivo, mode="r", encoding="utf-8") as f:
            for numero_linha, linha in enumerate(f, start=1):
                print(f"Linha {numero_linha}: {linha.strip()}")

    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    main()
