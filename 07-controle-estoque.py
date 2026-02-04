import os

os.system("cls")

qtd = int(input("Quantidade em estoque: "))

if qtd < 5:
    print("Estoque baixo!")
else:
    print("Estoque OK")