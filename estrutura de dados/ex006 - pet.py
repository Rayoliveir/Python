"""

"""

import os

def logo():
    os.system("cls || clear")


class Pet:
    def __init__(self, nome_pet:str, raca_pet:str, idade_pet:int, porte_pet:str, alimentacao_pet:str):
        self.nome = nome_pet
        self.raca = raca_pet
        self.idade = idade_pet
        self.porte = porte_pet
        self.alimentacao = alimentacao_pet

QUANTIDADE_PET = 2
pets = []

for i in range(QUANTIDADE_PET):
    logo()
    nome_animal = input("Informe o nome do seu pet: ")
    raca_animal = input(f"Informe a raça do(a) {nome_animal}: ")
    idade_animal = int(input(f"Informe a idade do(a) {nome_animal}: "))
    porte_animal = input(f"Informe o porte do(a) {nome_animal}: ")
    alimentacao_animal = input(f"Informe a alimentação do(a) {nome_animal}: ")

    pets.append(Pet(nome_animal, raca_animal, idade_animal, porte_animal, alimentacao_animal))

logo()
for i in pets:
    print(f"Nome: {i.nome}")
    print(f"Raça: {i.raca}")
    print(f"Idade: {i.idade}")
    print(f"Porte: {i.porte}")
    print(f"Alimentação: {i.alimentacao}")
    print("\n")