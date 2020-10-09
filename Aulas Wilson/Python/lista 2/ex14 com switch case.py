import sys

print("informe a media para aprovaçao: ")
aprov = float(input())

def nome(sexo):
  switcher = {
    "M": "informe o nome do aluno:",
    "m": "informe o nome do aluno:",
    "Masculino": "informe o nome do aluno:",
    "masculino": "informe o nome do aluno:",
    "F": "informe o nome da aluna: ",
    "f": "informe o nome da aluna: ",
    "Feminino": "informe o nome da aluna: ",
    "feminino": "informe o nome da aluna: "
  }
  return switcher.get(sexo, "Sexo Invalido!")

print("informe o sexo do(a) aluno(a)")
sex = input()

print(f'{nome(sex)}')
nome = input()

print(f"informe a 1ª nota de {nome}")
nota1 = float(input())
print(f"informe a 2ª nota de {nome}")
nota2 = float(input())
print(f"informe a 3ª nota de {nome}")
nota3 = float(input())

media = (nota1 + nota2 + nota3)/3

if(media >= aprov):
  def aprovar(sexo):
    switcher = {
      "M": f"O aluno {nome} foi APROVADO com media: {media:.2f}",
      "m": f"O aluno {nome} foi APROVADO com media: {media:.2f}",
      "Masculino": f"O aluno {nome} foi APROVADO com media: {media:.2f}",
      "masculino": f"O aluno {nome} foi APROVADO com media: {media:.2f}",
      "F": f"A aluna {nome} foi APROVADA com media: {media:.2f}",
      "f": f"A aluna {nome} foi APROVADA com media: {media:.2f}",
      "Feminino": f"A aluna {nome} foi APROVADA com media: {media:.2f}",
      "feminino": f"A aluna {nome} foi APROVADA com media: {media:.2f}"
    }
    return switcher.get(sexo, "nao se aplica a nenhum caso!")

  print(f'{aprovar(sex)}')

elif(media < aprov):
  def reprovar(sexo):
    switcher = {
      "M": f"O aluno {nome} foi REPROVADO com media: {media:.2f}",
      "m": f"O aluno {nome} foi REPROVADO com media: {media:.2f}",
      "Masculino": f"O aluno {nome} foi REPROVADO com media: {media:.2f}",
      "masculino": f"O aluno {nome} foi REPROVADO com media: {media:.2f}",
      "F": f"A aluna {nome} foi REPROVADA com media: {media:.2f}",
      "f": f"A aluna {nome} foi REPROVADA com media: {media:.2f}",
      "Feminino": f"A aluna {nome} foi REPROVADA com media: {media:.2f}",
      "feminino": f"A aluna {nome} foi REPROVADA com media: {media:.2f}"
    }
    return switcher.get(sexo, "nao se aplica a nenhum caso!")

  print(f'{reprovar(sex)}')