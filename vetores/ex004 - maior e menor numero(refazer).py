import os
os.system('cls || clear')

QUANTIDADE_NUMEROS = 5

num = []
maiorNum = 0
menorNum = 9999

for i in range(QUANTIDADE_NUMEROS):
    n = int(input("Informe um numero: "))
    num.append(n)

maiorNum = max(num)
menorNum = min(num)

"""
    if n > maiorNum:
        maiorNum = n
    if n < menorNum:
        menorNum = n
"""

for i, n in enumerate(num):
    print('Nota: {}'.format(num))

print('Menor numero: {}'.format(menorNum))
print('Maior numero: {}'.format(maiorNum))
