# Importando as bibliotecas:
# Bibloteca do sistema operacional:
import os 

# Importando dataclass para utilização da classe:
from dataclasses import dataclass 

#Função para limpar a tela:
# Definindo o nome da função:
def limpa_tela(): 
    # Usando a bibloteca os para limpar o terminal: 
    os.system("cls || clear") 

# Classe:
# Examina a classe para encontrar campos dentro da classe:
@dataclass 

# Definindo nome da classe:
class Cliente: 
    # Definindo o tipo da variavel nome dentro da classe:
    nome: str 
    # Definindo o tipo da variavel idade dentro da classe:
    idade: str 
    # Definindo o tipo da variavel Cpf dentro da classe:
    cpf: str 
    # Definindo o tipo da variavel CEP dentro da classe:
    cep: str
    #Definindo o tipo da variavel Endereço dentro da classe:
    endereco: str 

# Definindo função para solicitar dados do usuario:
def obter_dados():
    # Declarando a lista (clientes) para armazenar od dados do usuario:
    clientes = []

    #Iniciando um laço de repetição indeterminado:
    while True:
        #chamando a função limpa tela para limpar o terminal:
        limpa_tela()
        #Solicitando o NOME do usuario:
        nome = input("Digite o nome: ")
        #Solicitando a IDADE do usuario:
        idade = input("Digite a idade: ")
        #Solicitando o CPF do usuario:
        cpf = input("Digite o CPF: ")
        #Solicitando o CEP do usuario:
        cep = input("Digite o CEP: ")
        #Solicitando o ENDEREÇO do usuario:
        endereco = input("Digite o endereço: ")

        # Armazenando os dados da classe dentro de uma variavel: 
        cliente = Cliente(nome, idade, cpf, cep, endereco)

        # Declarando dados da variavel no vetor:
        clientes.append(cliente)

        # Verificando se o usuario deseja adicionar mais um cliente:
        continuar = input("Deseja adicionar outro cliente? (s/n): ")

        # Utilizando o operador lógico 'IF' para a verificação acima:
        if continuar.lower() != 's':
            # parando o laço de repetição caso a condição do operador lógico seja verdadeiro:
            break

    # Retornando um valor para a função obter_dados:
    return clientes

# Função para salvar os dados do usuario:
def salvar_dados(clientes):
    # Comando 'w' usado para ler o arquivo 'clientes.txt' (WRITE):
    with open("clientes.txt", "w") as arquivo:

        # Laço de repetição para ir de cliente em cientes dentro das posições do arquivo:
        for cliente in clientes:
            # Armazenando os dados (nome, idade, cpf, cep, endereço) dentro da variavel 'linha':
            linha = f"{cliente.nome},{cliente.idade},{cliente.cpf},{cliente.cep},{cliente.endereco}"
            # Declarando a organização das posições das informações dentro do arquivo:
            arquivo.write(linha + "\n")

# Função para ler os dados do usuario dentro do arquivo:
def ler_dados():
    # Comando 'r' usado para ler o arquivo 'clientes.txt' (READ):
    with open("clientes.txt", "r") as arquivo:
        # declarando variavel para ler cada linha até o final dentro do arquivo:
        linhas = arquivo.readlines()
        # Declarando 'clientes' como lista para armazenar dados:
        clientes = []

        # Laço de repetição para ir de linha em linha dentro das linhas do arquivo:
        for linha in linhas:
            # Declarando o que vai ser lido pelo laço de repetição e como vai ser separado:
            nome, idade, cpf, cep, endereco = linha.strip().split(",")
            #declarando variavel para receber a classe 'Cliente':
            cliente = Cliente(nome, idade, cpf, cep, endereco)
            # Transformando a variavel 'cliente' em uma lista:
            clientes.append(cliente)

        # Retornando um valor para a função:
        return clientes

# Declarando variavel para chamar a função 'obter_dados':
clientes = obter_dados()

# Chamando a função 'salvar_dados':
salvar_dados(clientes)

# Declarando variavel para chamar a função 'ler_dados':
clientes_lidos = ler_dados()

# Chamando função 'limpa_tela' antes de mostrar os dados do arquivo:
limpa_tela()

# Laço de repetição para mostrar as informações de cada cliente cadastrado na função 'ler_dados', que foi chamada na variavel 'clientes_lidos': 
for cliente in clientes_lidos:
    # Printando os dados de cada cliente dentro do arquivo:
    print(f"Nome: {cliente.nome}, Idade: {cliente.idade}, CPF: {cliente.cpf}, CEP: {cliente.cep}, Endereço: {cliente.endereco}")
    