#include <conio.h>
#include <stdio.h>
int Qtd = 1;

int SolicitaProximaIdade(int vlr)
{
  printf("Deseja informar a proxima idade? [S/N]");
  char resposta;
  scanf("%s", &resposta);
  if (resposta == 'S' || resposta == 's')
  {
    printf("Informe a idade do proximo aluno: ");
    int Age;
    scanf("%i", &Age);
    Qtd += 1;
    return(SolicitaProximaIdade(Age+vlr));
  }
  else
  {
    return(vlr);
  }
  
}

int main ()
{
  printf("Informe a idade do primeiro aluno: ");
  int idade;
  scanf("%i", &idade);
  int soma = SolicitaProximaIdade(idade);
  printf("\n As %i idades somam %i anos ea media eh: %.2f", Qtd, soma, float(soma)/Qtd);
  getch();
}