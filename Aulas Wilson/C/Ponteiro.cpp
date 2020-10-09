#include<stdio.h>
#include <stdlib.h>

//trazer pra ca a funçao de troca

//um ponteiro é um tipo de dado que recebe o endereço de memoria de uma variavel

void troca(int vlr1,int vlr2)  // Recebendo parametros por valor 
{
	int auxiliar = vlr1;
	vlr1 = vlr2;
	vlr2 = auxiliar;
}

void trocarUsandoPonteiros (int *vlr1, int *vlr2)  // Recebendo parametros por referencia 
{
	int auxiliar = *vlr1;
	*vlr1 = *vlr2;
	*vlr2 = auxiliar;
}

int main()
{
	int num1, num2;
	
	
	printf("Informe num1: ");
	scanf("%i", &num1);
	
	printf(" Informe num2: ");
	scanf("%i", &num2);
	
	printf("\n Trocando sem os ponteiros! ");
	
	troca(num1, num2);							// Enviando parametros por valor 
	printf("\n Valor de num1: %d", num1);
	printf("\n Valor de num2: %d", num2);
	printf("\n");
	printf("\n Trocando usando ponteiros! ");
	
	trocarUsandoPonteiros(&num1, &num2);		// Enviando parametros por referencia 
	printf("\n Valor de num1: %d", num1);
	printf("\n Valor de num2: %d", num2);
	
}

