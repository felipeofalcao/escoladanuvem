"""
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
"""


def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

valor = float(input("Digite o valor total da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta (ex: 10 para 10%): "))

valor_gorjeta = calcular_gorjeta(valor, porcentagem)
print(f"Valor da gorjeta: R$ {valor_gorjeta:.2f}")



