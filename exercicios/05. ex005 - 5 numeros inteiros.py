import os
os.system("cls || clear")

soma = 0

for i in range(1, 6):
    numero = int(input("Informe um número: "))
    soma += numero

print(f"Soma: {soma}")