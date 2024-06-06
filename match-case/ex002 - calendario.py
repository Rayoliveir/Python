import os

def logo():
    os.system("cls || clear")
    print("***** RAY'S CODE *****")

def tabela():
    print("""
      ____________________________
      | CÓDIGO  |      MÊS       |
      |   1     |    JANEIRO     |
      |   2     |    FEVEREIRO   |
      |   3     |    MARÇO       |
      |   4     |    ABRIL       |
      |   5     |    MAIO        |
      |   6     |    JUNHO       |
      |   7     |    JULHO       |
      |   8     |    AGOSTO      |
      |   9     |    SETEMBRO    |
      |   10    |    OUTUBRO     |
      |   11    |    NOVEMBRO    |
      |   12    |    DEZEMBRO    |
      ____________________________

""")
    

while True:
    logo()
    tabela()
    opcao = int(input("Informe o número do mês desejado: "))
    
    match(opcao):
        case 1:
            logo()
            print("Janeiro")
            break
        case 2:
            logo()
            print("Fevereiro")
            break
        case 3:
            logo()
            print("Março")
            break
        case 4:
            logo()
            print("Abril")
            break
        case 5:
            logo()
            print("Maio")
            break
        case 6:
            logo()
            print("Junho")
            break
        case 7:
            logo()
            print("Julho")
            break
        case 8:
            logo()
            print("Agosto")
            break
        case 9:
            logo()
            print("Setembro")
            break
        case 10:
            logo()
            print("Outubro")
            break
        case 11:
            logo()
            print("Novembro")
            break
        case 12:
            logo()
            print("Dezembro")
            break
        case _:
            print("Opção inválida! Tente novamente.")
            opcao = False

print("*" * 22)