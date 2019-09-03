Tipos Numéricos - int, float e complex
**************************************

int
---

	Para representação de todos números inteiros é o tipo int.
	A princípio utilizamos para números inteiros o tipo int. O número máximo de int que é aceito pode variar de uma máquina para outra.
	Para sabermos qual é o número máximo do tipo int fazemos:


.. code-block:: python

    # Objeto inteiro
	i = int(7)

ou

.. code-block:: python

    i = 7

.. code-block:: python

    # Verificando seu valor
	i

7

.. code-block:: python

    # Verificando seu tipo
	type(i)

int

.. code-block:: python

    # 
	type(bar)

long

.. code-block:: python

    # Representação hexadecimal de 178
	0xb2

178

.. code-block:: python

    # Representação octal de 8
	0o10

8

.. code-block:: python

    # Representação binária de 14
	0b1110

14

.. code-block:: python

    # Número 7 (sete) convertido para as bases binária, octal e hexadecimal
	bin(7)  # binário

'0b111'

.. code-block:: python

    # 
	oct(7)

'0o7'

.. code-block:: python

    # 
	hex(7)

'0x7'

.. code-block:: python

    # Descobrir o decimal dada uma base
	int('facada', base=16)

16435930

.. code-block:: python

    # 
	int('25', base=8)

21

.. code-block:: python

    # 
	int('1111', base=2)

15


float
-----

	Ponto flutuante; não tem precisão absoluta, sua precisão é relativa.
	Para uma maior precisão com números que tenham ponto flutuante, utilizar o módulo decimal.



.. code-block:: python

    # Criação de um float
	f = float(3)

ou

.. code-block:: python

    f = 3.0

.. code-block:: python

    f  # Veririca o valor

3.0

Formas de se definir um float:

.. code-block:: python

    # 
	x = 0.5000000000

ou

.. code-block:: python

    # 
	x = 0.5

ou

.. code-block:: python

    # 
	x = .5

	x  # Exibe o valor

0.5

.. code-block:: python

    type(x)  # Tipo

float

.. code-block:: python

    # 
	x = 2.

	x  # Verifica o valor

2.0

.. code-block:: python

    # Que tipo resulta de da soma de um inteiro e um float?
	type(7 + 3.0)

float


.. code-block:: python

    # Resultado
	7 + 3.0

10.0


.. code-block:: python

    # Divisão
	3 / 2

ou

.. code-block:: python

    3 / 2.0

ou

.. code-block:: python

    3.0 / 2

ou

.. code-block:: python

    3.0 / 2.0

1.5

.. code-block:: python

    # Divisão Inteira
	3 // 2.0

1.0

.. code-block:: python

    # Notação Científica
	1e+2

100.0

.. code-block:: python

    # 
	1e-3

0.001



complex
-------

    É o tipo de dados em Python que trata de números complexos, que são muito utilizados em engenharia elétrica.

.. code-block:: python

    # Número complexo somente com a parte real
	c = complex(1)
	print(c)

.. code-block:: console

    (1+0j)

.. code-block:: python

    # Verificando seu valor e seu tipo
	type(c)

.. code-block:: console

    complex

.. code-block:: python

    # Novo valor do número complexo com parte real e imaginária
	c = complex(5, 3)

.. code-block:: python

    # 
	c  # Verificando o valor

.. code-block:: console

    (5+3j)


.. code-block:: python

    # Número complexo somente com a parte imaginária
	c = complex(0, 3)

.. code-block:: python

    # 
	c  # Verificando seu valor

.. code-block:: console

    3j

.. code-block:: python

    # 
	c.imag  # Extraindo somente a parte imaginária

.. code-block:: console

    3.0

.. code-block:: python

    # 
	c.real  # Extraindo somente a parte real

.. code-block:: console

    0.0

.. code-block:: python

    # 
	c + 1  # Somando o número com a parte real

.. code-block:: console

    (1+3j)

.. code-block:: python

    # 
	c + complex('7j')  # Somando o número com a parte imaginária

.. code-block:: console

    10j

.. code-block:: python

    # 
	c + complex(2, 17)  # somando o número complexo com outro complexo

.. code-block:: console

    (2+20j)
