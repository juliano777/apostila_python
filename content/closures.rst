Closures
********

Funções são objetos também.
Closures são funções que constroem funções, retorna outra função.
Sua estrutura é uma função dentro de outra.
A função interna é também conhecida como função auxiliadora (helper).



Criação de uma closure:

.. code-block:: python

    def funcao_principal(x):
        def funcao_auxiliadora(y):
            return x ** y
        return funcao_auxiliadora



Criação de uma variável foo e passando o valor x para a função principal:

.. code-block:: python

    foo = funcao_principal(2)

"foo" é uma nova função cujo o "x" de "função_principal" é 2.



Qual é o nome da função?:

.. code-block:: python

    print(foo.__name__)

.. code-block:: console

    funcao_auxiliadora



Tipo de "foo":

.. code-block:: python

    type(foo)

.. code-block:: console

    function



Representação de "foo":

.. code-block:: python

    repr(foo)

.. code-block:: console

    '<function funcao_principal.<locals>.funcao_auxiliadora at 0x7f9845369950>'



Imprimindo o valor resultante ao passar agora o valor y:

.. code-block:: python

    print(foo(6))

.. code-block:: console

    64

A operação realizada foi 2 elevado a 6 (x ** y).



Podemos também chamar a função principal passando o parâmetro da função auxiliar:

.. code-block:: python

    funcao_principal(5)(2)

.. code-block:: console

    25



Closures com Lambda
-------------------

Criação de uma closure com lambda:

.. code-block:: python

    def funcao_principal(x):
        return lambda y: x ** y



O "x" será 3:

.. code-block:: python

    bar = funcao_principal(3)



Exibindo o nome do objeto:

.. code-block:: python

    print(bar.__name__)

.. code-block:: console

    <lambda>



Tipo:

.. code-block:: python

    type(bar)

.. code-block:: console

    function



Representação:

.. code-block:: python

    repr(bar)

.. code-block:: console

    '<function funcao_principal.<locals>.<lambda> at 0x7f9844527730>'



3 elevado a 2:

.. code-block:: python

    print(bar(2))

.. code-block:: console

    9



Passando o parâmetro da função principal e de lambda:

.. code-block:: python

    funcao_principal(2)(5)

.. code-block:: console

    32