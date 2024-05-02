import os
os.system("cls || clear")
"""
Escreva um algoritmo que solicite do usuário um número e mostre a
tabuada de multiplicação do número informado.
Exemplo:
5 x 1= 5
5 x 2 = 10
5 x 3 = 15
..
5 x 10 = 50
"""

numero = int(input("Informe um número: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")