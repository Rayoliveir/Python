"""
Descrição das variáveis:
  - quantidade_pares: Quantidade de números pares.
  - quantidade_impares: Quantidade de números ímpares.
  - quantidade_positivos: Quantidade de números positivos.
  - quantidade_negativos: Quantidade de números negativos.
  - maior_numero: O maior número.
  - menor_numero: O menor número.
  - media_pares: Média dos números pares.
  - media_impares: Média dos números ímpares.
  - media_geral: Média de todos os números.
  - numeros_invertidos: Os números na ordem inversa.
"""

QTD = 5

# Variáveis para armazenar as estatísticas
quantidade_pares = 0
quantidade_impares = 0
quantidade_positivos = 0
quantidade_negativos = 0
maior_numero = float('-inf')
menor_numero = float('inf')
soma_pares = 0
soma_impares = 0
soma_geral = 0
numeros = []

for i in range(QTD):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)
    
    # Processando cada número
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
        soma_impares += numero

    if numero > 0:
        quantidade_positivos += 1
    elif numero < 0:
        quantidade_negativos += 1

    maior_numero = max(maior_numero, numero)
    menor_numero = min(menor_numero, numero)

    soma_geral += numero
    
if quantidade_pares == 0:
    print("Não foram informados números pares!")
if quantidade_impares == 0:
    print("Não foram informados números impares")

# Calculando as médias
media_pares = soma_pares / quantidade_pares if quantidade_pares !=0 else 0
media_impares = soma_impares / quantidade_impares if quantidade_impares != 0 else 0
media_geral = soma_geral / QTD

# Imprimindo as estatísticas
print("\n")
print("*" * 43)
print("======= ESTATÍSTICAS DOS NÚMEROS ========")
print("\nQuantidade de números inseridos: {}".format(QTD))
#print("\n")
print("============ PARES E IMPARES ============")
print("Quantidade de pares: {}".format(quantidade_pares))
print("Quantidade de ímpares: {}".format(quantidade_impares))
print("========= POSITIVOS E NEGATIVOS =========")
print("Quantidade de positivos: {}".format(quantidade_positivos))
print("Quantidade de negativos: {}".format(quantidade_negativos))
print("============= MAIOR E MENOR =============")
print("Maior número: {}".format(maior_numero))
print("Menor número: {}".format(menor_numero))
print("================ MÉDIAS =================")
print("Média geral: {}".format(media_geral))
print("Média de pares: {}".format(media_pares))
print("Média de impares: {}".format(media_impares))
print("============= LISTA INVERSA =============")
print("Numeros na ordem inversa: {}".format(numeros[::-1]))
print("*" * 43)
