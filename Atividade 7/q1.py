"""
1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. 
"""

import csv
import statistics

def main():
    nome_arquivo = input("Informe o nome do arquivo CSV: ")

    try:
        valores = []

        with open(nome_arquivo, mode="r", newline="", encoding="utf-8") as f:
            leitor = csv.DictReader(f)

            for linha in leitor:
                try:
                    valor = float(linha["tempo_execucao"])
                    valores.append(valor)
                except KeyError:
                    print("Erro: coluna 'tempo_execucao' não encontrada no arquivo.")
                    return
                except ValueError:
                    print("Aviso: valor inválido encontrado na coluna 'tempo_execucao'. Linha ignorada.")

        if not valores:
            print("Nenhum valor válido encontrado na coluna 'tempo_execucao'.")
            return

        media = statistics.mean(valores)
        desvio = statistics.stdev(valores) if len(valores) > 1 else 0.0

        print(f"Média da coluna tempo_execucao: {media:.2f}")
        print(f"Desvio padrão da coluna tempo_execucao: {desvio:.2f}")

    except FileNotFoundError:
        print("Erro: arquivo não encontrado.")
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")

if __name__ == "__main__":
    main()
