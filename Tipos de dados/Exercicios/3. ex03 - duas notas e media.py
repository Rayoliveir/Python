import os
os. system("cls || clear")

nome = str(input("Informe o nome do aluno: "))
idade = int(input("Informe sua idade: "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

soma = nota1 + nota2
media = soma / 2

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Média: {media}")