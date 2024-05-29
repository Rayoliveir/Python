import os

def logo():
    os.system("cls || clear")
    print("***** RAY'S CODE *****")

def tabela():
    print("""
      ___________________________________________
      | CÓDIGO  |     PRATO      |     VALOR    |
      |   1     |    PICANHA     |   R$ 25,00   |
      |   2     |    LASANHA     |   R$ 20,00   |
      |   3     |   STROGONOFF   |   R$ 18,00   |
      |   4     | BIFE ACEBOLADO |   R$ 15,00   |
      |   5     |  PÃO COM OVO   |   R$ 5,00    |
      ___________________________________________

""")
    

while True:
    logo()   
    tabela()
    opcao = int(input("Informe uma opcão da tabela acima: "))

    match(opcao):
        case 1:
            logo()   
            print("PICANHA | R$25,00")
            break
        case 2:
            logo()   
            print("LASANHA | R$20,00")
            break
        case 3:
            logo()   
            print("STROGONOFF | R$18,00")
            break
        case 4:
            logo()   
            print("BIFE ACEBOLADO | R$15,00")
            break
        case 5:
            logo()   
            print("* PÃO COM OVO | R$5,00 * ")
            break
        case _:   
            opcao = False

print("*" * 24)