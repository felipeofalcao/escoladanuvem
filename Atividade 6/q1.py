
"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
"""

import random
import string

tamanho = int(input("Digite o tamanho da senha: "))

caracteres = string.ascii_letters + string.digits + string.punctuation

senha = ""

for _ in range(tamanho):
    senha += random.choice(caracteres)

print(f"Senha gerada: {senha}")
