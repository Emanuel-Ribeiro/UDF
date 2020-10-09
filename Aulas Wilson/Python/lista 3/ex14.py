numero = []

print("informe 10 numeros reais: ")
for n in range(1,11,1):
  
  numero.append(float(input(f'{n} numero: ')))

print(f'O maior numero apresentado foi {max(numero)} e o menor foi {min(numero)}')
