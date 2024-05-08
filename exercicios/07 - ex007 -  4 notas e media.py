"""Escrever um programa que leia 4 notas e no final mostre a media"""
import os
os.system("cls || clear")

soma = 0 

for i in range(1, 5):
    nota = float(input("Insira a nota: "))
    soma += nota

media =  soma / i

print("Média: {}".format(media))