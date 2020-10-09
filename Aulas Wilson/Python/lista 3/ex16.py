print('Informe a idade do(a) aluno(a): ')
idades = []
idade = 0
continua = 1
cont = 0
maioridade = 0
menoridade = 0

while continua == 1 :
    
    cont = cont + 1
    idade = (int(input(f'Informe a {cont} idade: ')))
    idades.append(idade)

    if(idade > 18):
      maioridade = maioridade + 1

    elif(idade <= 18):
      menoridade = menoridade + 1

    continua = int(input('Deseja inserir outra idade? [1 = sim] [0 = nao]: '))



print(f'O aluno mais novo tem {min(idades)} e o aluno mais velho tem {max(idades)}')
print(f'{maioridade} alunos sao maiores de idade e {menoridade} sao menores de idade.')
print('A media de idade dos alunos é: {:.2f}'.format((sum(idades)/len(idades))))