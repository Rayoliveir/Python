import os

def logo():
    os.system("cls || clear")
    print("***** RAY'S CODE *****")

def tabela():
    print("""
    __________________________
    |    OPÇÃO   |   TIPO    |
    |      1     |  À VISTA  |
    |      2     |  À PRAZO  |
    __________________________
    """)


logo()
while True:
    preco_produto = float(input("Informe o preço do produto: "))
    tabela()
    forma_pagamento = int(input("Informe a formaa de pagamento: "))
    
    match(forma_pagamento):
        case 1:
            desconto = preco_produto * 0.1
            total = preco_produto - desconto

            logo()
            print("Preço do produto: {}".format(preco_produto))
            print("Forma de pagamento: À vista")
            print("Valor do desconto: {}".format(desconto))
            print("Total a pagar: {}".format(total))
            break
        case 2:
            qtd_parcelas = int(input("Informe a quantidade de parcelas: "))
            valor_parcela = preco_produto / qtd_parcelas
            
            logo()
            print("Preço do produto: {}".format(preco_produto))
            print("Forma de pagamento: À prazo")
            print("Quantidade de parcelas: {}".format(qtd_parcelas))
            print("Valor por parcelas: {}".format(valor_parcela))
            print("Total a prazo: {}".format(preco_produto))
            break
        case _:
            print("Opção inválida, tente novamente!")
            forma_pagamento = False
