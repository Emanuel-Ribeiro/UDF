numero = int(input("informe o numero de pessoas: ")) 
pessoas = []
idades = []
for c in range(1, numero+1, 1):

  print(f"insira o nome e a idade da {c}º pessoa")
  pessoas.append(input('Nome: '))
  idades.append(int(input('Idade: ')))

maior_idade = max(idades)
index = idades.index(maior_idade)

print(f"A pessoa mais velha é {pessoas[index]} com {maior_idade} anos de idade")