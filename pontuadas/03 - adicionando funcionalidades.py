import os

def imc(peso, altura):
    
    return peso / (altura * altura)
    
def situacao(calculo):
    if calculo >= 40:
        massa = "obesidade grau III (mórbida)"
    elif calculo >= 35:
        massa = "Obesidade grau II"
    elif calculo >= 30:
        massa = "Obesidade grau I"
    elif calculo >= 25:
        massa = "Sobrepeso"
    elif calculo >= 18.5:
        massa = "Peso normal"
    else:
        massa = "Abaixo do peso"
    
    return massa

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("===== SENAI ===== ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
sobrenomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair' :
        break
    
    sobrenome = input("Digite o sobrenome do usuario (ou digite 'sair' para encerrar): ")
    if sobrenome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    sobrenomes.append(sobrenome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)
    

# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    massa = imc(peso[i], altura[i])
    
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i], sobrenomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print("IMC: ", round(massa, 2))
    print("Situação: ", situacao(massa))
    print("\n")
