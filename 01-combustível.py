import os

#Limpar tela
os.system ("cls")

#1 passo - Entrada de dados
print ("Exemplo 01- Combustível")

km = float (input ("Digite os KM percorridos: "))
litros = float (input ("Digite os Litros gastos: "))

#2 passo - Processamento (Calculos)
consumo = km / litros

#3 passo - Saída
print ("Consumo: ", consumo , "km/l")