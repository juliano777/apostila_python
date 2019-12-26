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


.. code-block:: python

    # Criação de um conjunto (set) não vazio:
    s = set([1, 1, 2, 3])

ou

.. code-block:: python

    s = set((1, 1, 2, 3))

ou

.. code-block:: python

    s = set([1, 1, 2, 3])

ou

.. code-block:: python

    s = set({1, 1, 2, 3})

ou

.. code-block:: python

    s = {1, 2, 3}

.. code-block:: python

    # Exibindo o conteúdo do set:
    s

.. code-block:: console

    {1, 2, 3}

.. code-block:: python

    # Definição de dois conjuntos:
    a = set([1,2,3])
    b = set([2,3,4])


.. code-block:: python

    # Operação de união entre os conjuntos:
    a | b

ou

.. code-block:: python

    a.union(b)

.. code-block:: console

    {1, 2, 3, 4}


.. code-block:: python

    # Operação de intersecção entre os conjuntos:
    a & b

ou

.. code-block:: python

    a.intersection(b)

.. code-block:: console

    {2, 3}


.. code-block:: python

    # Frozenset vazio:
    f = frozenset()

.. code-block:: python

    # Frozenset não vazio:
    f = frozenset((1, 2, 3))

ou

.. code-block:: python

    f = frozenset({1, 2, 3})

ou

.. code-block:: python

    f = frozenset([1, 2, 3])

ou

.. code-block:: python

    f = frozenset({1, 2, 3})

.. code-block:: python

    # Exibindo o conteúdo do frozenset:
    f

.. code-block:: console

    frozenset({1, 2, 3})
