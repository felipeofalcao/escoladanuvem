"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

quantidade = int(input("Quantos números deseja analisar? "))

pares = 0
impares = 0

for i in range(1, quantidade + 1):
    numero = int(input(f"Digite o número {i}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
