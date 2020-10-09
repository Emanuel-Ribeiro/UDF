print("informe um numero pra sabe se ele é par ou impar: ")
num1 = int(input())
if((num1 % 2) == 0):
  print(f"O numero {num1} é par")
elif((num1 % 2) != 0):
  print(f"O numero {num1} é impar")