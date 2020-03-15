
# https://data-flair.training/blogs/python-operator/
# https://www.tutorialspoint.com/python/bitwise_operators_example

Operadores
**********

Operadores Aritméticos
----------------------

+-------------------------+--------------+-------------+-----------+
| **Nome**                | **Operador** | **Exemplo** | **Saída** |
+-------------------------+--------------+-------------+-----------+
| Soma                    | \+           | 5 + 2       | 7         |
+-------------------------+--------------+-------------+-----------+
| Subtração               | \-           | 13 - 3      | 10        |
+-------------------------+--------------+-------------+-----------+
| Multiplicação           | \*           | 5 * 3       | 15        |
+-------------------------+--------------+-------------+-----------+
| Divisão                 | /            | 7 / 2       | 3.5       |
+-------------------------+--------------+-------------+-----------+
| Divisão Inteira (Floor) | //           | 7 // 2      | 3         |
+-------------------------+--------------+-------------+-----------+
| Potenciação             | \*\*         | 2 ** 9      | 512       |
+-------------------------+--------------+-------------+-----------+
| Módulo                  | %            | 7 % 2       | 1         |
+-------------------------+--------------+-------------+-----------+


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

+--------------------+----------+
| Nome               | Operador |
+--------------------+----------+
| And ou "E" lógico  | and      |
+--------------------+----------+
| Or ou "Ou" lógico  | or       |
+--------------------+----------+
| Not ou Negação     | not      |
+--------------------+----------+


Tabelas da Verdade
~~~~~~~~~~~~~~~~~~

**Tabela AND**

Na lógica **AND** para que o resultado seja verdadeiro (*True*), **todos** os
valores envolvidos têm que ser verdadeiros.

+-----------------+-----------+
| Operação        | Resultado |
+-----------------+-----------+
| False and False | False     |
+-----------------+-----------+
| False and True  | False     |
+-----------------+-----------+
| True and False  | False     |
+-----------------+-----------+
| True and True   | True      |
+-----------------+-----------+


**Tabela OR**

Na lógica **OR** para que o resultado seja verdadeiro (*True*), basta que
apenas um dos valores envolvidos seja verdadeiro.

+----------------+-----------+
| Operação       | Resultado |
+----------------+-----------+
| False or False | False     |
+----------------+-----------+
| False or True  | True      |
+----------------+-----------+
| True or False  | True      |
+----------------+-----------+
| True or True   | True      |
+----------------+-----------+


**Tabela NOT**

Seu papel é apenas inverter.

+---------------+---------------+
| **Operação**  | **Resultado** |
+---------------+---------------+
| not False     | True          |
+---------------+---------------+
| not True      | False         |
+---------------+---------------+


Operadores de Associação
------------------------

+--------------+-----------------------+
| **Operador** | **Breve Descrição**   |
+--------------+-----------------------+
| in           | Testa se pertence     |
+--------------+-----------------------+
| not in       | Testa se não pertence |
+--------------+-----------------------+

Exemplos:

7 in (9, 11, 13, 7, 28)                                                                                                                                                                                    
True

'a' in 'Python'                                                                                                                                                                                            
False

'nome' in {'nome': 'Diana'}                                                                                                                                                                                
True

'Diana' in {'nome': 'Diana'}                                                                                                                                                                               
False

(2 * 10) not in (20, 30)                                                                                                                                                                                  
False

3 not in (20, 30)                                                                                                                                                                                         
True



Operadores de Identidade
------------------------

+--------------+---------------------+
| **Operador** | **Breve Descrição** |
+--------------+---------------------+
| is           | Testa se é          |
+--------------+---------------------+
| is not       | Testa  não é        |
+--------------+---------------------+

Exemplos:

t1 = (1, 2, 3)                                                                                                                                                                                             

id(t1)                                                                                                                                                                                                     
139965970848192

t2 = t1                                                                                                                                                                                                    

id(t2)                                                                                                                                                                                                    
139965970848192

t3 = (1, 2, 3)                                                                                                                                                                                            

id(t3)                                                                                                                                                                                                    
139965970847744

t1 is t2                                                                                                                                                                                                  
True

t1 is t3                                                                                                                                                                                                  
False

t1 == t3                                                                                                                                                                                                  
True

t1 is not t3                                                                                                                                                                                              
True



Operadores Bitwise (Operadores Bit a Bit)
-----------------------------------------

+-------------------------+--------------+
| **Nome**                | **Operador** |
+-------------------------+--------------+
| Binary AND              | &            |
+-------------------------+--------------+
| Binary OR               | |            |
+-------------------------+--------------+
| Binary XOR              | ^            |
+-------------------------+--------------+
| Binary One's Complement | ~            |
+-------------------------+--------------+
| Binary Left-Shift       | <<           |
+-------------------------+--------------+
| Binary Right-Shift      | >>           |
+-------------------------+--------------+

Binary AND / "E" Binário (&)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~


+-------------+-------------+--+-------------+
| *And*       | **Binário** |  | **Decimal** |
+-------------+----+----+---+--+-------------+
| NumX        |  1 |  0 | 1 |  | 5           |
+-------------+----+----+---+--+-------------+
| NumY        |  1 |  1 | 0 |  | 6           |
+-------------+----+----+---+--+-------------+
| *Resultado* |  1 |  0 | 0 |  | 4           |
+-------------+----+----+---+--+-------------+

0b101 & 0b110                                                                                                                                                                                             
4

bin(0b101 & 0b110)                                                                                                                                                                                        
0b100'

5 & 6                                                                                                                                                                                                     
4




Binary OR / "Ou" Binário (|)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+--+-------------+
| *Or*        | **Binário** |  | **Decimal** |
+-------------+----+----+---+--+-------------+
| NumX        |  1 |  0 | 1 |  | 5           |
+-------------+----+----+---+--+-------------+
| NumY        |  1 |  1 | 0 |  | 6           |
+-------------+----+----+---+--+-------------+
| *Resultado* |  1 |  1 | 1 |  | 7           |
+-------------+----+----+---+--+-------------+

0b101 | 0b110                                                                                                                                                                                             
7

bin(0b101 | 0b110)
0b111'

5 | 6                                                                                                                                                                                                     
7


Binary XOR / "Ou" Exclusivo Binário (^) 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

+-------------+-------------+--+-------------+
| *XOr*       | **Binário** |  | **Decimal** |
+-------------+----+----+---+--+-------------+
| NumX        |  1 |  0 | 1 |  | 5           |
+-------------+----+----+---+--+-------------+
| NumY        |  1 |  1 | 0 |  | 6           |
+-------------+----+----+---+--+-------------+
| *Resultado* |  0 |  1 | 1 |  | 3           |
+-------------+----+----+---+--+-------------+

0b101 ^ 0b110                                                                                                                                                                                             
3

bin(0b101 ^ 0b110)
0b11'

5 ^ 6                                                                                                                                                                                                     
3


Binary One's Complement / Complemento Binário (~)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

It returns the one’s complement of a number’s binary.
It flips the bits. Binary for 2 is 00000010.
Its one’s complement is 11111101.
This is binary for -3.
So, this results in -3. Similarly, ~1 results in -2.






Binary Left-Shift / Deslocamento Binário à Esquerda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Binary Right-Shift / Deslocamento Binário à Direita
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





















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