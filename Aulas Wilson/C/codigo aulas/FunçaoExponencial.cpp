#include <stdio.h>
#include <conio.h>

float ExponencialNormal(int base, int expoente)
{
  float i, resultado;

  resultado = base;

	for(i=0; i<(expoente-1); i++)
  {
		resultado = base * resultado;
	}
  return(resultado);
}

float ExponencialRecursiva(int base, int expoente)
{
  if(expoente == 0)
    return 1;
  else if(expoente == 1)
    return base;
  else
    return(base*ExponencialRecursiva(base,expoente -1));
}

int main ()
{
  float base, expoente;
  printf("informe a base: ");
  scanf("%f", &base);
  printf("informe o expoente: ");
  scanf("%f", &expoente);

  printf("O valor do exponencial normal é: %.2f", base, expoente, ExponencialNormal(base, expoente));
  printf("\nO valor do exponencial recursiva é: %.2f", base, expoente, ExponencialRecursiva(base, expoente));
  getch();
}