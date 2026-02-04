import os

os.system("cls")

tipo = int(input("1-Carro 2-Moto 3-Caminhão: "))

if tipo == 1:
    print("Valor: R$10")
elif tipo == 2:
    print("Valor R$5")
elif tipo == 3:
    print("Valor: R$20")
else:
    print("Tipo inválido")