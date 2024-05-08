import os
os. system("cls || clear")

QUANTIDADE_NOTAS = 3

soma = 0

for i in range(QUANTIDADE_NOTAS):
    
    while True:
        nota = float(input("Informe uma nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida, tente novamente")
        else:
            soma += nota
            break

media = soma / QUANTIDADE_NOTAS


if media >= 7:
    resultado = "Aprovado"
elif media >= 5:
    resutado = "Recuperação"
else:
    resultado = "Reprovado"

print("Média: {}".format(media))
print("{}".format(resultado))
