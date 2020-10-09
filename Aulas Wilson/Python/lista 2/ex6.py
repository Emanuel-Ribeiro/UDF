print("insira um numero para ser o múltiplo: ")
mult = int(input())
print(f"insira um numero pra saber se ele é multiplo de {mult}: ")
num1 = int(input())
if((num1 % mult) == 0):
  print(f"O numero {num1} é multiplo de {mult}!")
elif((num1 % mult) != 0):
  print(f"O numero {num1} não é multiplo de {mult}!")