"""
Escopo de Variáveis

Dois casos de escopo:

1 - Variáveis Globais;
    - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o programa.

2 - Variáveis Locais;
    - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
    está limitado ao bloco onde foi declarada.

Para declarar variáveis em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. Isso significa que
ao declararmos uma variável, nós não colocamos o tipo de dado dela.
Este tipo é inferido ao atribuirmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

# Exemplo em Python:
numero = 42  # Exemplo de variável global
print(f'A variável numero tem o valor: {numero}')
print(f'O tipo da variável numero é: {type(numero)}')

print()

numero = 'Geek'
print(f'A variável numero tem o valor: {numero}')
print(f'O tipo da variável numero é: {type(numero)}')

numero = 2

if numero > 10:
    novo = numero + 10 # Exemplo de variável local, pois está sendo criada dentro do bloco do 'if'
    print(novo)

print(novo)