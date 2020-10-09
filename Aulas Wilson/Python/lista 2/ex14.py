import sys

print("informe a media para aprovaçao: ")
aprov = float(input())
print("informe o sexo do(a) aluno(a)")
sexo = input()

if((sexo == "M") | (sexo == "m") | (sexo == "Masculino") | (sexo == "masculino") ):
  print("informe o nome do aluno: ")
  nome = input()

elif((sexo == "F") | (sexo == "f") | (sexo == "Feminino") | (sexo == "feminino") ):
  print("informe o nome da aluna: ")
  nome = input()

if((sexo != "M") & (sexo != "m") & (sexo != "Masculino") & (sexo != "masculino") & (sexo != "F") & (sexo != "f") & (sexo != "Feminino") & (sexo != "feminino") ):
  print("Existem somente 2 generos comece novamente!")
  sys.exit()

print(f"informe a 1ª nota de {nome}")
nota1 = float(input())
print(f"informe a 2ª nota de {nome}")
nota2 = float(input())
print(f"informe a 3ª nota de {nome}")
nota3 = float(input())

media = (nota1 + nota2 + nota3)/3

if((sexo == "M") | (sexo == "m") | (sexo == "Masculino") | (sexo == "masculino") ):
  if(media >= aprov):
    print(f"O aluno {nome} foi aprovado com media {media:.2f}")

elif((sexo == "M") | (sexo == "m") | (sexo == "Masculino") | (sexo == "masculino") ):
  if(media < aprov):
    print(f"O aluno {nome} foi reprovado com media {media:.2f}")

if((sexo == "F") | (sexo == "f") | (sexo == "Feminino") | (sexo == "feminino") ):
  if(media >= aprov):
    print(f"A aluna {nome} foi aprovada com media {media:.2f}")

elif((sexo == "F") | (sexo == "f") | (sexo == "Feminino") | (sexo == "feminino") ):
  if(media < aprov):
    print(f"A aluna {nome} foi reprovada com media {media:.2f}")