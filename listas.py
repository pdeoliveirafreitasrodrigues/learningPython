"""
Listas

São como vetores ou matrizes em outras linguagens porém DINÂMICAS e podendo colocar QUALQUER tipo de dado.
"""
type([])

lista1 = [1, 99, 4, 15, 22]

lista2 = ["u", "a", "j", "q"]

lista3 = []

lista4 = list(range(11))

lista5 = list('geek university')

#checar se valores estão na lista
num = 32
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Número {num} não encontrado')

# Ordenar uma lista
lista1.sort()
print(lista1)

#Contar o número de ocorrências de um valor
