operacao = input('''
Informe a operaçao matematica a ser realizada:
+ Adiçao
- Subtraçao
* Multiplicaçao
/ Divisão
** Exponenciaçao
Informe a opçao: ''')

number_1 = float(input('Informe o primeiro valor: '))
number_2 = float(input('Informe o segundo valor: '))

if operacao == '+':
  print('{} mais {} = {:.2f}'.format(number_1, number_2, (number_1 + number_2)))
elif operacao == '-':
  print('{} menos {} = {:.2f}'.format(number_1, number_2, (number_1 - number_2)))
elif operacao == '*':
  print('{} multiplicado {} = {:.2f}'.format(number_1, number_2, (number_1 * number_2)))
elif operacao == '/':
  print('{} dividido {} = {:.2f}'.format(number_1, number_2, (number_1 / number_2)))
elif operacao == '**':
  print('{} elevado {} = {:.2f}'.format(number_1, number_2, (number_1 ** number_2)))
else:
  print('O operador informado nao é valido!')       