import os

def logoRay():
    os.system("cls || clear")
    print("===== RAY'S CODE =====")

def inflacao(valor):
    if valor < 100: 
        preco = (valor * 0.1) + valor
    elif valor >= 100:
        preco = (valor * 0.2) + valor
    return preco


logoRay()
produto = float(input("Informe o preço de um produto: "))

preco_inflacionado = inflacao(produto)

logoRay()
print("Preço a pagar: {}".format(preco_inflacionado))
print("=" * 22)