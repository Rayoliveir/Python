#Importando bibliotecas
import os
import math

#logo que limpa a tela
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

#calcula o imc
def calcular_imc(peso, altura):
    return peso / math.pow(altura, 2)

#IF-ELSE para decidir sutuação
def resultado_imc(imc):
    if imc < 18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado

#classe 
class Dados_usuario:
    def __init__(self, nome_usuario, sobrenome_usuario, idade_usuario, altura_usuario, peso_usuario):
        self.nome = nome_usuario
        self.sobrenomes = sobrenome_usuario
        self.idades = idade_usuario
        self.alturas = altura_usuario
        self.pesos = peso_usuario
        
imcs = []
dados = []
resultados_imcs = []
nomes_completos = []

while True:
    #solicitando dados pro usuario
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    #parando o laço caso o usuario queira
    if nome.lower() == 'sair':
        break
    
    #continuando a solicitação de dados
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    #colocando os dados dentro da class
    dados.append(Dados_usuario(nome, sobrenome, idade, altura, peso))

    #juntando o nome com o sobrenome em um vetor
    nomes_completos.append(nome + " " + sobrenome)
    
    #chamando função de calculo de imc
    imc = calcular_imc(peso, altura)
    
    #declarando imc como vetor
    imcs.append(imc)
    
    #chamando função do resultado da situação
    resultados_imcs.append(resultado_imc(imc))

#exibindo os dados do usuario
logoSenai()
print("\n=========== DADOS DO USUÁRIO ========== \n")
for i, dado in enumerate(dados):
    print(f"Usuário {i+1}")
    print(f"Nome: {dado.nome}")
    print(f"Sobrenome: {dado.sobrenomes}")
    print(f"Nome completo: {nomes_completos[i]}")
    print(f"Idade: {dado.idades}")
    print(f"Altura: {dado.alturas} metros")
    print(f"Peso: {dado.pesos} quilogramas")
    print(f"IMC:", imcs[i])
    print(f"Resultado:", resultados_imcs[i])
    print("\n")

#Importando bibliotecas
import os
import math

#logo que limpa a tela
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

#calcula o imc
def calcular_imc(peso, altura):
    return peso / math.pow(altura, 2)

#IF-ELSE para decidir sutuação
def resultado_imc(imc):
    if imc < 18.5:
        resultado = "Muito magro"
    elif imc < 25:
        resultado = "Peso normal"
    elif imc < 30:
        resultado = "Sobrepeso"
    elif imc < 35:
        resultado = "Obesidade grau I"
    elif imc < 40:
        resultado = "Obesidade grau II"
    else:
        resultado = "Obesidade grau III (mórbida)"

    return resultado

#classe 
class Dados_usuario:
    def __init__(self, nome_usuario, sobrenome_usuario, idade_usuario, altura_usuario, peso_usuario):
        self.nome = nome_usuario
        self.sobrenomes = sobrenome_usuario
        self.idades = idade_usuario
        self.alturas = altura_usuario
        self.pesos = peso_usuario
        
imcs = []
dados = []
resultados_imcs = []
nomes_completos = []

while True:
    #solicitando dados pro usuario
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    #parando o laço caso o usuario queira
    if nome.lower() == 'sair':
        break
    
    #continuando a solicitação de dados
    sobrenome = input("Digite o sobrenome do usuário: ")
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    #colocando os dados dentro da class
    dados.append(Dados_usuario(nome, sobrenome, idade, altura, peso))

    #juntando o nome com o sobrenome em um vetor
    nomes_completos.append(nome + " " + sobrenome)
    
    #chamando função de calculo de imc
    imc = calcular_imc(peso, altura)
    
    #declarando imc como vetor
    imcs.append(imc)
    
    #chamando função do resultado da situação
    resultados_imcs.append(resultado_imc(imc))

#exibindo os dados do usuario
logoSenai()
print("\n=========== DADOS DO USUÁRIO ========== \n")
for i, dado in enumerate(dados):
    print(f"Usuário {i+1}")
    print(f"Nome: {dado.nome}")
    print(f"Sobrenome: {dado.sobrenomes}")
    print(f"Nome completo: {nomes_completos[i]}")
    print(f"Idade: {dado.idades}")
    print(f"Altura: {dado.alturas} metros")
    print(f"Peso: {dado.pesos} quilogramas")
    print(f"IMC:", imcs[i])
    print(f"Resultado:", resultados_imcs[i])
    print("\n")

