import os
os.system("cls || clear")

soma: int = 00
qtdNumeros = 0

while True:
    numero = int(input('Informe um número: ')) 
   
    if numero < 0:
        break

    soma += numero
    qtdNumeros += 1
        
    
media = soma / qtdNumeros

print("Soma: {}".format(soma))
print("Média: {}".format(media))