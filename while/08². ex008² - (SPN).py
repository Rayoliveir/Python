"""
Escreva um algoritmo que pergunte ao usuário se deseja inserir mais uma nota. Mostre um menu conforme o descrito abaixo:

S – Inserir mais uma nota;
P – Ver quantas notas foram inseridas;
N – Calcular a média aritmética das notas informadas.

O programa deve mostrar a média aritmética para o usuário.
"""

import os
import time
os.system("clear")

soma : float = 0
quantidadeNotas = 0

while True :
    print("=== MENU ===")
    print("S - Inserir uma nota")
    print("P - Ver quantas notas foram inseridas")
    print("N - Calcular média aritmética")
   
    resposta = input("Deseja inserir uma nota: ")
    resposta = resposta.upper()
   
    if  resposta == "S":
        nota = float(input("\nDigite uma nota: "))
        soma += nota
        quantidadeNotas += 1
        os.system("clear")
    elif resposta == "P":
        if quantidadeNotas == 0:
            print("Não foram inseridas notas. \n")
            time.sleep(3)
            os.system("clear")
        else:
            print(f"Quantidade de notas inseridas: {quantidadeNotas} \n")
            input("Pressione uma tecla para continuar...")
            os.system("clear")
           
    elif resposta == "N":
        if quantidadeNotas == 0:
            print("Não foram inseridas notas. \n")
            time.sleep(3)
            os.system("clear")
        else:
            break
    else:
        print("Opção inválida... \n")
        time.sleep(3)
        os.system("clear")

media  = soma / quantidadeNotas

print(f"Média: {media}")