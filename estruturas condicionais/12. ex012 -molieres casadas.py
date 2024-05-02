import os
os.system("cls || clear")
"""
Faça um algoritmo que leia o nome, o sexo e o estado civil de
uma pessoa.
Caso sexo seja "F" e estado civil seja "CASADA", solicitar o
tempo de casada (anos).
Por fim, mostre os dados do usuário.
"""
nome = input("Infore seu nome: ")
sexo = input("Informe seu sexo(F ou M): ")
estadoCivil = input("Informe seu estado civil: ")

sexo = sexo.lower()
estadoCivil = estadoCivil.lower()

if sexo == "f" and estadoCivil == "casada":
    tempoCasada = input("Informe o tempo de casamento(anos): ")

print(f"Nome: {nome}")
print(f"Sexo: {sexo}")
print(f"Estado civil: {estadoCivil}")
print(f"Tempo de casamento(anos): {tempoCasada}") 