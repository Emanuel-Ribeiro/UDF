numero = int(input("informe um numero: "))
soma = 0
soma = int(soma)
for i in range(1, numero, 1):
  soma = soma + i
  if(i == (numero -1)):
    print("A soma dos numeros é {} e a media dos numeros é {}".format(soma, (soma / numero)))