"""Uma fruteira está vendendo frutas com a seguinte tabela de preços:
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra
ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total.
            até 5kg        acima de 5kg
morango |  R$2,50 por kg |  R$2,20 por kg
maçã    |  R$1,80 por kg |  R$1,50 por kg

Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a
quantidade (em Kg) de maçãs adquiridas e escreva o valor a ser pago pelo
cliente."""

import os
os.system("cls || clear")

print("\t===TABELA===")
print("            até 5kg         acima de 5kg ")
print("maçã    |  R$1,80 por kg |  R$1,50 por kg")
print("morango |  R$2,50 por kg |  R$2,20 por kg")
print("\n")
pesoMaca = float(input("Informe o peso de maçã(kg): "))
pesoMorangos = float(input("Informe o peso de morangos(kg): "))

if pesoMorangos < 5:
    precoMorango = 2.50
else: 
    precoMorango = 2.20

if pesoMaca < 5:
    precoMaca = 1.80
else:
    precoMaca = 1.50

pesoTotal = pesoMorangos + pesoMaca 
subTotal = (precoMorango * pesoMorangos) + (precoMaca * pesoMaca)

if pesoTotal > 8 or subTotal> 25:
    desconto = subTotal * 0.10
else:
    desconto = 0

totalPagar = subTotal - desconto
print("\n")
print(f"Peso de morangos(kg): {pesoMorangos:.2f}")
print(f"Peso de maçãs(kg): {pesoMaca:.2f}")
print(f"Peso total(kg): {pesoTotal:.2f}")
print(f"SubTotal: {subTotal:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Total a pagar: {totalPagar:.2f}")