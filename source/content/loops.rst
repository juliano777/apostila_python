Loops - Laços de Repetição
**************************

while
-----

Executa em laço (loop) enquanto a condição for verdadeira.

.. code-block:: python

    # 
    i = 0

    # 
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

	Opcionalmente, pode-se adicionar um else ao while em Python.
	A idéia é que se caso o loop seja executado sem interrupção, um break, por exemplo, o que estiver dentro do bloco else será executado.

.. code-block:: python

    # 
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

.. code-block:: python

    #    
    i = 0

    #
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

.. code-block:: python

    # 
    i = 0

    #
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

.. code-block:: python

    # 
    while True:
        print('x')

.. code-block:: console

    x
    x
    x
    . . .



for
~~~

.. code-block:: python

    # 
    for i in range(5):
        print(i)

.. code-block:: console

    0
    1
    2
    3
    4

.. code-block:: python

    # 
    lor = ('Gandalf', 'Bilbo', 'Frodo', 'Sauron', 'Aragorn', 'Legolas')

    #
    for i in lor:
        print(i)

.. code-block:: console

    Gandalf
    Bilbo
    Frodo
    Sauron
    Aragorn
    Legolas

.. code-block:: python

    #     
    for i, personagem in enumerate(lor):
        print('%d - %s' % (i, personagem))

.. code-block:: console

    0 - Gandalf
    1 - Bilbo
    2 - Frodo
    3 - Sauron
    4 - Aragorn
    5 - Legolas

list(enumerate(lor))
[(0, 'Gandalf'), (1, 'Bilbo'), (2, 'Frodo'), (3, 'Sauron'), (4, 'Aragorn'), (5, 'Legolas')]


dados =  [('Nome', 'Chiquinho'), ('Sobrenome', 'da Silva'), ('Idade', 50)]

for k, v in dados:
    print('%s: %s' % (k, v))

Nome: Chiquinho
Sobrenome: da Silva
Idade: 50


dados = {
    'Nome': 'Chiquinho',
    'Sobrenome': 'da Silva',
    'Idade': 50
}

for k, v in dados.items():
    print('%s: %s' % (k, v))

Sobrenome: da Silva
Idade: 50
Nome: Chiquinho



for i in range(5):
    print(i)
else:
    print('Fim')
    
0
1
2
3
4
Fim

for i in range(10):
    if i == 6:
        break
    print(i)
else:
    print('Fim')

0
1
2
3
4
5


for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('Fim')

1
3
5
7
9
Fim
