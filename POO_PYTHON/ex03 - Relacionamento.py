import os
os.system("cls || clear")

class Endereco:
    def __init__(self, longradouro: str, numero: int) -> None:
        self.longradouro = longradouro
        self.numero = numero

    def exibir_endereco(self) -> str:
            return f"\nLongradouro: {self.longradouro} \nNumero: {self.numero}"

class Aluno:
    # nome, idade
    #contructor
    def __init__(self, nome: str, idade: int, endereco: Endereco) -> None:
        # Atributos
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def exibir_dados(self) -> str: 
        return f"Nome: {self.nome} \nIdade: {self.idade} \nEndereço: {self.endereco.exibir_endereco()}"
    
    
aluno1 = Aluno("Marta", 22, Endereco("Rua A", 22))

print(aluno1.exibir_dados())
