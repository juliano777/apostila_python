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


texto = ''

if not texto:
    print('A string é vazia!')

A string é vazia!


x = 1

y = 2



if x > y:
    print('X é maior')
else:    
    print('Y é maior')
    
Y é maior

y = 1

x = 1

if x > y:
    print('X é maior')
elif x < y:    
    print('Y é maior')
else:    
    print('Valores iguais')
    
Valores iguais




x = 10

if (x > 5):
    y = 3
else:
    y = 0


y = (50 if (x > 5) else 40)

print(y)
50




if Ternário

nota = float(input('Digite a nota do aluno: '))
Digite a nota do aluno: 8

estado = 'aprovado' if nota >= 7 else 'reprovado'

print('Aluno {}!'.format(estado))
Aluno aprovado!




num = int(input('Digite um número: '))
Digite um número: -2

sinal = 'positivo' if num > 0 else 'negativo' if num < 0 else 'zero'

print('O número é {}'.format(sinal))
O número é negativo




continue


break