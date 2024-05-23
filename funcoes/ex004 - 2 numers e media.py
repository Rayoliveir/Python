import os

def logoRay():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

def media(n1, n2):
    QTD = 2
    soma = n1 + n2
    aritm = soma / QTD
    return aritm

logoRay()
primeiro_numero = int(input("Informe o primeiro número: "))
logoRay()
segundo_numero = int(input("Informe o segundo número: "))

calculo = media(primeiro_numero, segundo_numero)

logoRay()
print("Primeiro número: {}".format(primeiro_numero))
print("segundo número: {}".format(segundo_numero))
print("Média: {}".format(calculo))