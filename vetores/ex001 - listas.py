import os
os.system('cls || clear')

#criando uma lista / vetor
notas = []

#solicitando 3 notas para o usuario
for i in range(3):
    nota = float(input('Informe uma nota: '))
    notas.append(nota)

#exibindo as notas para o usuario
for i in range(3):
    print('Nota: {}'.format(notas[i]))
    