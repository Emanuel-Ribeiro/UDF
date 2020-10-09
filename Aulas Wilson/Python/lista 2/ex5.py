print("insira um numero pra saber se ele é multiplo de 3: ")
num1 = int(input())
if((num1 % 3) == 0):
  print(f"O numero {num1} é multiplo de 3")
elif((num1 % 3) != 0):
  print(f"O numero {num1} não é multiplo de 3")