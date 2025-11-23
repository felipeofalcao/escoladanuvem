"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def palindromo(texto):
    texto_normalizado = ""

    for caractere in texto:
        if caractere.isalnum():
            texto_normalizado += caractere.lower()

    return texto_normalizado == texto_normalizado[::-1]


frase = input("Digite uma palavra ou frase: ")

resultado = palindromo(frase)

if resultado:
    print("Sim")
else:
    print("Não")
