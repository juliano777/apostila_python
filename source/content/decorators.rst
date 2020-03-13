Decoradores em Python
*********************

    É um conceito diferente do conceito decorator de design pattern.
    Pode ser implementado como uma classe ou como uma função.
    Modificam funções.
    É identificado da seguinte forma: @nome_do_decorador.
    Deve ser inserido na linha anterior da definição.
    Um decorador deve ser executável, ou seja, deve ter o método __call__().
    São envelopes de função.
    Decoradores podem ser definidos como classes ou funções.

Decoradores de Funções
----------------------

Classe como decorador:

.. code-block:: python

    class Decorador(object):
        
        def __init__(self, funcao):
            '''        
            O parâmetro "funcao" é a função que será decorada.
            '''

            print('Método __init__() do decorador')  # Mensagem ao instanciar
            funcao()  # Executa a função ao instanciar
        
        def __call__(self):    
            print('Método __call__() do decorador')



Definição da classe com decorador:
      
.. code-block:: python

    @Decorador
    def funcao_decorada():
        print('Dentro da função decorada')


.. code-block:: console

    Método __init__() do decorador
    Dentro da função decorada

O método construtor do decorador é invocado logo após da definição da função
decorada.
No exemplo, a própria função, que é usada como parâmetro, é invocada pelo
método construtor __init__().



Execução da função decorada:

.. code-block:: python

    funcao_decorada()

.. code-block:: console

    Método __call__() do decorador



Recriação da classe decoradora:

.. code-block:: python

    class Decorador(object):
        def __init__(self, funcao):
            print('Método __init__() do decorador')
            self.funcao = funcao

        def __call__(self):        
            print('Método __call__() do decorador')
            self.funcao()

Diferente da criação da classe anteriormente, aqui a função não é chamada
no método construtor, mas sim no método __call__.



Definição da função decorada:

.. code-block:: python

    @Decorador
    def funcao_decorada():
        print('Dentro da função')

.. code-block:: console

    Método __init__() do decorador



Execução da função decorada:

.. code-block:: python

    funcao_decorada()

.. code-block:: console

    Método __call__() do decorador
    Dentro da função



Decorador com Argumentos
------------------------

    Para funções decoradas que têm argumentos.



Criação da classe decoradora:

.. code-block:: python

    class Decorador():

        def __init__(self, f):
            print('Método __init__() do decorador')
            self.f = f

        def __call__(self, *args, **kargs):        
            print('Método __call__() do decorador')
            return self.f(*args, **kargs)



Definição da classe decorada:

.. code-block:: python

    @Decorador
    def soma(x, y):
        return x + y



Execução da classe decorada:

.. code-block:: python

    print(soma(2, 5))

.. code-block:: console

    Método __call__() do decorador
    7



Função como Decorador
---------------------

    Até então foram vistos exemplos de decoradores definidos como classes, agora serão vistos os definidos como função.



Criação da função decoradora, o decorador em si:

.. code-block:: python

    def funcao_decoradora(funcao):
    
        # Função auxiliar
        def funcao_auxiliar():
        print('Antes da função decorada')
        funcao()
        print('Depois da função decorada')
        
        return funcao_auxiliar



Definição da função decorada:

.. code-block:: python

    @funcao_decoradora
    def foo():
        print('Função decorada')



Execução da função decorada:
  
.. code-block:: python

    foo() 

.. code-block:: console

    Antes da função decorada
    Função decorada
    Depois da função decorada



Podemos também aplicar mais de um decorador a uma função:

.. code-block:: python

    # Função para itálico em HTML
    def to_italic(funcao):
        def funcao_auxiliadora(*args, **kargs):
            return '<i>' + funcao(*args, **kargs) + '</i>'
        return funcao_auxiliadora

    # Função para negrito em HTML
    def to_bold(funcao):
        def funcao_auxiliadora(*args, **kargs):
            return '<b>' + funcao(*args, **kargs) + '</b>'
        return funcao_auxiliadora



Definição da função decorada com dois decoradores:

.. code-block:: python

    @to_italic
    @to_bold
    def fc_msg(msg):
        return msg



Execução da função decorada:

.. code-block:: python

    fc_msg('Hello, World!')

.. code-block:: console

    '<i><b>Hello, World!</b></i>'


Memoização
----------

    Texto...



Criação do decorador de memoização:

.. code-block:: python

    def memoize(f):
        '''
        Memoize function (as decorator)
        '''

        # dictionary (cache)
        mem = {}

        ''' Helper function '''
        def memoizer(*param):
            key = repr(param)
            if not key in mem:
                mem[key] = f(*param)
            return mem[key]
        return memoizer



Criação da função decorada com memoização aplicada para Fibonacci:

.. code-block:: python

    @memoize
    def fibo(n):
        if (n < 2): return n
        else:
            return fibo(n - 1) + fibo(n - 2)



Execução da função decorada:

.. code-block:: python

    fibo(39)

.. code-block:: console

    63245986