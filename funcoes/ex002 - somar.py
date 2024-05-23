import os

def logoRay():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

def somar(n1, n2):
    resultado = n1 + n2
    return resultado

logoRay()
primeiro_numero = int(input("Informe o 1º número: "))
logoRay()
segundo_numero = int(input("Informe o 2º número: "))

soma = somar(primeiro_numero, segundo_numero)

logoRay()
print("Soma: {}".format(soma))
print("=" * 22)
