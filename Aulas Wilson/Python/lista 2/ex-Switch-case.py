def nomeMes(numeroDoMes):
  batatinha = {
    1: "jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
  }
  return batatinha.get(numeroDoMes, "ivalido!")

num = int(input("Informe o número: "))

print(f"O mês é {nomeMes(num)}")