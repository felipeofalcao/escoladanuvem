"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""

senha = input("Digite uma senha: ")

tem_numero = False
for caractere in senha:
    if caractere.isdigit():
        tem_numero = True
        break

if len(senha) >= 8 and tem_numero:
    print("Senha válida!")
else:
    print("Senha INVÁLIDA. Ela deve ter pelo menos 8 caracteres e conter pelo menos um número.")
