
# https://data-flair.training/blogs/python-operator/
# https://www.tutorialspoint.com/python/bitwise_operators_example

Operadores
**********

Operadores Aritméticos
----------------------

+-------------------------+----------+---------+-------+
| Nome                    | Operador | Exemplo | Saída |
+-------------------------+----------+---------+-------+
| Soma                    | \+       | 5 + 2   | 7     |
+-------------------------+----------+---------+-------+
| Subtração               | \-       | 13 - 3  | 10    |
+-------------------------+----------+---------+-------+
| Multiplicação           | \*       | 5 * 3   | 15    |
+-------------------------+----------+---------+-------+
| Divisão                 | /        | 7 / 2   | 3.5   |
+-------------------------+----------+---------+-------+
| Divisão Inteira (Floor) | //       | 7 // 2  | 3     |
+-------------------------+----------+---------+-------+
| Potenciação             | \*\*     | 2 ** 9  | 512   |
+-------------------------+----------+---------+-------+
| Módulo                  | %        | 7 % 2   | 1     |
+-------------------------+----------+---------+-------+


Operadores Relacionais
----------------------

+-------------+----------+---------------+-------+
| Nome        | Operador | Exemplo       | Saída |
+-------------+----------+---------------+-------+
| Menor       | <        | 3 < 2         | False |
|             |          +---------------+-------+
|             |          | 2 < 3         | True  |
+-------------+----------+---------------+-------+
| Maior       | >        | 7 > 5         | True  |
|             |          +---------------+-------+
|             |          | 'A' > 'B'     | False |
+-------------+----------+---------------+-------+
| Menor Igual | <=       | 5 <= 9        | True  |
|             |          +---------------+-------+
|             |          | 11 <= 3       | False |
+-------------+----------+---------------+-------+
| Maior Igual | >=       | 'Z' >= 'W'    | True  |
|             |          +---------------+-------+
|             |          | 0 >= 1        | False |
+-------------+----------+---------------+-------+
| Igual       | ==       | 7 == (4 + 3)  | True  |
|             |          +---------------+-------+
|             |          | 'k' == 'v'    | False |
+-------------+----------+---------------+-------+
| Diferente   | !=       | 5 != 3        | True  |
|             |          +---------------+-------+
|             |          | 0 != 0        | False |
+-------------+----------+---------------+-------+


Operadores de Atribuição
------------------------

 +-----------------------------------+----------+
| Nome                              | Operador |
+-----------------------------------+----------+
| Atribuição                        | =        |
+-----------------------------------+----------+
| Adicionar e Atribuir (Incremento) | +=       |
+-----------------------------------+----------+
| Subtrair e Atribuir (Decremento)  | -=       |
+-----------------------------------+----------+
| Dividir e Atribuir                | /=       |
+-----------------------------------+----------+
| Multiplicar e Atribuir            | \*=      |
+-----------------------------------+----------+
| Módulo e Atribuir                 | %=       |
+-----------------------------------+----------+
| Exponenciação e Atribuir          | \*\*=    |
+-----------------------------------+----------+
| Divisão Inteira e Atribuir        | //=      |
+-----------------------------------+----------+


Operadores Lógicos
------------------

Operadores de Associação
------------------------

Operadores de Identidade
------------------------

Operadores Bitwise (Operadores Bit a Bit)
-----------------------------------------





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

.. code-block:: python

    False | False

.. code-block:: console

    False

.. code-block:: python

    False | True

.. code-block:: console

    True

.. code-block:: python

    True | False

.. code-block:: console

    True

.. code-block:: python

    True | True

.. code-block:: console

    True






# 0010 | 0001 = 0011 -> 2 | 1 = 3

.. code-block:: python

    2 | 1

.. code-block:: console

    3

'''
0010
ou
0001
-------
0011
'''


# 1010 | 0011 = 1011 -> 10 | 3 = 11


.. code-block:: python

    10 | 3

.. code-block:: console

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



.. code-block:: python

    False & False

.. code-block:: console

    False

.. code-block:: python

    False & True

.. code-block:: console

    False

.. code-block:: python

    True & False

.. code-block:: console

    False

.. code-block:: python

    True & True

.. code-block:: console

    True


# 0010 & 0001 = 0000 -> 2 & 1 = 0

.. code-block:: python

    2 & 1

.. code-block:: console

    0


# 1010 & 0011 = 0010 -> 10 & 3 = 2

.. code-block:: python

    10 & 3

.. code-block:: console

    2



## Operador ampersand "^": Ou Exclusivo Binário / Binary XOr

# Deslocamento de Bits / Bit Shift


.. code-block:: python

    False >> False

.. code-block:: console

    0

.. code-block:: python

    False >> True

.. code-block:: console

    0

.. code-block:: python

    True >> False

.. code-block:: console

    1

.. code-block:: python

    True >> True

    .. code-block:: console

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