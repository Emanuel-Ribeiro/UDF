//escreva um algoritimo que solicite ao usuario um numero inteiro positivo e ao final apresente a somatoria de todos os numeros inteiros positivos até o numero informado (ex: valor informado:4 resultado esperado: 4+3+2+1)

#include <stdio.h>
#include <conio.h>

float SomaAntecessoresNormal(int valor)
{
  int soma = 0;
  for (int i=1; i<=valor; i=i+1)
  {
    soma = soma + i;
  }
  return(soma);
}

float SomaAntecessoresRecursiva(int valor)
{
  int soma = 0;
  if (valor == 1)
    return(1);
  else
  {
    soma = valor + SomaAntecessoresRecursiva(valor-1);
    return(soma);
  }
}

int main ()
{
  float Num1, Num2;
  printf("informe o primeiro numero: ");
  scanf("%f", &Num1);

  printf("A soma dos antecessores normal é: %.2f",SomaAntecessoresNormal(Num1));
  printf("\nA soma dos antecessores recursiva é: %.2f",SomaAntecessoresRecursiva(Num1));
  getch();
}