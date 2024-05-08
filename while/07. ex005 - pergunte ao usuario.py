import os
os.system("cls || clear")

contadorNotas = 0

soma = 0

while True:

    nota = float(input("Informe uma nota: "))
    decisao = input("Deseja inserir mais ua nota? ")

    #converte o texto em maiusculo
    resposta = resposta.upper()

    if resposta != "N":
        soma += nota
        contadorNotas += 1
    else:
        break

media = soma / contadorNotas

print("Média: {}".format(media))