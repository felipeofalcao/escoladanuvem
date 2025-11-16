"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

valor_total = 100.0
valor_dolar = 5.20
valor_euro = 6.15

print(f"R$ {valor_total:.2f} convertido em dólar é equivalente a U$ {valor_total/valor_dolar:.2f} e em euro € {valor_total/valor_euro:.2f}")