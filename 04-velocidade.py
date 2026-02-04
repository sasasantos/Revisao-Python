import os

os.system("cls")

velocidade = float(input("Velocidade do carro: "))

if velocidade > 80:
    print("Multado")
else:
    print("Dentro do limite")