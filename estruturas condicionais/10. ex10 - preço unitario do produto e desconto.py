"""
Faça um algoritmo para ler: a descrição do produto (nome), a quantidade adquirida
e o preço unitário.

Calcular e escrever o total (total = quantidade adquirida * preço unitário), o desconto
e o total a pagar (total a pagar = total - desconto), sabendo-se que:

- Se quantidade <= 5 o desconto será de 2%
- Se quantidade > 5 e quantidade <= 10 o desconto será de 3%
- Se quantidade > 10 o desconto será de 5%.
"""

import os
os.system("cls || clear")

nomeProduto = input("Insira o nome do produto: ") 
quantidadeAdquirida = int(input("Informe a qauntidade de produtos adquiridos:"))
precoUnitario = float(input("Informe o preço unitario do produto: "))

if quantidadeAdquirida <= 5:
    desconto = 0.02
elif quantidadeAdquirida <= 10:
    desconto = 0.03
else:
    desconto = 0.05

total = quantidadeAdquirida * precoUnitario
totalPagar = total - (total * desconto)

print(f"Nome do produto: {nomeProduto}")
print(f"Preço unitario do produto: {precoUnitario}")
print(f"Total: {total}")
print(f"Desconto: {desconto}")
print(f"Total a pagar: {totalPagar}")
