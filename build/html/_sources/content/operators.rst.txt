
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

Atribuição de Valores
~~~~~~~~~~~~~~~~~~~~~

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

.. code-block:: python

    7 in (9, 11, 13, 7, 28)

.. code-block:: console

    True

.. code-block:: python

    'a' in 'Python'

.. code-block:: console

    False

.. code-block:: python

    'nome' in {'nome': 'Diana'}    

.. code-block:: console

    True

.. code-block:: python

    'Diana' in {'nome': 'Diana'}                                                                                                                                                                               

.. code-block:: console

    False

.. code-block:: python

    (2 * 10) not in (20, 30)                                                                                                                                                                                  

.. code-block:: console

    False

.. code-block:: python

    3 not in (20, 30)                                                                                                                                                                                         

.. code-block:: console

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

.. code-block:: python

    t1 = (1, 2, 3)                                                                                                                                                                                             

.. code-block:: python

    id(t1)                                                                                                                                                                                                     

.. code-block:: console

    139965970848192

.. code-block:: python

    t2 = t1                                                                                                                                                                                                    

.. code-block:: python

    id(t2)                                                                                                                                                                                                    

.. code-block:: console

    139965970848192

.. code-block:: python

    t3 = (1, 2, 3)                                                                                                                                                                                            

.. code-block:: python

    id(t3)                                                                                                                                                                                                    

.. code-block:: console

    139965970847744

.. code-block:: python

    t1 is t2                                                                                                                                                                                                  

.. code-block:: console

    True

.. code-block:: python

    t1 is t3                                                                                                                                                                                                  

.. code-block:: console

    False

.. code-block:: python

    t1 == t3                                                                                                                                                                                                  

.. code-block:: console

    True

.. code-block:: python

    t1 is not t3

.. code-block:: console

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

.. code-block:: python

    0b101 & 0b110                                                                                                                                                                                             

.. code-block:: console

    4

.. code-block:: python

    bin(0b101 & 0b110)                                                                                                                                                                                        

.. code-block:: console

    0b100'

.. code-block:: python

    5 & 6                                                                                                                                                                                                     

.. code-block:: console

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

.. code-block:: python

    0b101 | 0b110

.. code-block:: console

    7

.. code-block:: python

    bin(0b101 | 0b110)

.. code-block:: console

    0b111'

.. code-block:: python

    5 | 6                                                                                                                                                                                                     

.. code-block:: console

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

.. code-block:: python

    0b101 ^ 0b110

.. code-block:: console

    3

.. code-block:: python

    bin(0b101 ^ 0b110)

.. code-block:: console

    0b11'

.. code-block:: python

    5 ^ 6                                                                                                                                                                                                     

.. code-block:: console

    3


Binary One's Complement / Complemento Binário (~)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    ~ True                                                                                                                                                                                                             

.. code-block:: console

    -2

.. code-block:: python

    ~ False                                   

.. code-block:: console

    -1

.. code-block:: python

    ~ 0        

.. code-block:: console

    -1

.. code-block:: python

    ~ 1                                  

.. code-block:: console

    -2

.. code-block:: python

    ~ 2        

.. code-block:: console

    -3

.. code-block:: python

    ~ -3                          

.. code-block:: console

    2

.. code-block:: python

    ~ -1                                                      

.. code-block:: console

    0  





Binary Left-Shift / Deslocamento Binário à Esquerda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    False << False                                                                                                                                                                                             

.. code-block:: console

    0

.. code-block:: python

    False << True                                                                                                                                                                                              

.. code-block:: console

    0

.. code-block:: python

    True << False                                                                                                                                                                                              

.. code-block:: console

    1

.. code-block:: python

    True << True                                                                                                                                                                                               

.. code-block:: console

    2


Binary Right-Shift / Deslocamento Binário à Direita
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

