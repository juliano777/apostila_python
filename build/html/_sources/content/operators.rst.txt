
# https://data-flair.training/blogs/python-operator/
# https://www.tutorialspoint.com/python/bitwise_operators_example


Aritméticos
~~~~~~~~~~~

| Descrição       | Operador | Exemplo | Saída |
|-----------------|----------|---------|-------|
| Soma            | +        |  5 + 2  |  7    |
|  Subtração      | -        | 13 - 3  | 10    |
| Multiplicação   | *        | 5 * 3   | 15    |
| Divisão         | /        | 7 / 2   | 3.5   |
| Divisão Inteira | //       | 7 // 2  | 3     |
| Potenciação     | **       | 2 ** 9  | 512   |


**Soma**

+

Menor
<

Deslocamento para esquerda
<<
Subtração
-

Maior
>

Deslocamento para direita
>>
Multiplicação
*

Menor ou igual
<=

E bit-a-bit (AND)
&

Divisão
/

Divisão Inteira
//


>>> 7 / 2
3.5
>>> 7 / 2.0
3.5
>>> 7 // 2.0
3.0
>>> 7 // 2
3




Maior ou igual
>=

Ou bit-a-bit (OR)
|


Igual
==

Ou exclusivo bit-a-bit (XOR)
^
Módulo
%

Diferente
!=

Inversão (NOT) 
~
Potência
**



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



Atribuição de Valores
---------------------

.. code-block:: python

    # Atribuição Simples

    foo = 0
    bar = 'bla bla bla'
    print(foo)

.. code-block:: console

    0

.. code-block:: python

    print(bar)

.. code-block:: console

    bla bla bla

.. code-block:: python

    # Atribuição Composta ou Atribuição por Tupla
    x, y, z = (1, 2, 3)

    print(x)

.. code-block:: console

    1

.. code-block:: python

    print(y)

.. code-block:: console

    2

.. code-block:: python

    print(z)

.. code-block:: console

    3

Invertendo valores:

.. code-block:: python

    x = 10
    y = 20
    x, y = y, x
    print(x)

.. code-block:: console

    20

.. code-block:: python

    print(y)

.. code-block:: console

    10