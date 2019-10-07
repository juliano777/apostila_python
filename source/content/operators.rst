# https://www.tutorialspoint.com/python/bitwise_operators_example

# Operadores bit a bit / Python Bitwise


# Operadores Lógicos OR (|) e AND (&)

'''
    Pipe (|) e ampersand (&) são operadores lógicos, utilizados respectivamente para as lógicas or e and.
'''    


# Operador pipe "|": Ou Binário / Binary Or

'''
    O operador pipe faz a lógica "or" binária, em português "ou".

    Dada a seguinte tabela da verdade em que;
    
    0 = False
    1 = True

    Observe os resultados e em seguida via statements Python: 

+----+---+---+
| OR | 0 | 1 |
+----+---+---+
|  0 | 0 | 1 |
+----+---+---+
|  1 | 1 | 1 |
+----+---+---+

'''    

False | False
False

False | True
True

True | False
True

True | True
True






# 0010 | 0001 = 0011 -> 2 | 1 = 3

2 | 1
3

'''
0010
ou
0001
-------
0011
'''


# 1010 | 0011 = 1011 -> 10 | 3 = 11

10 | 3
11


# Operador ampersand "&": E Binário / Binary And

'''
    O operador ampersand faz a lógica "and" binária, em português "e".

    Como vimos nos exemplos anteriores, mas agora com a lógica and, observe os resultados e em seguida via statements Python: 



+-----+---+---+
| AND | 0 | 1 |
+-----+---+---+
|  0  | 0 | 0 |
+-----+---+---+
|  1  | 0 | 1 |
+-----+---+---+

''' 



False & False
False

False & True
False

True & False
False

True & True
True


# 0010 & 0001 = 0000 -> 2 & 1 = 0

2 & 1
0


# 1010 & 0011 = 0010 -> 10 & 3 = 2

10 & 3
2



## Operador ampersand "^": Ou Exclusivo Binário / Binary XOr


















# Deslocamento de Bits / Bit Shift


False >> False
0

False >> True
0

True >> False
1

True >> True
0









