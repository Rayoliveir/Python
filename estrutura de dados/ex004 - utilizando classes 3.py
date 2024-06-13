import os
os.system("cls || clear")

#Constante
QUANTIDADE_ALUNOS = 2

#Classe
class Aluno:
    def __init__(self, nome_qualquer:str, idade_qualquer:int):    
        self.nome = nome_qualquer
        self.idade = idade_qualquer    

alunos = []

#Solicitando dados para o usuario
for i in range(QUANTIDADE_ALUNOS):
    nome_A = input("Digite seu nome: ")
    idade_A = int(input("Digite sua idade: "))

    alunos.append(Aluno(nome_A, idade_A,))


#Exibindo dados pro usuario
for aluno in alunos:
    print(f"Nome: {aluno.nome}")
    print(f"idade: {aluno.idade}")
