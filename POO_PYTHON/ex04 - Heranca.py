from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Funcionario(ABC):
    # Contructor
    def __init__(self, nome: str, idade: int, salario: float) -> None:
        self.nome = nome
        self.idade = idade
        self.salario = salario
    
    @abstractmethod
    def calcular_salario(self) -> float:
        pass

class Gerente(Funcionario):
    def calcular_salario(self) -> float:
        # Acrescimo de 20%
        BONIFICACAO = 1.2
        salario_final = self.salario * BONIFICACAO
        return salario_final
    # Subtraindo pr dps somar
        # BONIFICACAO = 0.2
        # salario_final = self.salario * BONIFICACAO
        # salario_final += self.salario
        # return salario_final

class Motoboy(Funcionario):
    def __init__(self, nome: str, idade: int, salario: float, cnh: str) -> None:
        super().__init__(nome, idade, salario)
        self.cnh = cnh

    def calcular_salario(self) -> float:
        # Acrescimo de 10%
        BONIFICACAO = 1.1
        salario_final = self.salario * BONIFICACAO
        return salario_final

# Instanciar classes

gerente1 = Gerente("Marcos", 35, 2000.0)
print("*== GERENTE ==*")
print(f"Nome: {gerente1.nome}")
print(f"Idade: {gerente1.idade}")
print(f"Salario: {gerente1.calcular_salario()}")

motoboy1 = Motoboy("Junior", 25, 2000.0, "1234567890")
print("*== MOTOBOY ==*")
print(f"Nome: {motoboy1.nome}")
print(f"Idade: {motoboy1.idade}")
print(f"Salario: {motoboy1.calcular_salario()}")
