"""
4- Calculadora de Preço Total
* Desenvolva um programa que calcula o preço total de uma compra. Use as seguintes informações:

* Nome do produto: "Cadeira Infantil"
* Preço unitário: R$ 12.40
* Quantidade: 3
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

produto = "Cadeira Infantil"
preco_unitario = 12.40
qtd = 3

print(f"O produto {produto} tem o preço unitário de R$ {preco_unitario:.1f}, colocando {qtd} no carrinho o valor total fica: R$ {qtd * preco_unitario:.1f}")