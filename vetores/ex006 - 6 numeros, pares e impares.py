"""
crie um programa que leia 6 números, armazenando em um vetor 
e informe quantos são pares e quantos são impares

mostre os números informados pelo usuario
"""
import os
os.system("cls || clear")

QTD = 6
pares = 0
impares = 0
numeros = []

for i in range(QTD):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

for i in range(QTD):
    print(f"{i+1}º Números: {numeros[i]}")

print("Pares: {}".format(pares))
print("Impares: {}".format(impares))