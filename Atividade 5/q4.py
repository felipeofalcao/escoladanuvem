"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""

from datetime import date

print("Digite sua data de nascimento:")
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))

data_nascimento = date(ano, mes, dia)
data_hoje = date.today()

dias_vivo = (data_hoje - data_nascimento).days

print(f"Você está vivo há {dias_vivo} dias.")
