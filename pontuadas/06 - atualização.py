"""
- BIBLIOTECAS
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

- FUNÇÃO PARA CALCULAR MÉDIA
float calcularMedia(float notas[]) {
	int i;
	float soma = 0;
	for(i = 0; i < TAM; i++) {
		soma += notas[i];
	}
	return soma / TAM;
}

- FUNÇÃO PARA VERIFICAR SITUAÇÃO
char* verificarSituacao(float media) {
	char* resultado[200];
	media >= 7 ? strcpy(resultado, "Aprovado!") : strcpy(resultado, "Reprovado!");
	return resultado;
}

- FUNÇÃO PARA MOSTRAR RESULTADO
void mostrarResultado(float notas[]) {
	printf("\nMédia: %.1f \n", calcularMedia(notas));
	printf("Resultado: %s \n", verificarSituacao(calcularMedia(notas)));
}

int main() {
	setlocale(LC_ALL, "");
	
	float notas[TAM];
	int i;
	
	for(i = 0; i < TAM; i++) {
		printf("Digite a %dª nota: ", i + 1);
		scanf("%f",&notas[i]);
	}

	mostrarResultado(notas);
	
	return 0;
}
"""

import os

#limpa tela
def limpa():
    os.system("clear")

#define TAM 3 (CONSTANTE)
TAM = 3

#função calcular media
def calcular_media(notas):
    soma = 0
    for i in range(TAM):
        soma += notas[i]
    return soma / TAM

#função verificar situacao
def verificar_situacao(media):
    resultado : str
    if media >= 7:
        resultado = "Aprovado!"
    else:
        resultado = "Reprovado"
    return resultado

#função mostrar resultado
def mostrar_resultado(notas):
    media = calcular_media(notas)
    print(f"Média:{media}")
    print(f"Resultado:{verificar_situacao(media)}")

#codigo principal
notas = []

for i in range(TAM):
    nota = float(input(f"Informe a {i+1}ª nota: "))
    notas.append(nota)
    
mostrar_resultado(notas)











