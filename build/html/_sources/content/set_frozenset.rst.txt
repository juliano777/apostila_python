set e frozenset
***************

|    Similarmente a list e tuple, a diferença entre eles é que frozenset é um tipo imutável.
|    Seus elementos são únicos.
|    Implementam operações matemáticas de conjuntos.



.. code-block:: python

    # Set vazio:
    s = {*()}

ou


.. code-block:: python

    s = set()



Criação de um conjunto (set) não vazio:

> s = set([1, 1, 2, 3])

ou

> s = set((1, 1, 2, 3))

ou

> s = set([1, 1, 2, 3])

ou

> s = set({1, 1, 2, 3})

ou

> s = {1, 2, 3}



Exibindo o conteúdo do set:

> s

{1, 2, 3}



Definição de dois conjuntos:

> a = set([1,2,3])

> b = set([2,3,4])



Operação de união entre os conjuntos:

> a | b

ou

> a.union(b)

{1, 2, 3, 4}



Operação de intersecção entre os conjuntos:

> a & b

ou

> a.intersection(b)

{2, 3}



Frozenset vazio:

f = frozenset()



Frozenset não vazio:

> f = frozenset((1, 2, 3))

ou

> f = frozenset({1, 2, 3})

ou

> f = frozenset([1, 2, 3])

ou

> f = frozenset({1, 2, 3})



Exibindo o conteúdo do frozenset:

> f

frozenset({1, 2, 3})
