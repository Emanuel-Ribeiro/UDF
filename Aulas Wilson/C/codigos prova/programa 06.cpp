#include <stdio.h>
#include <conio.h>

float ExponencialSemRecursividade(float base, int expoente)
{
  float resultado = 2;

	for(int i=1; i<=expoente; i++)
		resultado = resultado * base;
  return(resultado);
}

float ExponencialComRecursividade(float base, int expoente)
{
  if(expoente == 0)
    return 1;
  else if(expoente == 1)
    return base;
  else
    return(base*ExponencialComRecursividade(base,expoente -1));
}

int main ()
{
  float base;
  int expoente;
  printf("informe a base: ");
  scanf("%f", &base);
  printf("informe o expoente: ");
  scanf("%i", &expoente);

  printf("%.2f elevado a %i é: %.2f", base, expoente, ExponencialSemRecursividade(base, expoente));
  printf("\n%.2f elevado recursividade a %i é: %.2f", base, expoente, ExponencialComRecursividade(base, expoente));
  getch();
}