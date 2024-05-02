import os
os.system("cls || clear")

pares = 0
impares = 0

for i in range(5):
    numero = int(input("Informe um número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1

print(f"Pares: {pares}")
print(f"Impares: {impares}")