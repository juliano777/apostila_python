
.. https://data-flair.training/blogs/python-operator/
.. https://www.tutorialspoint.com/python/bitwise_operators_example

Operadores
**********

O que são Operadores
--------------------

|   Operadores são elementos de programação que permitem fazer operações com
| operandos.
|   Operandos são os elementos cujas ações de um operador têm efeito.
|   Operadores já fazem parte de nossa vida muito antes da programação, em
| matemática para ser mais preciso.
|   Operadores podem ser **binários** e **unários**.

Operadores Binários
~~~~~~~~~~~~~~~~~~~

|   São aqueles que requerem 2 (dois) operandos para uma operação.
|
|   Exemplo: `2 + 5`
|
|   Operador: `+` (soma)
|   Operandos: `2` e `5`



Operadores Unários
~~~~~~~~~~~~~~~~~~

|   São aqueles que requerem apenas 1 (um) operando para uma operação.
|
|   Exemplo: `not False`
|
|   Operador: `not` (negação)
|   Operandos: `False`



Operadores Aritméticos
----------------------

|   São os primeiros operadores que uma pessoa tem contato na vida, pois são
| os operadores para operações matemáticas.

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

|   Têm por objetivo atribuir um valor a uma variável.

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



Atribuição simples e exibição da primeira variável:

.. code-block:: python

    foo = 0
    bar = 'bla bla bla'
    print(foo)

.. code-block:: console

    0

Exibição do valor da segunda variável:

.. code-block:: python

    print(bar)

.. code-block:: console

    bla bla bla

Atribuição composta ou atribuição por tupla e exibição de seus respectivos
valores:

.. code-block:: python

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

Invertendo valores e suas respectivas exibições:

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


Incremento:

.. code-block:: python

    x = 0
    x += 1  # 1
    x += 1  # 2
    print(x)

.. code-block:: console

    2

Decremento (aproveitando o exercício anterior):

.. code-block:: python

    x -= 1
    print(x)

.. code-block:: console

    1



Dividir e atribuir:

.. code-block:: python

    x = 20
    x /= 2  # 10.0
    x /= 2  # 5.0
    print(x)

.. code-block:: console

    5.0



Multiplicar e atribuir:

.. code-block:: python

    x = 10
    x *= 2  # 20
    x *= 2  # 40
    print(x)

.. code-block:: console

    40



Atribuição por módulo:

.. code-block:: python

    x = 5
    x %= 3
    print(x)

.. code-block:: console

    2



Atribuição por exponenciação:

.. code-block:: python

    x = 10
    x **= 2
    print(x)

.. code-block:: console

    100



Atribuição floor:

.. code-block:: python

    x = 7
    x //= 2
    print(x)

.. code-block:: console

    3     


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
| is not       | Testa se não é      |
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
| Binary OR               | \|           |
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

    7 << 2

.. code-block:: console

    28

.. code-block:: python

    bin(7 << 2)                                     

.. code-block:: console

    '0b11100'

.. code-block:: python

    7 << 3         

.. code-block:: console

    56

.. code-block:: python

    bin(7 << 3)                         

.. code-block:: console

    '0b111000'




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

    4 >> 1

.. code-block:: console

    2


.. code-block:: python

    bin(4 >> 1)                                      

.. code-block:: console

    '0b10'


.. code-block:: python

    4 >> 2         

.. code-block:: console

    1


.. code-block:: python

    8 >> 1                                   

.. code-block:: console

    4


.. code-block:: python

    bin(8 >> 1)         

.. code-block:: console

    '0b100'


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

