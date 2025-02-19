from abc import ABC, abstractmethod
import os
os.system("cls || clear")

class Endereco:
    def __init__(self, longradouro: str, numero: int, complemento: str, cep: str, cidade: str) -> None:
        self.longradouro = longradouro
        self.numero = numero
        self.complemeto = complemento
        self.cep = cep
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"\nLongradouro: {self.longradouro}"
                f"\nNumero: {self.numero} "
                f"\nComplemento: {self.complemeto} "
                f"\nCEP: {self.cep} "
                f"\nCidade: {self.cidade}")

class Funcionario(ABC):
    # Constructor
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

    def calcular_salario():
        pass

    def __str__(self) -> str:
        return (f"Nome: {self.nome}" 
                f"\nTelefone: {self.telefone}" 
                f"\nEmail: {self.email}" 
                f"\nSálario: {self.salario_final()}"
                f"\n-- ENDEREÇO -- {self.endereco}")

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crea: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        return 2000.0
    
        # Acrescimo de 20%
        # BONIFICACAO = 1.2
        # salario_final = self.salario * BONIFICACAO
        # return salario_final

    # def __str__(self) -> str:
    #     return (f"super().__str__()"
    #             f"\nSalario: {self.salario_final}")

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm: str, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
    
    def salario_final(self) -> float:
        return 5000.0
        # Acrescimo de 20%
        # BONIFICACAO = 1.2
        # salario_final = self.salario * BONIFICACAO
        # return salario_final

    # def __str__(self) -> str:
    #     return (f"super().__str__()"
    #         f"\nSalario: {self.salario_final}")

     
# Instanciando classes
print("*== Dados do engenheiro ==*")
engenheiro_1 = Engenheiro("joana", "7199999-9999", "joana@gmail.com", "12345678900", Endereco("Rua a", 99, "casa 1", "45.666-000", "xique-xique"))

print(engenheiro_1)

print("\n*== Dados do médico ==*")
medico_1 = Medico("Jose", "7199999-9999", "JOSE@GMAIL.COM", "12345678900", Endereco("Rua B", 55, "Estrada 55", "42200-000", "xique-xique"))
print(medico_1)