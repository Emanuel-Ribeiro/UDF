#escrever em python as seis operaçoes matematicas usando funçoes
#soma subtraçao multiplicaçao e divisao
# e as duas funçoes recursivas fatorial e exponencial
#usando for while e recursividade

escolha = int(0)
continua = int(1)

def soma(a, b):
  if (a == 0):
    print(b)
  elif (b == 0):
    print(a)
  else:
    print(f"A soma dos numeros {a} e {b} é igual a: {a + b}")

def subtracao(a, b):
  if (a == 0):
    print(b)
  elif (b == 0):
    print(a)
  else:
    print(f"A subtração dos numeros {a} e {b} é igual a: {a - b}")

def multiplicacao(a, b):
  if(a == 0):
    print(0)
  elif(b == 0):
    print(0)
  else:
    print(f"O produto dos numeros {a} e {b} é igual a: {a * b}")

def divisao(a, b):
  if(a == 0):
    print(0)
  elif(b == 0):
    print("Impossivel dividir por 0")
  else:
    print(f"A divisao dos numeros {a} e {b} é igual a: {a / b}")

def fatorial(a):
  if(a == 0):
    print(0)
  elif(a == 1):
    print(1)
  else:
    print(f"O fatorial do numero {a} é {a * fatorial(a-1)}")

def exponencial(a,b):
  if(a == 0):
    print (1)
  elif(b == 1):
    print (a)
  else:
    print(f"O numero {a} elevado a {b} é igual a: {a*exponencial(a,b -1)}")

while continua != 0:

  num = int(input("Informe a operaçao desejada: \n [1 = soma] [2 = subtração] [3 = multiplicação] [4 = divisão] [5 = fatorial] [6 = exponencial]: "))

 
  a = float(input("informe o primeiro numero: "))
  if (num != 5):
    b = float(input("\ninforme o segundo numero: "))

  if __name__ == "__main__":
    switch = {
        1: soma,
        2: subtracao,
        3: multiplicacao,
        4: divisao,
        5: fatorial,
        6: exponencial
    }

    case = switch.get(num)
    if(num != 5):
      case(a,b)
    elif(num == 5):
      case(a)
  
  continua = int(input("\nDeseja continuar? [1=sim] [0=não]: "))

print("Você escolheu sair!")