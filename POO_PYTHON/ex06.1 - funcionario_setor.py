import os
from enum import Enum

def limpa():
    os.system("cls || clear")

class Sexo(Enum):
    MASCULINO = "Masculino"
    FEMININO = "Feminino"

class Setor(Enum):
    FINANCEIRO = "Financeiro"
    RECURSOS_HUMANOS = "Recursos humanos"
    VENDAS = "Vendas"
    MARKETING = "Marketing"

class Funcionario:
    def __init__(self, nome: str, idade: int, sexo: Sexo, setor: Setor) -> None:
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.setor =  setor

    def __str__(self) -> str:
        return (f"\nNome: {self.nome}"
                f"\nIdade: {self.idade}"
                f"\nSexo: {self.sexo.value}"
                f"\nSetor: {self.setor.value}")
    
# Intanciando
limpa()
funcionario_1 = Funcionario("José", 18, Sexo.MASCULINO, Setor.FINANCEIRO)

print(funcionario_1)