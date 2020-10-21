#escrever em python as seis operaçoes matematicas usando funçoes
#soma subtraçao multiplicaçao e divisao
# e as duas funçoes recursivas fatorial e exponencial

def media(num1, num2):
  resposta = (num1+num2)/2
  return resposta

a = float(input("informe a primeira nota: "))
b = float(input("informe a segunda nota: "))

print(f"A media é {media(a,b)}")