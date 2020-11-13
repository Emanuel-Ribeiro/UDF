#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <time.h>

float vetor[1000];
int Qtd = 0;

int imprimeMenu() 
{
  int resposta;

  system("cls");

  printf("\n ======= EXERCICIO DE ORDENACAO ======== ");
  printf("\n =  1: Preencher o Vetor               = ");
  printf("\n =  2: Limpar o Vetor                  = ");
  printf("\n =  3: Imprimir o Vetor                = ");
  printf("\n =  4: Ordenar Buble Sort              = ");
  printf("\n =  5: Ordenar Selection Sort          = ");
  printf("\n =  6: Ordenar Insertion Sort          = ");
  printf("\n =  7: Preencher Vetor Aleatoriamente  = ");
  printf("\n =  8: Sair                            = ");
  printf("\n ======================================= ");

  printf("\n Informe a opcao desejada: ");
  scanf("%i", &resposta);
  
  return(resposta);
}

void vetorAleatorio(int Tamanho)
{
  for (int i=0; i<Tamanho; i++)
	  vetor[i] = (rand() %100);
  
  printf("\n %i numeros gerados com sucesso!",Tamanho);  // A função rand() "randomic" gera um número
                                                         // aleatório com base no DateTime do Sistema
  Qtd = Tamanho;                                         // (por isso, usar a biblioteca time.h)
  getch();
}

void bubbleSort() 
{
  float aux;

  for (int i=0; i<Qtd-1; i++)
    for (int j=0; j<Qtd-1 -i; j++)
      if (vetor[j] > vetor[j+1]) 
      {
        aux = vetor[j];
        vetor[j] = vetor[j+1];
        vetor[j+1] = aux;
      }
}

void selectionSort() 
{
  // implementar aqui o algoritmos de orden ação Selection Sort
}

void insertionSort() 
{
  // implementar aqui o algoritmos de orden ação Insertion Sort
}

void limparVetor() 
{
  for (int i=0; i<Qtd; i++)
    vetor[i] = 0;

  printf("\n Vetor zerado com sucesso! \n");
}

void imprimirVetor() 
{
  printf("\n Dados do Vetor: \n");

  for (int i=0; i<Qtd; i++)
    printf("%.2f, ", vetor[i]);

  getch();
}

int main() 
{
  char menu;
  int resposta;

  do 
  {
	resposta = imprimeMenu();
	
	if (resposta == 1) 
  {
	  do 
    {
      printf("Insira o %i. valor no vetor: ", Qtd+1);
      scanf("%f", &vetor[Qtd]);

      Qtd+=1;

      printf("Deseja inserir mais um valor? (S/N): ");
      scanf("%s", &menu);

    } while (menu == 'S' | menu == 's'); }

	else if (resposta == 2)
	  limparVetor();

	else if (resposta == 3)
	  imprimirVetor();

	else if (resposta == 4)
      bubbleSort();

	else if (resposta == 5)
      selectionSort();

	else if (resposta == 6)
      insertionSort();

	else if (resposta == 7) 
  {
    int Tamanho;

    printf("Informe o tamanho do vetor que deseja criar: ");
    scanf("%i", &Tamanho);

    vetorAleatorio(Tamanho);
  }

  } while (resposta < 8);
}