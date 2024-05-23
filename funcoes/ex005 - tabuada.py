import os

def logoRay():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

def tabuada(n, limite = 10):
    for i in range(1, limite + 1):
        print(f"{n} x {i} = {n * i}")

logoRay()
n1 = int(input("Informe um número: "))

logoRay()
tabuada(n1)
