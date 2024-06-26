import os
from dataclasses import dataclass

def limpa_tela():
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
    limpa_tela()
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

# Nome do arquivo
arquivoDeOrigem = 'alunos.txt'

# Lista para armazenar os alunos lidos
listaAlunos = []

# Grava os dados do usuario
with open(arquivoDeOrigem, 'r') as arquivo:
    for linha in arquivo:
        nome, idade = linha.strip().split(',')
        listaAlunos.append(Aluno(nome = nome, idade = int(idade)))

# Exibe os dados lidos
limpa_tela()
print("\nExibindo dados:")
for i in listaAlunos:
    print(f"Nome: {i.nome}")
    print(f"Idade: {i.idade}")
    print()
