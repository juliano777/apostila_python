Tupla
*****

|	Tupla têm sua estrutura muito similar à da lista, no entanto, ela é imutável.
|	Ela é mais recomendada para uso de dados estáticos, pois comparada à lista, tem
| um desempenho melhor devido à sua simplicidade e consome menos recursos.



.. code-block:: python

    # Declaração de uma tupla vazia:
	t = ()

ou

.. code-block:: python

    t = tuple()


.. code-block:: python

    # Declaração de uma tupla com três elementos:
	t = tuple([1, 2, 3])

ou

.. code-block:: python

    t = (1, 2, 3)

ou

.. code-block:: python

    t = 1, 2, 3

.. code-block:: python

    # Exibindo o conteúdo da tupla:
	t

.. code-block:: console

    (1, 2, 3)


.. code-block:: python

	# Criação de um conjunto (set) contendo todos atributos e 
	# métodos de uma tupla:
	tupla = set(dir(tuple))


.. code-block:: python

    # Criação de um conjunto (set) contendo todos atributos e 
	# métodos de uma lista:
	lista = set(dir(list))



.. code-block:: python

    # Via intersecção, o que há em comum entre lista e tupla?:
	tupla.intersection(lista)

. . .

Tuplas tem apenas os métodos count e index.

.. code-block:: python

    # Tupla de um único elemento:
	t = (1, )


.. code-block:: python

    # Exibir o conteúdo da tupla:
	t

.. code-block:: console

    (1,)



.. code-block:: python

    # Função type para verificar o tipo do objeto:
	type(t)

.. code-block:: console

    tuple


.. code-block:: python

    # Declaração de duas variáveis e trocando o valor entre elas:
	x = 0
	y = 1
	x, y = y, x  # A troca se dá pela atribuição respectiva



.. code-block:: python

	# Verificando os valores das variáveis:
	x

.. code-block:: console

    1


.. code-block:: python

    y


.. code-block:: console

    0



.. code-block:: python

    # Criação de uma variável que retorna uma tupla com três elementos:
	def retorna_tupla():
		return 1, 2, 3



.. code-block:: python

    # Atribuição respectiva:
	x, y, z = retorna_tupla()


.. code-block:: python

    # Verificando os valores das variáveis:
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

Tuplas são imutáveis, mas seus elementos não necessariamente:

.. code-block:: python

    t = ({}, [])   # Tupla com dois elementos; um dicionário e uma lista
	t[0].update({'chave': 'valor'})  # Alterando o primeiro elemento
	t[1].append(7)  # Alterando o segundo elemento
	t  # Exibindo a tupla

.. code-block:: console

    ({'chave': 'valor'}, [7])