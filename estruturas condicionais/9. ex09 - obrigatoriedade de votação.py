import os
os.system("cls || clear")

nome = input("Informe seu nome: ")
idade = int(input("Informe sua idade: "))

if idade < 18 and idade > 65:
    print("Não é obrigato a votar")
else: 
    print("É obrigado a votar")
