import os

os.system("cls")

numero = int(input("Digite um número: "))

for i in range(1,11):
    print(numero, "x", i, "=", numero * i)

input("Pressione a tecla <Enter> para continuar...")