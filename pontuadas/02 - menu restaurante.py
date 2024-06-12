import os
import time

def tabela_pratos():
    os.system("clear")
    print("""
    |===================================|
    |   CÓDIGO  |   PRATOS  |   PREÇOS  |
    |===================================|
    |     1     |  FEIJOADA |   60,00   |  
    |     2     |  PAELLA   |   80,00   |
    |     3     |  SUSHI    |   75,00   |
    |     4     |  CURRY    |   50,00   |
    |     5     |  MOUSSAKA |   70,00   |
    |     6     |  POUTINE  |   40,00   |
    |     7     |  TAGINE   |   90,00   |
    |===================================|
    |     0     |  ENCERRAR PEDID0      |
    |===================================|
    """)
    
def tabela_pagamento():
    os.system("clear")
    print("""
    |==========================|
    |    CÓDIGO   |    OPÇÃO   |
    |==========================|
    |       1     |   À VISTA  |
    |       2     |   À PRAZO  |
    |==========================|
    
    """)

soma = 0
pratos = []

while True:
    time.sleep(2)
    tabela_pratos()
    opcao = int(input("Informe o código do prato desejado: "))
    
    match (opcao):
        case 1:
            escolha = "FEIJOADA"
            pratos.append(escolha)
            soma += 60
            
        case 2:
            escolha = "PAELLA"
            pratos.append(escolha)
            soma += 80
        case 3: 
            escolha = "SUSHI"
            pratos.append(escolha)
            soma += 75 
        case 4: 
            escolha = "CURRY"
            pratos.append(escolha)
            soma += 50
        case 5: 
            escolha = "MOUSSAKA"
            pratos.append(escolha)
            soma += 70
        case 6: 
            escolha = "POUTINE"
            pratos.append(escolha)
            soma += 40
        case 7: 
            escolha = "TAGINE"
            pratos.append(escolha)
            soma += 90
        case 0:
            print("ENCERRANDO O PEDIDO!")
            break
        case _:
            opcao = False
            
    op1 = input("Informe se deseja adicionar mais um prato (S/N): ")
    op1 = op1.upper()
    if op1 != "S":
        break
    
while True:
    time.sleep(2)
    tabela_pagamento()
    pagamento = int(input("Informe a forma de pagamento: "))
    
    match (pagamento):
        case 1:
            pagamento = 'DINHEIRO'
            taxa = soma * 0.1
            total_final = soma - taxa
            break
        case 2:
            pagamento = 'CARTÃO'
            taxa = soma * 0.1
            total_final = soma + taxa
            break
        case _:
            pagamento = False

time.sleep(2) 
os.system("clear")
print("Pratos escolhidos: {}".format(pratos))
print("Forma de pagamento: {}".format(pagamento))
print("Preço taxado: {}".format(taxa))
print("Subtotal: {}".format(soma))
print("Total a pagar: {}".format(total_final))
