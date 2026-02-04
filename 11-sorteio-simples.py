import os

os.system("cls")

import random

sorteado = random.randint(1,10)
palpite = int(input("Digite seu palpite: "))

if palpite == sorteado:
    print("Acertou!")
else:
    print("Errou! Número era:", sorteado)