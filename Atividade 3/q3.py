"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

temp = float(input("Digite a temperatura: "))
origem = input("Unidade de origem (C, F ou K): ").upper()
destino = input("Unidade desejada (C, F ou K): ").upper()

unidades_validas = ["C", "F", "K"]

if origem not in unidades_validas or destino not in unidades_validas:
    print("Unidade inválida. Digite C, F ou K.")
else:
    # Converter origem para Celsius
    if origem == "C":
        temp_c = temp
    elif origem == "F":
        temp_c = (temp - 32) * 5/9
    else: # origem == "K"
        temp_c = temp - 273.15

    # Converter Celsius para destino
    if destino == "C":
        temp_final = temp_c
    elif destino == "F":
        temp_final = temp_c * 9/5 + 32
    else: # destino == "K"
        temp_final = temp_c + 273.15

    print(f"{temp}°{origem} equivale a {temp_final:.2f}°{destino}")
