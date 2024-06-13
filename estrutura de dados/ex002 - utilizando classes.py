import os
from dataclasses import dataclass
os.system("cls || clear")

#Constante
QUANTIDADE_ALUNOS = 2

#Classe
@dataclass
class Aluno:
    nome: str
    idade: int
    peso: float
    altura: float

alunos = []

#Solicitando dados para o usuario
for i in range(QUANTIDADE_ALUNOS):
    nome_A = input("Digite seu nome: ")
    idade_A = int(input("Digite sua idade: "))
    peso_A = float(input("Digite seu peso: "))
    altura_A = float(input("Digite sua altura: "))

    aluno = Aluno(nome = nome_A, idade = idade_A, peso = peso_A, altura = altura_A)
    alunos.append(aluno)

#Exibindo dados pro usuario
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")
    print(f"peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")
