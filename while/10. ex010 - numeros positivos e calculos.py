import os
os.system('cls || clear')

soma = 0
pares = 0
impares = 0
qtdNumeros = 0
somaGeral = 0
numero : int = 0

while True:
    numero = int(input('Informe um número: '))
    
    if numero > 0:
        somaGeral += numero
        qtdNumeros += 1

        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    if numero == 0:
        break

mediaGeral = somaGeral / qtdNumeros

if pares != 0:
    mediaPares = soma / pares
else:
    mediaPares = 0


print('Números pares: {}'.format(pares))    
print('Números impares: {}'.format(impares))
print('Média de números pares: {}'.format(mediaPares))    
print('Média geral: {}'.format(mediaGeral))    