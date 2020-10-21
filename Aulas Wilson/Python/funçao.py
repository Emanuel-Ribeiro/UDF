#escrever em python as seis operaçoes matematicas usando funçoes
#soma subtraçao multiplicaçao e divisao
# e as duas funçoes recursivas fatorial e exponencial
#usando for while e recursividade

escolha = int(0)
continua = int(1)

def soma(num1, num2):
  if (num1 == 0):
    return(num2)
  elif (num2 == 0):
    return(num1)
  else:
    return(num1 + num2)

def subtracao(num1, num2):
  if (num1 == 0):
    return(num2)
  elif (num2 == 0):
    return(num1)
  else:
    return(num1 - num2)

def multiplicacao(num1, num2):
  if(num1 == 0):
    return(0)
  elif(num2 == 0):
    return(0)
  else:
    return(num1 * num2)

def divisao(a, b):
  if(a == 0):
    print("0")
  elif(b == 0):
    print("Impossivel dividir por 0")
  else:
    print(f"A divisao dos numeros {a} e {b} é igual a: {a / b}")

while continua != 0:

  num = int(input("Informe a operaçao desejada: \n [1 = soma] [2 = subtração] [3 = multiplicação] [4 = divisão] [5 = fatorial] [6 = exponencial]: "))

  a = float(input("informe o primeiro numero: "))
  b = float(input("\ninforme o segundo numero: "))

  if __name__ == "__main__":
    switch = {
        1: soma,
        2: subtracao,
        3: multiplicacao,
        4: divisao
    }

    case = switch.get(num)
    case()

  soma(a,b)
  subtracao(a,b)
  multiplicacao(a,b)
  divisao(a,b)

  print("Deseja continuar? [1=sim] [0=não]")
  continua = int(input("\nDeseja continuar? [1=sim] [0=não]: "))