import os
os. system("cls || clear")

print(" === Solicitando dados === \n")
primeiroNumero = int(input("Digite o primeiro numero: "))
segundoNumero = int(input("Digite o segundo numero: "))

soma = primeiroNumero + segundoNumero
subtacao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

print(" === Exibindo resultados === \n")
print(f"Primeiro numero: {primeiroNumero}")
print(f"Segundo numero: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Subtração: {subtacao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")