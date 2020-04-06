Loops - Laços de Repetição
**************************

while
-----

Executa em laço (loop) enquanto a condição for verdadeira.



Enquanto i for menor que 5, exiba i:

.. code-block:: python

    i = 0

    while i < 5:
        print(i)
        i += 1

.. code-block:: console

    0
    1
    2
    3
    4



O else no loop while
~~~~~~~~~~~~~~~~~~~~

|   Opcionalmente, pode-se adicionar um else ao while em Python.
|   A idéia é que se caso o loop seja executado sem interrupção, um break, por exemplo, o que estiver dentro do bloco else será executado.



Loop while com else sem interrupção:

.. code-block:: python

    i = 0
    while i < 5:
        print(i)
        i += 1
    else:   
        print('Fim')

.. code-block:: console

    0
    1
    2
    3
    4
    Fim



Loop while com else com interrupção (break):

.. code-block:: python

    i = 0

    while i <= 10:
        if i == 5: break       
        print(i)
        i += 1
    else:   
        print('Fim')

.. code-block:: console

    0
    1
    2
    3
    4



Loop while com else e sem break:

.. code-block:: python

    i = 0

    while i <= 10:
        if (i % 2 == 0): 
            i += 1
            continue
        print(i)
        i += 1        
    else:   
        print('Fim')

.. code-block:: console

    1
    3
    5
    7
    9
    Fim



Loop Infinito
~~~~~~~~~~~~~

|   Bla bla bla



Enquanto não houver uma interrupção externa, o loop abaixo exibirá "x" eternamente:

.. code-block:: python

    while True:
        print('x')

.. code-block:: console

    x
    x
    x
    . . .



for
~~~

|   Bla bla bla



Um simples loop for com a função range:

.. code-block:: python

    for i in range(5):
        print(i)

.. code-block:: console

    0
    1
    2
    3
    4



Loop sobre os elementos de uma tupla:

.. code-block:: python

    lor = ('Gandalf', 'Bilbo', 'Frodo', 'Sauron', 'Aragorn', 'Legolas')

    for i in lor:
        print(i)

.. code-block:: console

    Gandalf
    Bilbo
    Frodo
    Sauron
    Aragorn
    Legolas



Loop sobr os elementos da tupla enumerados:

.. code-block:: python

    for i, personagem in enumerate(lor):
        print(f'{i} - {personagem}')

.. code-block:: console

    0 - Gandalf
    1 - Bilbo
    2 - Frodo
    3 - Sauron
    4 - Aragorn
    5 - Legolas



Enumerando a tupla e convertendo-a para uma lista:

.. code-block:: python

    list(enumerate(lor))

.. code-block:: console

    [(0, 'Gandalf'), (1, 'Bilbo'), (2, 'Frodo'), (3, 'Sauron'), (4, 'Aragorn'), (5, 'Legolas')]



Lista cujos elementos são tuplas cujos elementos representam chave e valor, e por fim loop:

.. code-block:: python

    dados =  [('Nome', 'Chiquinho'), ('Sobrenome', 'da Silva'), ('Idade', 50)]

    for k, v in dados:
        print(f'{k}: {v}')

.. code-block:: console

    Nome: Chiquinho
    Sobrenome: da Silva
    Idade: 50



Criação de um dicionário:

.. code-block:: python

    dados = {
        'Nome': 'Chiquinho',
        'Sobrenome': 'da Silva',
        'Idade': 50
    }



Loop sobre um dicionário:

.. code-block:: python

    for k, v in dados.items():
        print(f'{k}: {v}')

.. code-block:: console

    Sobrenome: da Silva
    Idade: 50
    Nome: Chiquinho



Loop for com else e sem interrupção:

.. code-block:: python

    for i in range(5):
        print(i)
    else:
        print('Fim')

.. code-block:: console

    0
    1
    2
    3
    4
    Fim



Loop for com else e com interrupção:

.. code-block:: python

    for i in range(10):
        if i == 6:
            break
        print(i)
    else:
        print('Fim')

.. code-block:: console

    0
    1
    2
    3
    4
    5



Loop for com else e sem interrupção:

.. code-block:: python

    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)
    else:
        print('Fim')

.. code-block:: console

    1
    3
    5
    7
    9
    Fim