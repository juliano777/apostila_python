Lista
*****

    Uma lista é uma estrutura de dados similar ao tradicional array que tem em
    outras linguagens, porém seus elementos podem ser de tipos diferentes.
    Uma lista é também uma coleção de dados mutável, pois sua estrutura pode ser mudada.



Formas de criar uma lista vazia:

.. code-block:: python

    l = []

ou 

.. code-block:: python

    l = list()



Formas de criar uma lista com elementos:

.. code-block:: python

    l = list([1, 2, 3])

ou

.. code-block:: python

    l = [1, 2, 3]



Declaração de uma nova lista:

.. code-block:: python

    x = ['a', 'b', 3, 4.0]



Exibindo o terceiro elemento da lista:

.. code-block:: python

    print(x[2])

.. code-block:: console

    3



Alterando o terceiro elemento da lista:

.. code-block:: python

    x[2] = 30



Exibindo o terceiro elemento da lista:

.. code-block:: python

    print(x[2])

.. code-block:: console

    30



Exibindo os elementos da lista:

.. code-block:: python

    print(x)

.. code-block:: console

    ['a', 'b', 30, 4.0]



Existe "7" na lista?:

.. code-block:: python

    7 in x

.. code-block:: console

    False



Existe "3" na lista?:

.. code-block:: python

    3 in x

.. code-block:: console

    True



O método append adiciona um elemento ao final da lista:

.. code-block:: python

    x.append('Uma string qualquer...')



Exibindo os elementos da lista:

.. code-block:: python

    print(x)

.. code-block:: console

    ['a', 'b', 30, 4.0, 'Uma string qualquer...']



O método extend faz com que os elementos de outra lista sejam adicionadas a
uma lista atual:

.. code-block:: python

    foo = ['a', 'b', 'c']  # Definição da primeira lista
    bar = [1, 2]  # Definição da segunda lista
    foo.extend(bar)  # Extendendo a primeira lista com os elementos da segunda
    print(foo)  # Exibindo a lista extendida

.. code-block:: console

    ['a', 'b', 'c', 1, 2]



O operador "+" sendo utilizado para criar uma nova lista a partir de outra somada à outra:

.. code-block:: python

    y = x + ['abobrinha', '7', {'chave': 'valor'}, ('SP', 'MG', 'PR', 'RO')]



Exibindo a nova lista:

.. code-block:: python

    y

.. code-block:: python

    ['a',
     'b',
     30,
     4.0,
     'Uma string qualquer...',
     'abobrinha',
     '7',
     {'chave': 'valor'},
     ('SP', 'MG', 'PR', 'RO')]



Utilizando "+=" como um atalho para o método extend e exibindo seu novo conteúdo:

.. code-block:: python

    x += ['xyz']
    x

.. code-block:: console

    ['a', 'b', 30, 4.0, 'Uma string qualquer...', 'xyz']



Removendo um elemento da lista e exibindo seu novo conteúdo:

.. code-block:: python

    x.remove('xyz')
    x

.. code-block:: console

    ['a', 'b', 30, 4.0, 'Uma string qualquer...']



Método extend com uma lista como parâmetro:

.. code-block:: python

    x.extend(['xyz'])
    x

.. code-block:: console

    ['a', 'b', 30, 4.0, 'Uma string qualquer...', 'xyz']



Método extend com uma string como parâmetro:

.. code-block:: python

    x.extend('xyz')
    x

.. code-block:: console

    ['a', 'b', 30, 4.0, 'Uma string qualquer...', 'xyz', 'x', 'y', 'z']

Ao utilizarmos uma string como parâmetro do método extend, a string foi
convertida em lista de forma a transformar cada caractere em elemento
de uma lista.



Método append:

.. code-block:: python

    x.append('xyz')
    x

.. code-block:: console

    ['a', 'b', 30, 4.0, 'Uma string qualquer...', 'xyz', 'x', 'y', 'z', 'xyz']

Aqui podemos ver claramente a diferença entre os métodos extend e append, que
pode causar uma certa confusão inicial para quem está iniciando em Python.
Nota-se que o método append adicionou a string inteira como um novo elemento
da lista.




Extendendo a lista com o operador "+=":

.. code-block:: python

    x += 'String'
    x

.. code-block:: console

    ['a',
    'b',
    30,
    4.0,
    'Uma string qualquer...',
    'xyz',
    'x',
    'y',
    'z',
    'xyz',
    'S',
    't',
    'r',
    'i',
    'n',
    'g']

Como o operador "+=" ser um atalho para o método extend ele transformou a
string numa lista, uma lista cujos elementos são os caracteres da string.



Tentativa de utilizar o operador "+" em uma lista:

.. code-block:: python

    x + 'bla bla bla'

.. code-block:: console

    TypeError: can only concatenate list (not "str") to list

Não se pode concatenar uma lista com uma string.



Criação de uma nova lista a partir de uma string:

.. code-block:: python

    z = list('Hobbit')
    z

.. code-block:: console

    ['H', 'o', 'b', 'b', 'i', 't']



Novamente o método append:

.. code-block:: python

    z.append('Hobbit')
    z

.. code-block:: console

    ['H', 'o', 'b', 'b', 'i', 't', 'Hobbit']



Qual o tamanho (quantos elementos) da lista?

.. code-block:: python

    len(z)

.. code-block:: console

    7

Tamanho 7, posições variam de 0 a 6.



Método insert utilizando a priemira posição (0):

.. code-block:: python

    z.insert(0, 'Gandalf')
    z

.. code-block:: console

    ['Gandalf', 'H', 'o', 'b', 'b', 'i', 't', 'Hobbit']



Pode-se também verificar o tamanho de uma lista com o dunder len:

.. code-block:: python

    z.__len__()

.. code-block:: console

    8



Dado que a lista tem 8 (oito) elementos, inserir num novo elemento na nona (8) posição:

.. code-block:: python

    z.insert(8, 'Bilbo')
    z

.. code-block:: console

    ['Gandalf', 'H', 'o', 'b', 'b', 'i', 't', 'Hobbit', 'Bilbo']

O efeito foi o mesmo que utilizar o método append.



O método pop sem parâmetros retorna o último elemento e o apaga da lista:

.. code-block:: python

    z.pop()

.. code-block:: console

    'Bilbo'


.. code-block:: python

    z


.. code-block:: console

    ['Gandalf', 'H', 'o', 'b', 'b', 'i', 't', 'Hobbit']



Como o método pop retorna o último elemento, o mesmo pode ser utilizado para atribuição:

.. code-block:: python

    livro = ('O {}'.format(z.pop()))
    livro

.. code-block:: console

    'O Hobbit'



Retornando e apagando o sexto elemento:

.. code-block:: python

    z.pop(5)

.. code-block:: console

    'i'




Método sort, organiza a lista com seus elementos pela ordem alfabética:

.. code-block:: python

    z.sort()
    z



.. code-block:: console

    ['Gandalf', 'H', 'b', 'b', 'i', 'o', 't']



O método reverse pega a atual posição dos elementos e reconstrói a lista
na ordem reversa:

.. code-block:: python

    z.reverse()
    z

.. code-block:: python

    ['t', 'o', 'b', 'b', 'H', 'Gandalf']



A função sorted não altera a lista, apenas retorna o conteúdo pela ordem
alfabética:

.. code-block:: python

    sorted(z)

.. code-block:: console

    ['Gandalf', 'H', 'b', 'b', 'o', 't']


.. code-block:: python

    z

.. code-block:: console

    ['t', 'o', 'i', 'b', 'b', 'H', 'Gandalf']



A função sorted também pode somente retornar o reverso de uma lista:

.. code-block:: python

    sorted([1, 2, 3], reverse=True)

.. code-block:: console

    [3, 2, 1]



Criação de uma lista a partir do retorno de sorted:

.. code-block:: python

    w = sorted(z)
    w

.. code-block:: console

    ['Gandalf', 'H', 'b', 'b', 'o', 't']

.. code-block:: python

    z

.. code-block:: console

    ['t', 'o', 'b', 'b', 'H', 'Gandalf']



A função reversed() sempre retorna um iterador:

> reversed(z)

<listreverseiterator object at 0x1653c10>



Convertendo para lista o iterador gerado pela função reversed:

.. code-block:: python

    z = list(reversed(z))
    z

.. code-block:: console

    ['Gandalf', 'H', 'b', 'b', 'o', 't']



Função sorted transforma a string numa lista e organiza por ordem
alfabética:

.. code-block:: python

    sorted('aAcb')

.. code-block:: console

    ['A', 'a', 'b', 'c']



Função sorted transforma a string numa lista e organiza por ordem alfabética:

.. code-block:: python

    sorted('aAcb', reverse=True)

.. code-block:: console

    ['c', 'b', 'a', 'A']



Função reversed transforma a string em uma lista com seus caracteres em ordem
reversa:

.. code-block:: python

    list(reversed('aAcb'))

.. code-block:: console

    ['b', 'c', 'A', 'a']



Definição de lista com 3 (três) elementos:

.. code-block:: python

    x = [1, 2, 3]



A partir da lista "x", atribuir respectivamente seus elementos como valores
para as variáveis à esquerdae exibir seus valores:

.. code-block:: python

    a, b, c = x
    print(a)

.. code-block:: console

    1

.. code-block:: python

    print(b)

.. code-block:: console

    2

.. code-block:: python

    print(c)

.. code-block:: console

    3



E se a quantidade de variáveis que receberão os valores forem em menor
número que a quantidade de elementos da lista?:

.. code-block:: python

    y, z, = x

.. code-block:: console

    ValueError: too many values to unpack (expected 2)

Lista com três elementos não pode fazer atribuição respectiva a apenas
duas variáveis.



Utilização do caractere underscore como solução:

.. code-block:: python

    y, z, _ = x
    print(y)

.. code-block:: console

    1


.. code-block:: python

    print(z)

.. code-block:: console

    2