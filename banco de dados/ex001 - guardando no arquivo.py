import os
from dataclasses import dataclass

os.system("cls || clear")

#constante
QUANTIDADE_ALUNOS = 2

#classe
@dataclass
class Aluno:
    nome: str
    idade: int

alunos =[]

#solicitando dados
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite o seu nome: "),
        idade = int(input("Digite a sua idade: "))
    )
    alunos.append(aluno)

# Nome do arquivo
arquivo = 'alunos.txt'

# Grava os dados do usuario
with open(arquivo, 'w') as arquivo:
    for aluno in alunos:
        arquivo.write(f"{aluno.nome}, {aluno.idade}\n")

print(f"Dados gravados com sucesso!")
