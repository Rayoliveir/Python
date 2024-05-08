import os
os.system("cls || clear")

soma = 0
numero = -1
contador = 0

numero= int(input("Informe um número: "))

while numero > 0:
    numero= int(input("Informe um número: "))
    soma += numero
    contador = contador + 1


media = soma / contador

print("Soma: {}".format(soma))
print("Média: {}".format(media))