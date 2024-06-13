import os

def logo():
    os.system("cls || clear")

#Constante
QUANTIDADE_ALUNOS = 2

#Vetor
nomes = []
idades = []

for i in range(QUANTIDADE_ALUNOS):
    logo()
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    nomes.append(nome)
    idades.append(idade)

#Exibindo dados pro usuario
logo()
for i in range(len(nomes)):
    print(f"Nome: {nomes[i]}")
    print(f"idades: {idades[i]}")
