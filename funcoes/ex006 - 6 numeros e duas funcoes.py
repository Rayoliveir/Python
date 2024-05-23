import os

def logoRay():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

def verificar_par(numeros):
    quantidade_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            quantidade_pares += 1
    return quantidade_pares

def verificar_impar(numeros):
    quantidade_impares = 0
    for numero in numeros:
        if numero % 2 != 0:
            quantidade_impares += 1
    return quantidade_impares

QTD = 6

lista_numeros = []

logoRay()
for i in range(QTD):
    numero = int(input("informe um número: "))
    lista_numeros.append(numero)

pares = verificar_par(lista_numeros)
impares = verificar_impar(lista_numeros)

logoRay()
print("Números pares: {}".format(pares))
print("Números impares: {}".format(impares))
print("=" * 22)
