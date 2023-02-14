"""
Tipo Booleano

Algebra Booleana, criada por George Boole

2 constantes: Verdadeiro ou Falso

No Python -> 'True' ou 'False'

OBS: Sempre com inicial maiúscula para declarar.

Errado: true, false ||||||||| Certo: True, False

"""

ativo = False

print(ativo)

"""
Operações básicas:
"""

#  Negação (not):
"""
Fazendo a negação, se o valor for verdadeiro o resultado será falso. Se for falso, o resultado será verdadeiro.
"""
print(f'A variável ativo agora com o not está como {not ativo}!')

logado = False

#  Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores.  Ou um Ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""
print(ativo or logado)

#  E (and):
"""
Também é uma operação binária, ou seja, depende de dois valores.
Ambos os valores devem ser verdadeiros.

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""