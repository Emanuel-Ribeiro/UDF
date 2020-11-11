# listas e tuplas são conjunto de dados com a diferença que
# listas [] sao mutaveis e as tuplas () sao imutaveis

lista = ['java', 'C', 'Pascal', 'Python', 'Cobol']

tupla = ('java', 'C', 'Pascal', 'Python', 'Cobol')

print(lista)
print(type(lista))
print(tupla)
print(type(tupla))

lista[1]="C++"
print(lista)
print(lista[3])# o indice cresce a partir de zero
#se o indice for positivo ele acessa o elemento de forma crescente
print(lista[-1])# o indice decresce a partir de -1
#se o indice for negativo ele acessa o elemento de forma decrescente
print(lista[-2])# o indice decresce a partir de -1 (menos um)
print(len(lista))
lista[len(lista)-1] = "Basic"
print(lista)
print(len(lista))
print(lista[2:5]) #o indice 2 inclusive e o indice 5 inclusive
print(lista[:4])  #o indice 0 inclusive e o indice 4 inclusive
print(lista[2])   #o indice 2 inclusive e todos os indices seguintes
print(lista[-3:-1]) #o indice -3 inclusive e o ultimo indice exclusive

lista2=[]

for i in lista:
    if "P" in lista:
        lista2.append(i)

if "Cobol" in lista2:
    print("tem cobol")
else:
    print("nao tem cobol")