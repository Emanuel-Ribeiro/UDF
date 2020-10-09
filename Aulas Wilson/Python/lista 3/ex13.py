numero_registros = int(input('Informe o numero de registros: '))

idadeHomens = []
idadeMulheres = []
somaMulheres = 0
somaHomens = 0
mediaMulheres = 0
mediaHomens = 0

for r in range(1, numero_registros+1, 1):
  
  print(f'------- {r}ª Pessoa -------')
  nome = input('Nome: ')
  sexo = input('Sexo [M/F]: ')
  if(sexo in 'mM'):
    idadeHomens.append(int(input('Idade: ')))
  if(sexo in 'Ff'):
    idadeMulheres.append(int(input('Idade: ')))

somaMulheres = sum(idadeMulheres)
mediaMulheres = somaMulheres / len(idadeMulheres)

somaHomens = sum(idadeHomens)
mediaHomens = somaHomens / len(idadeHomens)

print(f'A media de idade dos homens é de {mediaHomens} anos')
print(f'A media de idade das mulheres é de {mediaMulheres} anos')
