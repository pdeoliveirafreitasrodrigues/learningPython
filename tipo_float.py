"""
Tipo Float

Tipo real, decimal

Casas decimais

Separador de casas decimais na programação é "." e não a ","
"""

# Errado no ponto de vista do float, porém gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

print()

#Certo no ponto de vista do float
valor = 1.44
print(valor)
print(type(valor))

print()

# É possível realizar dupla atribuição:
valor1, valor2 = 1, 44

print(valor1)
print(type(valor1))
print()
print(valor2)
print(type(valor2))

print()

# Podemos converter um float para um int
"""
OBS: Ao converter valores de float para int nós perdemos precisão
"""
resultado = int(valor)
print(resultado)
print(type(resultado))

print()

# Podemos trabalhar com números complexos
print(f"O tipo da classe do valor 5j é: {type(5j)}")