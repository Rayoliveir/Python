import os

def logo():
    os.system("cls || clear")

class Livro:
    def __init__(self, titulo_livro: str, autor_livro:str, numero_paginas:int, preco_livro:float):
        self.titulo = titulo_livro
        self.autor = autor_livro
        self.paginacao = numero_paginas
        self.preco = preco_livro

QUANTIDADE_LIVROS = 2
livros = []

for i in range(QUANTIDADE_LIVROS):
    logo()
    titulo_do_livro = input("Informe o titulo do livro: ")
    autor_do_livro = input("informe o nome do autor do livro: ")
    numero_de_paginas = int(input("Informe a quantidade de paginas do livro: "))
    preco_do_livro = float(input("Informe o preço do livro: "))

    livros.append(Livro(titulo_do_livro, autor_do_livro, numero_de_paginas, preco_do_livro))

logo()
for i in livros:
    print(f"Título: {i.titulo}")
    print(f"Título: {i.autor}")
    print(f"Preço: {i.preco}")
    print(f"Número de paginas: {i.paginacao}")
    print("\n")
    