import os
os.system("cls || clear")

soma = 0 

for i in range(1, 4):
    nota = float(input("Insira a nota: "))
    soma += nota

media =  soma / i

if media >= 7:
    print("Aprovado")
elif media <= 4:
    print("Reprovado")
else:
    print("Recuperação")

print("Média: {}".format(media))