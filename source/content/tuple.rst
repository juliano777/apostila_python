Tupla
*****

	Tupla têm sua estrutura muito similar à da lista, no entanto, ela é imutável.
	Ela é mais recomendada para uso de dados estáticos, pois comparada à lista, tem um desempenho melhor devido à sua simplicidade e consome menos recursos.



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

.. code-block:: python
	    
{'__add__',
 '__class__',
 '__contains__',
 '__delattr__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__getitem__',
 '__getslice__',
 '__gt__',
 '__hash__',
 '__init__',
 '__iter__',
 '__le__',
 '__len__',
 '__lt__',
 '__mul__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rmul__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 'count',
 'index'}

Tuplas tem apenas os métodos count e index.



Tupla de um único elemento:

> t = (1, )



Exibir o conteúdo da tupla:

> t

(1,)



Função type para verificar o tipo do objeto:

> type(t)

tuple



Declaração de duas variáveis e trocando o valor entre elas:

> x = 0

> y = 1

> x, y = y, x  # A troca se dá pela atribuição respectiva



Verificando os valores das variáveis:

> x

1

> y

0



Criação de uma variável que retorna uma tupla com três elementos:

> def retorna_tupla():
    return 1, 2, 3



Atribuição respectiva:

> x, y, z = retorna_tupla()



Verificando os valores das variáveis:

> print(x)

1

> print(y)

2

> print(z)

3



Tuplas são imutáveis, mas seus elementos não necessariamente:

> t = ({}, [])   # Tupla com dois elementos; um dicionário e uma lista

> t[0].update({'chave': 'valor'})  # Alterando o primeiro elemento

> t[1].append(7)  # Alterando o segundo elemento

> t  # Exibindo a tupla

({'chave': 'valor'}, [7])
