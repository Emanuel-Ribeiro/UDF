print('Informe o tanto de numeros desejados: ')
numeros = []
continua = 1
cont = 0

while continua == 1 :
    
    cont = cont + 1
    numeros.append(float(input(f'Informe o {cont} numero: ')))
    numeros.sort()
    continua = int(input('Deseja inserir outro numero? [1 = sim] [0 = nao]: '))

print(f'Os numeros informados foram: {numeros}') 