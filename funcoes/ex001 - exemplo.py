import os

def logosray():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

logosray()
nome = input("Informe seu nome: ")
logosray()
idade = int(input("Informe sua idade: "))
logosray()
peso = float(input("Informe seu peso: "))

logosray()
print("Nome: {}".format(nome))
print("Idade: {}".format(idade))
print("Peso: {:.2f}".format(peso))
print("=" * 22)
