import os
os.system("cls || clear")

soma = 0

while True:
    for i in range(2):
        nota = float(input("Informe sua nota: "))

    if nota < 0 or nota > 10:
        print("Nota inválida, informe as duas notas novamente")
    else:
        print("Nota válida")
        break

soma += nota
media = soma / i

print("Notas informadas: {}".format(nota))
print("Média: {}".format(media))