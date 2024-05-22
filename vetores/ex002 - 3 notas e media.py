import os
os.system('cls || clear')

#criando uma lista / vetor
notas = []

#solicitando 3 notas para o usuario
for i in range(3):
    nota = float(input('Informe uma nota: '))
    notas.append(nota)

media = sum(notas) / 3

#exibindo as notas para o usuario
for i in range(3):
    print('Nota: {}'.format(notas[i]))

print('Média: {}'.format(media))