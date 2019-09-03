Tipos Numéricos - int, float e complex
**************************************

int
---

	Para representação de todos números inteiros é o tipo int.
	A princípio utilizamos para números inteiros o tipo int. O número máximo de int que é aceito pode variar de uma máquina para outra.
	Para sabermos qual é o número máximo do tipo int fazemos:


Objeto inteiro:

> i = int(7)

ou

> i = 7



Verificando seu valor;

> i

7



Verificando seu tipo:

> type(i)

int

type(bar)
long



Representação hexadecimal de 178:

> 0xb2

178



Representação octal de 8:

> 0o10

8



Representação binária de 14:

> 0b1110

14



Número 7 (sete) convertido para as bases binária, octal e hexadecimal:

> bin(7)  # binário

'0b111'

> oct(7)

'0o7'

> hex(7)

'0x7'



Descobrir o decimal dada uma base:

> int('facada', base=16)

16435930

> int('25', base=8)

21

> int('1111', base=2)

15



float

	Ponto flutuante; não tem precisão absoluta, sua precisão é relativa.
	Para uma maior precisão com números que tenham ponto flutuante, utilizar o módulo decimal.



Criação de um float:

> f = float(3)

ou

> f = 3.0

> f  # Veririca o valor

3.0



Formas de se definir um float:

> x = 0.5000000000

ou

> x = 0.5

ou

> x = .5

> x  # Exibe o valor

0.5

> type(x)  # Tipo

float

> x = 2.

> x  # Verifica o valor

2.0



Que tipo resulta de da soma de um inteiro e um float?
 
> type(7 + 3.0)

float



Resultado:

> 7 + 3.0

10.0



Divisão

> 3 / 2

ou

> 3 / 2.0

ou

> 3.0 / 2

ou

> 3.0 / 2.0

1.5



Divisão Inteira:

> 3 // 2.0

1.0



Notação Científica:

> 1e+2

100.0

> 1e-3

0.001



complex

    É o tipo de dados em Python que trata de números complexos, que são muito utilizados em engenharia elétrica.

.. code-block:: python

    # Número complexo somente com a parte real
	c = complex(1)


> c

(1+0j)

.. code-block:: python

    # Verificando seu valor e seu tipo
	type(c)

complex

.. code-block:: python

    # Novo valor do número complexo com parte real e imaginária
	c = complex(5, 3)

.. code-block:: python

    # 
	c  # Verificando o valor

(5+3j)


.. code-block:: python

    # Número complexo somente com a parte imaginária
	c = complex(0, 3)

.. code-block:: python

    # 
	c  # Verificando seu valor

3j

.. code-block:: python

    # 
	c.imag  # Extraindo somente a parte imaginária

3.0

.. code-block:: python

    # 
	c.real  # Extraindo somente a parte real

0.0

.. code-block:: python

    # 
	c + 1  # Somando o número com a parte real

(1+3j)

.. code-block:: python

    # 
	c + complex('7j')  # Somando o número com a parte imaginária

10j

.. code-block:: python

    # 
	c + complex(2, 17)  # somando o número complexo com outro complexo

(2+20j)
