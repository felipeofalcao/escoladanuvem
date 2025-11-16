"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

produto = "Camiseta"
preco_original = 50
desconto = preco_original/100*20

print(f"O valor do produto {produto} é R$ {preco_original:.2f}, com desconto de 20% fica R$ {preco_original - desconto:.2f}")