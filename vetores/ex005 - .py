import os
os.system('cls || clear')

numeros = []

while True:
    numero = float(input('digite um numero: '))
    if numero == 0:
        break
    numeros.append(numero)

maiorNumero = max(numeros)
menorNumero = min(numeros)

