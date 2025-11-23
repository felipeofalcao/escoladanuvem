"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

print("Operações disponíveis: +  -  *  /")

num1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação desejada: ")
num2 = float(input("Digite o segundo número: "))

if operacao == "+":
    resultado = num1 + num2
    print(f"Resultado: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"Resultado: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"Resultado: {resultado}")
elif operacao == "/":
    if num2 == 0:
        print("Erro: divisão por zero.")
    else:
        resultado = num1 / num2
        print(f"Resultado: {resultado}")
else:
    print("Operação inválida.")
