if / elif / else
****************

	O comando if, que inglês significa "se" indica uma condição.


.. code-block:: python

    # Criação de dois objetos int:
    x = 7
    y = 5

    # Bloco if:
    if x > y:
        print('X é maior')

.. code-block:: console

    X é maior

.. code-block:: python

    # Bloco if;
    if x < y:
        print('X é maior')

.. code-block:: python

    # Objetos booleanos:
    foo = True
    bar = False

    # Bloco if:
    if foo:
        print('foo é verdadeiro!')

.. code-block:: console

    foo é verdadeiro!

.. code-block:: python

    # Bloco if:
    if not bar:
        print('bar é falso!')

.. code-block:: console

    bar é falso!

.. code-block:: python

    # Objeto string:
    texto = 'Python e PostgreSQL: Poder!'

    # Bloco if:
    if texto:
        print('A string NÃO é vazia!')

.. code-block:: console

    A string NÃO é vazia!

.. code-block:: python

    # String vazia:
    texto = ''

    # Bloco if:
    if not texto:
        print('A string é vazia!')

.. code-block:: console

    A string é vazia!

.. code-block:: python

    # Objetos int:
    x = 1
    y = 2

    # Bloco if:
    if x > y:
        print('X é maior')
    else:
        print('Y é maior')

.. code-block:: python

    Y é maior

.. code-block:: python

    # Objetos int:
    y = 1
    x = 1

    # Bloco if:
    if x > y:
        print('X é maior')
    elif x < y:    
        print('Y é maior')
    else:    
        print('Valores iguais')

.. code-block:: console

    Valores iguais

.. code-block:: python

    # Objeto int:
    x = 10

    # Bloco if:    
    if (x > 5):
        y = 3
    else:
        y = 0


if Ternário
~~~~~~~~~~~

.. code-block:: python

    x = 10  # Variável int

    # Atribuição de valor condicional:
    y = (50 if (x > 5) else 40)

    # Exibe o valor de "y":
    print(y)

.. code-block:: console

    50

.. code-block:: python

    # Variável float para receber a nota:
    nota = float(input('Digite a nota do aluno: '))

.. code-block:: console

    Digite a nota do aluno: 8

.. code-block:: python

    # Atribuição condicional:
    estado = 'aprovado' if nota >= 7 else 'reprovado'

.. code-block:: python

    # Exibe a mensagem:
    print('Aluno {}!'.format(estado))

.. code-block:: console

    Aluno aprovado!

.. code-block:: python

    # Variável int:
    num = int(input('Digite um número: '))

.. code-block:: console

    Digite um número: -2

.. code-block:: python

    # Atribuição condicional:
    sinal = 'positivo' if num > 0 else 'negativo' if num < 0 else 'zero'

    # Exibe mensagem:
    print('O número é {}'.format(sinal))

.. code-block:: console

    O número é negativo