import os

def logo():
    os.system("cls || clear")
    print("***** RAY'S CODE *****")

print(""" 
--------------------
** TABELA DE DIAS **
--------------------
**  1 - DOMINGO   **
**  2- SEGUNDA    **
**  3 - TERÇA     **
**  4 - QUARTA    **
**  5 - QUINTA    **
**  6 - SEXTA     **
********************
""")


while True:
    dia_semana = int(input("Informe um dia da semana de acordo a tabela: "))

    match(dia_semana):
        case 1:
            logo()
            print("Domingo, Final de semana!")
            break
        case 2:
            logo()
            print("Segunda-feira, Dia útil!")
            break
        case 3:
            logo()
            print("Terça-feira, Dia útil!")
            break
        case 4:
            logo()
            print("Quarta-feira, Dia útil!")
            break
        case 5:
            logo()
            print("Quinta-feira, Dia útil!")
            break
        case 6:
            logo()
            print("Sexta-feira, Dia útil!")
            break
        case 7:
            logo()
            print("Final de semana!")
            break
        case _:
            dia_semana = False
