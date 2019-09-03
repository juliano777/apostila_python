Booleanos
*********

    Qualquer objeto pode ser testado como um valor verdadeiro, para uso como condição em um if ou um while ou como um operando de operações "booleanas". Os seguintes valores são considerados como False: 

	False, 0, 0L, 0.0, 0j, [], (), {}, set([]), None, "" ou ''.

	Instâncias de classes definidas por usuários, se a classe define um método __bool__() ou __len__(), quando este método retornar o inteiro zero ou um valor booleano False.
	Todos outros valores são considerados verdadeiros, então objetos de muitos tipos são considerados como True.

.. code-block:: python

    # Definindo a variável como True de forma indireta
    b = bool(1)
    
    # Verificando o valor da variável
    print(b)

.. code-block:: console

    True

.. code-block:: python

    # Definindo a variável como False de forma indireta
    b = bool(0)

    # Verificando o valor da variável
    print(b)
    
.. code-block:: console

    False

.. code-block:: python

    # Teste usando a lógica OR
    .. code-block:: python

    # True | False

.. code-block:: console

    True

.. code-block:: python

    # Teste usando a lógica AND
    True & False

.. code-block:: console

    False

.. code-block:: python

    # Negação de True
    not True

.. code-block:: console

    False

.. code-block:: python

    # Negação de False
    not False

.. code-block:: console

    True

.. code-block:: python

    # Criação de classes de teste
    class Foo(object):
        def __len__(self):
            return 1

    class Bar(object):
        def __len__(self):
            return 0

.. code-block:: python

    # Criação de objetos:
    foo = Foo()
    bar = Bar()

    # Verificando o valor booleano dos objetos
    bool(foo)

.. code-block:: console

    True

.. code-block:: python

    # 
    bool(bar)

.. code-block:: console

    False

.. code-block:: python

    # True AND (NOT False)
    bool(foo) & (not bool(bar))

.. code-block:: console

    True

True AND False:

> bool(foo) & bool(bar)

.. code-block:: console

    False



Classe para testar os métodos __bool__ e __len__:

> class Spam(object):
    def __bool__(self):
        return True

    def __len__(self):
        return 0

    O método __bool__ retorna um valor verdadeiro e o método __len__ um falso.
    Com ambos declarados na mesma classe, um objeto dela o que retornará?



Criação de objeto:

> spam = Spam()


Verificando o valor booleano:

> bool(spam)

.. code-block:: console

    True

    O retorno foi verdadeiro, o método __bool__ prevalece.
