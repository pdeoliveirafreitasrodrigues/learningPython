"""
Tipo String

Em Python, um dado é considerado do tipo String sempre que:

- Estiver entre aspas simples -> 'uma  string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma  string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma  string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'Geek University'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJolie'
print(nome)
print(type(nome))

nome = "Angelina \" Jolie"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) #Transforma em uma lista de Strings
"""
# - Estiver entre aspas duplas triplas -> """uma  string""", """234""", """a""", """True""", """42.3"""

""" Quando se cria uma String em Python ele faz:

Pos:  0    1    2    3    4    5    6    7    8    9    10   11   12   13   14
    ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']
    
    Isso é o mesmo que Geek University.
    
    
    
print(nome[0:4]) # Slice de String
print(nome[5:15]) # Slice de String

# [  0,         1      ]
# ['Geek', 'University']
print(nome.split()[0])

print(nome.split()[1])     
"""
nome = 'Geek University'

"""
[::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta
"""
print(nome[::-1]) # Inversão da String (método super Pythônico)

print(nome.replace('e', 'i'))
print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)
print()
print(texto[::-1])