"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais
uma nota. Mostre um menu conforme o descrito abaixo:

S - Inserir mais uma nota;
P - Ver quantas notas foram inseridas;
N - Calcular a média aritmética das notas informadas.

O programa deve mostrar a média aritmética para o usuário.
"""
import os
import time  
os.system("cls || clear")

contadorNotas = 0
soma = 0

while True:
    nota = float(input("Informe uma nota: "))
    contadorNotas += 1
    soma += nota

    print("\nTabela")
    print("S - Inserir mais uma nota")
    print("P - Ver quantidade de notas inseridas")
    print("N - Calcular a media das notas informadas")
    print ("\n")

    resposta = input("Escolha uma das opções acima: ")

    #converte o texto em maiusculo
    resposta = resposta.lower()

    if resposta == "p":
        print("Notas informadas: {}".format(contadorNotas))
        break
    if resposta == "n":
        break

media = soma / contadorNotas

print("Média: {}".format(media))