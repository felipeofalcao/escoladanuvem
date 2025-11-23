"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""

quantidade = int(input("Quantos alunos tem na turma? "))

soma = 0

for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a nota do aluno {i}: "))
    soma = soma + nota

media = soma / quantidade

print(f"A média da turma é: {media:.2f}")