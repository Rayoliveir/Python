import os
os.system("cls || clear")

qtdSalario = 0
somaSalario = 0
mulheres5k: int = 0


idade = int(input("Informe sua idade: "))
sexo = input("Informe seu genero(M | F): ")
salario = float(input("Informe seu salario: "))

sexo = sexo.upper()

while True:
    print("\n")
    print("===== TABELA DE OPÇÕES =====");
    print("1 | Adicionar pessoa");
    print("2 | Exibir resutados e sair");
    print("\n")

    opcao = int(input("Escolha umas das opções da tabela: "))

    if opcao == 1:
        idade = int(input("Informe sua idade: "))
        sexo = input("Informe seu genero(M | F): ")
        salario = float(input("Informe seu salario: "))

        sexo = sexo.upper()

        if idade > maiorIdade:
            maiorIdade = idade
        else: 
            menorIdade = idade

        qtdSalario += 1
        somaSalario += salario

        if sexo == "f" and salario >= "5000":
            mulheres5k += 1
    
    elif opcao == 2:
        break