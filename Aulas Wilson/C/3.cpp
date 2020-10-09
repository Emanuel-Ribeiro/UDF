#include <stdio.h>
#include <conio.h>

float media (int n, float *vnotas);

int main () {
	float vnotas[10], media_notas;
	int i=0;
	for (i=0; i<10; i++) {
		printf("Digite os valores das notas: ");
		scanf("%f", &vnotas[i]);
	}
	media_notas = media(10, vnotas);
	printf("\n Media = %.1f \n", media_notas);
	getch();
}

float media (int n, float *vnotas) {
	int i=0;
	float m, soma;
	for (i=0; i<n; i++)
		soma = soma + vnotas[i];
	m = soma / n;
	return	m;
}
