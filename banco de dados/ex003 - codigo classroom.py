import os
from dataclasses import dataclass

os.system("cls || clear")

# Grava os dados no arquivo
def salvar(lista):
    nome_arquivo = 'alunos.txt'
    with open(nome_arquivo, 'w') as arquivo:
        for aluno in lista:
            arquivo.write(f"{aluno.nome},{aluno.idade}\n")
    print(f"Dados gravados com sucesso.")


# Lendo os dados no arquivo
def ler_dados_alunos(lista):
    arquivo_origem = 'alunos.txt'
    listaAlunos = []
   
    with open(arquivo_origem, 'r') as arquivo:
        for linha in arquivo:
            nome, idade = linha.strip().split(',')
            listaAlunos.append(Aluno(nome=nome, idade=int(idade)))

    print("\nExibindo dados.")
    for i in listaAlunos:
        print(f"Nome: {i.nome}")
        print(f"Idade: {i.idade}")
        print()

def deletar_usuario(lista, usuario):
    for aluno in lista:
        if usuario == aluno.nome:
            lista.remove(aluno)
            salvar(lista)
            return
    print("Usuário não encontrado.")

QUANTIDADE_ALUNOS = 2

@dataclass
class Aluno:
    nome: str
    idade: int

alunos = []

print("Solicintando dados.")
for i in range(QUANTIDADE_ALUNOS):
    aluno = Aluno(
        nome = input("Digite seu nome: "),
        idade = int(input("Digite sua idade: "))
    )
    alunos.append(aluno)
    print()

salvar(alunos)

ler_dados_alunos(alunos)

nome_usuario_excluir = str(input("Digite o nome do aluno que deseja excluir: "))
deletar_usuario(alunos, nome_usuario_excluir)

ler_dados_alunos(alunos)