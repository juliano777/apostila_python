Tipos de Dados
**************

	Os tipos em Python podem ser mutáveis ou imutáveis, ou seja, permitem ou não alterar seu conteúdo.
	Todos os tipos de dados são objetos, pois não existem tipos primitivos em Python.
    O tipo de dado de um objeto é determinado em tempo de execução e não há uma declaração explícita como se vê em outras linguagens.



Criação de um objeto e verificando seu tipo:

.. code-block:: python

    # Atribuir um inteiro à variável (objeto) "x":
    x = 7

    # Verificar o tipo de "x":
    type(x)

.. code-block:: console

    int


Variáveis
---------

	São criadas através de atribuição de valor e quando não existem mais referência a elas são destruídas pelo garbage colector.
	Seus nomes devem começar por uma letra (não acentuadas) ou por underline "_".

Tipagem Dinâmica
~~~~~~~~~~~~~~~~

    No mesmo código pode ter objetos diferentes com o mesmo nome.
    Como dito anteriormente, o tipo é determinado na execução e um mesmo nome pode ter tipos diferentes ao longo do código, porém na verdade será outro objeto.


.. code-block:: python

    # Criação de dois objetos de mesmo nome
    x = 3.7

    # Exibir o id de "x": 
    id(x)

.. code-block:: console

    140291958334736

.. code-block:: python

    # Qual é o tipo de "x":
    type(x)

.. code-block:: console

    float

.. code-block:: python

    # Atribuir uma string à variável "x":
    x = 'foo'

    # Verificar a id de "x":
    id(x)

.. code-block:: console

    140292017787768

.. code-block:: python

    # Qual é o tipo de "x":
    type(x)

.. code-block:: console

    str

Foram criados dois objetos "x", sendo o primeiro float e o segundo uma string.
Nota-se ao redefinir o valor do objeto o mesmo deixou de existir (garbagem collector) criando um novo objeto.


Tipagem Forte
~~~~~~~~~~~~~

    A tipagem em Python além de dinâmica ela é forte.
    Em casos de operações matemáticas, por exemplo, é necessário fazer um cast para ser possível quando os tipos são incompatíveis.

.. code-block:: python

    # Soma entre um um número de ponto flutuante e um inteiro
    5.0 + 2

.. code-block:: console

    7.0

.. code-block:: python

    # Tentativa de soma entre uma string e um inteiro
    '5' + 2

.. code-block:: console

    TypeError: must be str, not int


Ocorreu um erro, pois foi feita uma tentativa de somar uma string com um inteiro.
Para isso ser possível é necessário fazer um cast da string para um valor numérico (quando for compatível, é claro).

.. code-block:: python

    # Soma utilizando cast
    int('5') + 2

.. code-block:: console

    7