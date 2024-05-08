"""3. Elabore um algoritmo para ler o nome de um aluno, sua idade e as
três notas. Calcular a média do aluno.
Caso a média do aluno seja menor que 7, o aluno está reprovado.
Mostrar: nome, idade, média e se está aprovado ou reprovado."""

import os
os. system("cls || clear")

nome = str(input("Informe o seu nome: "))
idade = int(input("Informe sua idade: "))
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
contador = 3

soma = nota1 + nota2 + nota3
media = soma / contador

print("\n")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Primeira nota: {nota1}")
print(f"Segunda nota: {nota2}")
print(f"Terceira nota: {nota3}")
print(f"Média: {media}")

print("\n")
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")