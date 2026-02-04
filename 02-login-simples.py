import os

#Limpar tela
os.system ("cls")

#1 passo - Entrada de dados
print ("Exemplo 02 - Login Simples ")

usuario = input ("Digite seu usuário: ")

#2 passo - Verificar os dados
if usuario == "admin":
    senha = input ("Digite sua senha: ")

    if senha == "123":
        print ("Acesso Liberado!")
    else:
        print("Acesso Negado!")

else:
    print ("Dados Incorretos!")

print ("Fim do Programa!")
