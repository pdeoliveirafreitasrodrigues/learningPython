"""
Tipo Numérico

Dica importante: Se você divir um valor com "/" ele dá o resultado correto (Ex: 5 / 2 == 2.5),
                 Mas se você dividir um valor com "//" o resultado vai sempre ser um inteiro
                 (Ex: 5//2 == 2)

 4 % 2 --> Operação para saber o resto da divisão
 2 ** 8 --> Operação de potenciação (Elevação)
 num += 1 --> Variável "num" recebe ela mesma mais 1
 num -= 1 --> Variável "num" recebe ela mesma menos 1
 num *= 1 --> Variável "num" recebe ela mesma vezes 1
 num /= 1 --> Variável "num" recebe ela mesma dividida por 1
 num //= 1 --> Variável "num" recebe ela mesma dividida por 1 (Regra da "//")

 type(VARIÁVEL/VALOR) --> Mostra o tipo de dado de determinada variável ou valor/texto digitado
"""

num = 1_000_000

print(f'O Valor dentro da variável num é {num}')

print(float(num))