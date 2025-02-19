import os
os.system("cls || clear")

class SalarioNegativoError(Exception):
    pass

class Endereco:
    def __init__(self, longradouro: str, numero: str, cidade: str) -> None:
        self.longradouro = longradouro
        self.numero = numero
        self.cidade = cidade

    def __str__(self) -> str:
        return (f"Longradouro: {self.longradouro}"
                f"\nNúmero: {self.numero}"
                f"\nCidade: {self.cidade}")

class Funcionario:
    def __init__(self, nome: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.email = email
        self.endereco = endereco

    def calcular_salario():
        pass
        
        
    def salario(self) -> float:
        try:
            self.__validar_salario()
        except SalarioNegativoError as error:
            return f"Error: {error}"
    
    def __validar_salario(salario_final):
        if salario_final < 0:
            raise SalarioNegativoError(f"Valor inválido.")

    def __str__(self) -> str:
        return (f"Nome: {self.nome}"
                f"Email: {self.email}"
                f"Salario: {self.salario()}"
                f"-- ENDEREÇO --: {self.endereco}")
    
class Motoboy(Funcionario):
    def __init__(self, nome: str, email: str, cnh: str, endereco: Endereco) -> None:
        super().__init__(nome, email, endereco)
        self.cnh = cnh
    
class Gerente(Funcionario):
    def __init__(self, nome: str, email: str, endereco: Endereco) -> None:
        super().__init__(nome, email, endereco)

    def salario(self) -> float:
        try:
            self.__validar_salario()
        except SalarioNegativoError as error:
            return f"Error: {error}"
    
    def __validar_salario(salario_final):
        if salario_final < 0:
            raise SalarioNegativoError(f"Valor inválido.")
        
# INSTANCIANDO CLASSES
