import os

def logoRay():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

def subtrair(n1,n2):
    resultado = n1 - n2
    return resultado

def multiplicar(n1,n2):
    return n1 * n2

def dividir(n1,n2):
    return n1 / n2

logoRay()
primeiro_numero = int(input("Informe o 1º número: "))
logoRay()
segundo_numero = int(input("Informe o 2º número: "))

mais = somar(primeiro_numero, segundo_numero)
menos = subtrair(primeiro_numero, segundo_numero)
vezes = multiplicar(primeiro_numero, segundo_numero)
dividido = dividir(primeiro_numero, segundo_numero)

logoRay()
print("Soma: {}".format(mais))
print("Subtração: {}".format(menos))
print("Divisão: {}".format(dividido))
print("Multiplicação: {}".format(vezes))
print("=" * 22)
