import os
os.system("cls || clear")

primeiroNumero = int(input("Informe o primeiro número: "))
segundoNumero = int(input("Informe o segundo número: "))
contador = 2

soma = primeiroNumero + segundoNumero
produto = primeiroNumero * segundoNumero
media = soma / contador


"""
maiorNumero = max(primeiroNumero, segundoNumero)
menorNumero = min(primeiroNumero, segundoNumero)

if primeiroNumero > segundoNumero:
    maiorNumero = primeiroNumero
else:
    maiorNumero = segundoNumero
if primeiroNumero < segundoNumero:
    menorNumero = primeiroNumero
else:
    menorNumero = segundoNumero
"""

if primeiroNumero < segundoNumero:
    menorValor = primeiroNumero
    maiorValor = segundoNumero    
else:
    maiorValor = primeiroNumero    
    menorValor = segundoNumero

print("\n")
print(f"Primeiro número: {primeiroNumero}")
print(f"Segundo número: {segundoNumero}")
print(f"Soma: {soma}")
print(f"Produto: {produto}")
print(f"Média: {media}")
print(f"Menor valor: {menorValor}")
print(f"Maior valor: {maiorValor}")