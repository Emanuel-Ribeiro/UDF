#include <stdio.h>
#include <conio.h>
#include <stdlib.h>

void bubbleSort(int vetor[], int tam)
{
  int aux;

  for (int i = 0; i < tam -1; i++)
  {
    for (int j = 0; j < tam - 1 - i; j++)
    {
      if(vetor[j] > vetor[j+1])
      {
        aux = vetor[j];
        vetor[j] = vetor[j+1];
        vetor[j+1] = aux;
      }
    } 
  }
}

void imprimeFuncao(int vetor[], int tamanho)
{
  int i;

  for (i = 0; i < tamanho; i++)
    printf("%d, ", vetor[i]);
}

 int main()
{
  int menu = 1;
  int i = 0;
  int vetor[] = {};

  do
  {
    printf("Insira um valor inteiro no vetor: ");
    scanf("%d", &vetor[i]);
    i = i + 1;
    printf("Deseja inserir mais um valor? ([1]-Sim | [0]-Nao):\n");
    scanf("%d", &menu);
  } while (menu != 0);
  
  int tam = sizeof(vetor) / sizeof(vetor[0]);
  bubbleSort(vetor, tam);
  printf("Vetor ordenado: \n");
  imprimeFuncao(vetor, tam);
  return 0;
}