import os

def logo():
    os.system("cls || clear")
    print("***** RAY'S CODE *****")


resultado = False


while True:
    logo()
    a = int(input("informe o primeiro número: "))
    b = int(input("Informe o segudno número: "))
    operador = input("Digite o operador (+ - * /): ")

    match(operador):
        case '+':
            resultado = a + b
            break
        case '-':
            resultado = a - b
            break
        case '*':
            resultado = a * b
            break
        case '/':
            resultado = a / b
            break
        case _:
           operador = False
            
            
               
logo()
print(f"{a} {operador} {b} = {resultado}")
print("{} {} {} = {}".format(a, operador, b, resultado))
print("***********************")