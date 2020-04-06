if / elif / else
****************

	O comando if, que inglês significa "se" indica uma condição.



Criação de dois objetos int:

.. code-block:: python

    x = 7
    y = 5



Bloco if teste se x é maior que y:

.. code-block:: python

    if x > y:
        print('X é maior')

.. code-block:: console

    X é maior



Bloco if teste se x é menor que y:

.. code-block:: python

    if x < y:
        print('Y é maior')

|   Aqui nada aconteceu, pois a condição de if não foi satisfeita.



Criação de duas variáveis booleanas:

.. code-block:: python

    foo = True
    bar = False



Modo "pythônico" de se testar um valor booleano:

.. code-block:: python

    if foo:
        print('foo é verdadeiro!')

.. code-block:: console

    foo é verdadeiro!

|   Note que não foi testado `foo == False`, utilizou-se uma maneira muito mais elegante.



Testando uma Variável booleana com negação:

.. code-block:: python

    if not bar:
        print('bar é falso!')

.. code-block:: console

    bar é falso!



Podemos também de maneira parecida, se a variável tiver um conteúdo:    

.. code-block:: python

    # Objeto string:
    texto = 'Python e PostgreSQL: Poder!'

    # Bloco if:
    if texto:
        print('A string NÃO é vazia!')


.. code-block:: console

    A string NÃO é vazia!



Teste de negação com string vazia:    

.. code-block:: python

    # String vazia:
    texto = ''

    # Bloco if:
    if not texto:
        print('A string é vazia!')

.. code-block:: console

    A string é vazia!



Boco if com else:    

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



Bloco if com elif:    

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



O valor de y depende de x:    

.. code-block:: python

    # Objeto int:
    x = 10

    # Bloco if:    
    if (x > 5):
        y = 3
    else:
        y = 0

    # Exibe o resultado
    print(y)

.. code-block:: console

    3



Operador Ternário
~~~~~~~~~~~~~~~~~

|   Um recurso bastante interessante em outras linguagens como em C, por exemplo.
|   Seu objetivo é abreviar um bloco if em apenas uma linha.

**Sintaxe**:

|   `retorno_se_verdadeiro if condição else retorno_se_falso`




Declaração de uma variável x com valor, atribui a y o resultado e exibe seu valor:

.. code-block:: python

    x = 10  # Variável int

    # Atribuição de valor condicional:
    y = (50 if (x > 5) else 40)

    # Exibe o valor de "y":
    print(y)

.. code-block:: console

    50



Variável float para receber a nota:    

.. code-block:: python

    nota = float(input('Digite a nota do aluno: '))

.. code-block:: console

    Digite a nota do aluno: 8



Atribuição condicional:

.. code-block:: python

    estado = 'aprovado' if nota >= 7 else 'reprovado'



Exibe a mensagem:

.. code-block:: python

    print(f'Aluno {estado}!')

.. code-block:: console

    Aluno aprovado!



Variável int:

.. code-block:: python

    num = int(input('Digite um número: '))

.. code-block:: console

    Digite um número: -2



Atribuição condicional:

.. code-block:: python

    sinal = 'positivo' if num > 0 else 'negativo' if num < 0 else 'zero'



Exibe mensagem:

.. code-block:: python

    print(f'O número é {sinal}'

.. code-block:: console

    O número é negativo