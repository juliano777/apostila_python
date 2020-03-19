Iteratoradores e Geradores
**************************

Iterator
--------


    Um iterator (iterador) permite acessar elementos de uma coleção / sequência, retornando cada elemento sequencialmente.
    Todo objeto que tiver o método __next__() é um iterator.



Criação de um iterator com uma string:

.. code-block:: python

    it = iter('bar')



Representação:

.. code-block:: python

    repr(it)

.. code-block:: console

    '<iterator object at 0x7f123cd62c50>'



Executando o método __next__ até seu fim:

.. code-block:: python

    it.__next__()

.. code-block:: console

    'b'

.. code-block:: python

    it.__next__()

.. code-block:: console

    'a'

.. code-block:: python

    it.__next__()

.. code-block:: console

    'r'

.. code-block:: python

    it.__next__()

.. code-block:: console

    StopIteration:

        Bla bla bla

|   Nota-se que a iteração foi feita sobre a string declarada, de forma a 
| retornar caractere por caractere e após o último foi lançada uma exceção
| indicando que não há mais elementos a serem retornados.



Classe Iterator
---------------

    É possível também implementar um iterador como um objeto de uma classe personalizada.
    É necessário implementar os métodos __iter__ e __next__.
    __iter__ retorna o objeto iterador por si.
    __next__ retorna o próximo item da coleção e ao alcançar o fim e se houver uma chamada sequente uma exceção é lançada (StopIteration).



Criação da classe de iterador:

.. code-block:: python

    class FirstNumbers(object):

    def __init__(self, n):
        self.n = n
        self.i = 0
    
    def __iter__(self):
        return self
    
    
    def __next__(self):
        if self.i <= self.n:
            cur = self.i
            self.i += 1
            return cur
        else:
            raise StopIteration()



Somatória dos 10 primeiros números:

.. code-block:: python

    print(sum(FirstNumbers(10)))

.. code-block:: console

    45



Generator

    Um generator é um objeto iterável assim como um iterator, mas nem todo iterator é um generator.
    Funções de generator permite declarar uma função que se comporta como um iterador, podendo ser usadas em loops.
    Um generator implementa o conceito de lazy evaluation, o que faz com que em determinadas situações economize-se recursos de processamento, pois cada elemento é processado conforme a demanda.



Criando um objeto range que vai de 0  a 9:

.. code-block:: python

    numeros = range(0, 10)



Se for utilizado list comrprehension será gerada uma lista:

.. code-block:: python

    rq = [x ** 2 for x in numeros]



Verificando os elementos:

.. code-block:: python

    rq

.. code-block:: console

    [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]



Verificando o tipo:

.. code-block:: python

    type(rq)

.. code-block:: console

    list



Tuple comprehension é uma maneira de se criar um generator:

.. code-block:: python

    rq = (x ** 2 for x in numeros)



Verificando o tipo do objeto:

.. code-block:: python

    type(rq)

.. code-block:: console

    generator



Executando o método dunder next até o fim dos elementos:

.. code-block:: python

    rq.__next__()

.. code-block:: console

    0

.. code-block:: python

    rq.__next__()

.. code-block:: console

    1

. . .

.. code-block:: console

    81

.. code-block:: python

    rq.__next__()

.. code-block:: console

    StopIteration:

        Bla bla bla



Funções Generator

    Uma função generator utiliza o comando yield em vez de return, o que faz com que retorne o próximo elemento da sequência.



Criação de uma função generator:

.. code-block:: python

    def gen():

    i = 0

    while i < 10:
        yield i
        i += 1



Criação do gerador via execução da função:

.. code-block:: python

    x = gen()



Verificando os tipos:

.. code-block:: python

    type(gen)

.. code-block:: console

    function

.. code-block:: python

    type(x)

.. code-block:: console

    generator



Execução do método __next__ até o fim:

.. code-block:: python

    x.__next__()

.. code-block:: console

    0

. . . 

.. code-block:: python

    x.__next__()

.. code-block:: console

    9

.. code-block:: python

    x.__next__()

.. code-block:: console

    StopIteration:



Iterator vs Generator

    - Para criar um generator utilizamos ou uma função com yield no lugar de return ou tuple comprehension.
    Para criar um iterador utilizamos a função iter();

    - Generator utiliza yield, iterator não;

    - Gerador salva o estado de variáveis locais a cada vez que o yield pausa o loop. Um iterador não faz uso de variáveis locais, tudo o que ele precisa é faz a iteração.

    - Iteradores fazem uso mais eficiente de memória.



Do módulo timeit importar a função de mesmo nome:

.. code-block:: python

    from timeit import timeit



Verificação de tipos:

.. code-block:: python

    type(iter([x for x in range(1, 1001)]))

.. code-block:: console

    list_iterator

.. code-block:: python

    type((x for x in range(1, 1001)))

.. code-block:: console

    generator



Strings com código em loop sobre iterador e gerador, respectivamente:

.. code-block:: python

    code_it = '''                                
for i in (iter([x for x in range(1, 1001)])):
    pass
'''

.. code-block:: python

    code_gen = '''                                
for i in ((x for x in range(1, 1001))):
    pass
'''



Cronometrando os códigos de iterador e gerador, respectivamente:

.. code-block:: python

    timeit(code_it)

.. code-block:: console

    42.666774257901125

.. code-block:: python

    timeit(code_gen)

.. code-block:: console

    53.58039242995437