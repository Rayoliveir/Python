import os
from dataclasses import dataclass
def logo():
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
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: ")),
        peso = float(input("Digite seu peso: ")),
        altura = float(input("Digite sua altura: "))
    )
    alunos.append(aluno)

#Exibindo dados pro usuario
logo()
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")
    print(f"peso: {aluno.peso}")
    print(f"Altura: {aluno.altura}")
