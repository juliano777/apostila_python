Exceções
********

.. https://docs.python.org/3/tutorial/errors.html
.. https://docs.python.org/3/library/exceptions.html


**Blocos de Comandos**:

- | try: Tenta executar o bloco de comandos;
- | except: Em outras linguagens de programação é conhecido como "catch",
  | captura e trata a exceção;
- | else: Só é executado se não tiver nenhuma exceção;
- | finally: Tendo exceção ou não é executado de qualquer jeito.

::

                        try:
                         | 
                      Deu erro?
                        / \                    
                  Sim  /   \  Não
                      /     \
                     /       \
                   else:   except:
                     \       /
                      \     /
                       \   /
                        \ /
                      finally:


`Hierarquia de classes built-in de exceções <https://docs.python.org/3/library/exceptions.html>`_:

::

    BaseException
    +-- SystemExit
    +-- KeyboardInterrupt
    +-- GeneratorExit
    +-- Exception
        +-- StopIteration
        +-- StopAsyncIteration
        +-- ArithmeticError
        |    +-- FloatingPointError
        |    +-- OverflowError
        |    +-- ZeroDivisionError
        +-- AssertionError
        +-- AttributeError
        +-- BufferError
        +-- EOFError
        +-- ImportError
        |    +-- ModuleNotFoundError
        +-- LookupError
        |    +-- IndexError
        |    +-- KeyError
        +-- MemoryError
        +-- NameError
        |    +-- UnboundLocalError
        +-- OSError
        |    +-- BlockingIOError
        |    +-- ChildProcessError
        |    +-- ConnectionError
        |    |    +-- BrokenPipeError
        |    |    +-- ConnectionAbortedError
        |    |    +-- ConnectionRefusedError
        |    |    +-- ConnectionResetError
        |    +-- FileExistsError
        |    +-- FileNotFoundError
        |    +-- InterruptedError
        |    +-- IsADirectoryError
        |    +-- NotADirectoryError
        |    +-- PermissionError
        |    +-- ProcessLookupError
        |    +-- TimeoutError
        +-- ReferenceError
        +-- RuntimeError
        |    +-- NotImplementedError
        |    +-- RecursionError
        +-- SyntaxError
        |    +-- IndentationError
        |         +-- TabError
        +-- SystemError
        +-- TypeError
        +-- ValueError
        |    +-- UnicodeError
        |         +-- UnicodeDecodeError
        |         +-- UnicodeEncodeError
        |         +-- UnicodeTranslateError
        +-- Warning
            +-- DeprecationWarning
            +-- PendingDeprecationWarning
            +-- RuntimeWarning
            +-- SyntaxWarning
            +-- UserWarning
            +-- FutureWarning
            +-- ImportWarning
            +-- UnicodeWarning
            +-- BytesWarning
            +-- ResourceWarning



Forçando um erro dividindo por zero:

.. code-block:: python

    print(1 / 0)

.. code-block:: console

    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-18-79ea940cf5e7> in <module>()
    ----> 1 print('Resultado = %s' % (x / y))

    ZeroDivisionError: integer division or modulo by zero



bla bla bla:

.. code-block:: python

    try:
        print(1 / 0)

    # catch all exceptions
    except:
        print('\n\nErro: Não dividirás por zero!\n\n')

.. code-block:: console

    Erro: Não dividirás por zero!



Utilizando try e forçando um erro de divisão por zero:

.. code-block:: python

    try:
        print(1 / 0)
    # specified exception
    except ZeroDivisionError:
        print('\n\nErro: Não dividirás por zero!\n\n')


.. code-block:: console

    Erro: Não dividirás por zero!


.. code-block:: python

    numeros = ('zero', 'um', 'dois')

    try:                            
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])
    except IndexError:    
        print('\n\nERRO: Índice não encontrado\n\n')
   
.. code-block:: console

    zero
    um
    dois

    ERRO: Índice não encontrado



sasasasasa:

.. code-block:: python

    try:                            
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])
    except IndexError, e:    
        print('\n\nERRO: Índice não encontrado\n\n%s' % e)

.. code-block:: console

    zero
    um
    dois


    ERRO: Índice não encontrado

    tuple index out of range

O "e" é a mensagem de erro "tuple index out of range"



ssdsdpsdsd:

.. code-block:: bash

    $ vim excecao.py

.. code-block:: python

    #_*_ encoding: utf-8 _*_

    import sys

    numeros = ('zero', 'um', 'dois')

    try:
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])
    except IndexError, e:
        print >> sys.stderr, '\n\nERRO: Índice não encontrado\n\n%s' % e
        sys.exit(1)



sdsdsdsd:

.. code-block:: bash

    python excecao.py

.. code-block:: console

    zero
    um
    dois


    ERRO: Índice não encontrado

    tuple index out of range


ddsdsd:

.. code-block:: bash

    echo $?

.. code-block:: console

    1



sdsdsdsdsdsd:

.. code-block:: bash

    vim excecao3.py

.. code-block:: python

    #_*_ encoding: utf-8 _*_

    import sys

    numeros = ('zero', 'um', 'dois')

    try:
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])
    except IndexError as e:
        print('\n\nERRO: Índice não encontrado\n\n%s' % e, file = sys.stderr)
        sys.exit(1)



sdsdsd:

.. code-block:: bash

    python3 excecao3.py

.. code-block:: console

    zero
    um
    dois


    ERRO: Índice não encontrado

    tuple index out of range



sdsdsdsd:

.. code-block:: bash

    echo $?

.. code-block:: console

    1



sddsdsdsdsd:

.. code-block:: python

    f = open('/tmp/blablabla.txt', 'r')

.. code-block:: console

    ---------------------------------------------------------------------------
    IOError                                   Traceback (most recent call last)
    <ipython-input-20-11fa3db68c79> in <module>()
    ----> 1 f = open('/tmp/blablabla.txt', 'r')

    IOError: [Errno 2] No such file or directory: '/tmp/blablabla.txt'



sddsdsdsd:

.. code-block:: python

    try:
        f = open('/tmp/blablabla.txt', 'r')
    except IOError as e:
        print('O arquivo não existe!')

.. code-block:: python

    O arquivo não existe!



sdsdsdsd:

.. code-block:: python

    type(e)

.. code-block:: console

    IOError



sdsdssdsdsd:    

.. code-block:: python

    dir(e)

.. code-block:: console

    ['__class__',
     '__delattr__',
     '__dict__',
     '__doc__',
     '__format__',
     '__getattribute__',
     '__getitem__',
     '__getslice__',
     '__hash__',
     '__init__',
     '__new__',
     '__reduce__',
     '__reduce_ex__',
     '__repr__',
     '__setattr__',
     '__setstate__',
     '__sizeof__',
     '__str__',
     '__subclasshook__',
     '__unicode__',
     'args',
     'errno',
     'filename',
     'message',
     'strerror']



dsdsdsdsd:

.. code-block:: python

    repr(e)

.. code-block:: console

    "IOError(2, 'No such file or directory')"


sdsdsdsdsd:

.. code-block:: python

    e.<TAB>

.. code-block:: console

    e.args      e.errno     e.filename  e.message   e.strerror



sdsddssd:

.. code-block:: python

    print(e.errno)

.. code-block:: console

    2



sdsdsdsdsd:

.. code-block:: bash

    vim excecao.py

.. code-block:: python

    #_*_ encoding: utf-8 _*_

    import sys 

    try:    
        f = open('/tmp/blablabla.txt', 'r')
    
    except IOError as e:       
        print >> sys.stderr, '\n\nERRO: Arquivo não encontrado\n\n%s' % e 
        sys.exit(e.errno)



sddssd:

.. code-block:: bash

    python excecao.py

.. code-block:: console

    ERRO: Arquivo não encontrado

    [Errno 2] No such file or directory: '/tmp/blablabla.txt'



sdsdklsdkkl:

.. code-block:: bash

    echo $?

.. code-block:: console

    2



sdsdsdsdd:

.. code-block:: bash

    vim excecao3.py



.. code-block:: python

    #_*_ encoding: utf-8 _*_

    import sys 

    try:    
        f = open('/tmp/blablabla.txt', 'r')
    
    except IOError as e:       
        print('\n\nERRO: Arquivo não encontrado\n\n%s' % e, file = sys.stderr) 
        sys.exit(e.errno)



sdsdsdsdsd:

.. code-block:: bash

    python3 excecao3.py

.. code-block:: console

    ERRO: Arquivo não encontrado

    [Errno 2] No such file or directory: '/tmp/blablabla.txt'



sdsddssd:

.. code-block:: bash

    echo $?

.. code-block:: console

    2




else
----



.. code-block:: bash

    vim excecao.py

.. code-block:: python

    #_*_ encoding: utf-8 _*_

    import sys

    f = sys.argv[1]

    try:
        f = open(f, 'r')

    except IOError:
        print('Não existe o arquivo')  
        
    else:
        print('Sim, o arquivo existe!')  
        f.close()



ewowewewe:

.. code-block:: bash

    python excecao.py /tmp/blablabla.txt

.. code-block:: console

    Não existe o arquivo



ewewewewe:

.. code-block:: bash

    touch /tmp/blablabla.txt
    python excecao.py /tmp/blablabla.txt

.. code-block:: console

    Sim, o arquivo existe!



dsdsdsdsd:

.. code-block:: bash

    rm /tmp/blablabla.txt



finally
-------



.. code-block:: bash

    vim excecao.py


.. code-block:: python

    #_*_ encoding: utf-8 _*_

    import sys

    f = sys.argv[1]

    try:
        f = open(f, 'r')

    except IOError:
        print('Não existe o arquivo')  
        
    else:
        print('Sim, o arquivo existe!')  
        f.close()

    finally:
        print('Se deu certo ou errado, o programa termina aqui :/')



dsdsdsdsd:

.. code-block:: bash

    python excecao.py /tmp/blablabla.txt

.. code-block:: console

    Não existe o arquivo

Se deu certo ou errado, o programa termina aqui :/



sdsdsd:

.. code-block:: bash

    touch /tmp/blablabla.txt
    python excecao.py /tmp/blablabla.txt

.. code-block:: console

    Sim, o arquivo existe!

Se deu certo ou errado, o programa termina aqui :/


raise
-----

sasasasa:

.. code-block:: python

    raise Exception('Provocando uma exceção')

.. code-block:: console
        
    ---------------------------------------------------------------------------
    Exception                                 Traceback (most recent call last)
    <ipython-input-62-69ebfeaaf513> in <module>()
    ----> 1 raise Exception('Provocando uma exceção')

    Exception: Provocando uma exceção



saassasasa:

.. code-block:: python

    try:
        raise ZeroDivisionError()
    except IOError:
        print('Exceção IOError')
    except IndexError:    
        print('Exceção IndexError')
    except:
        print('Exceção não declarada')

.. code-block:: console

    Exceção não declarada



ewwewewe:

.. code-block:: python

    try:
        raise ZeroDivisionError('Erro de divisão por zero')
    except IOError:
        print('Exceção IOError')
    except IndexError:    
        print('Exceção IndexError')
    except ZeroDivisionError:
        print('Exceção ZeroDivisionError')
    except:
        print('Exceção não declarada')

.. code-block:: console

    Exceção ZeroDivisionError



osdkskldskl:

.. code-block:: python

    try:
        raise ZeroDivisionError('Erro de divisão por zero')
    except IOError:
        print('Exceção IOError')
    except IndexError:    
        print('Exceção IndexError')
    except ZeroDivisionError:
        print('Exceção ZeroDivisionError')
    except Exception:
        print('Exceção não declarada')

.. code-block:: console

    Exceção ZeroDivisionError



ssdsdpsdsd:

.. code-block:: python

    try:
        raise ZeroDivisionError('Erro de divisão por zero')
    except IOError:
        print('Exceção IOError')    
    except IndexError:    
        print('Exceção IndexError')
    except ZeroDivisionError:
        print('Exceção ZeroDivisionError')
        raise
    except Exception:
        print('Exceção não declarada')

.. code-block:: console

        Exceção ZeroDivisionError
    ---------------------------------------------------------------------------
    ZeroDivisionError                         Traceback (most recent call last)
    <ipython-input-77-be8b35cbd0cc> in <module>()
        1 try:
    ----> 2     raise ZeroDivisionError('Erro de divisão por zero')
        3 except IOError:
        4     print('Exceção IOError')
        5 except IndexError:

    ZeroDivisionError: Erro de divisão por zero



Exceção Personalizada
---------------------

Para criarmos uma exceção personalizada preciamos criar uma classe que herde
de uma outra classe de exceção, cuja raiz é Exception.



DSSDSDSD:

.. code-block:: python

    class FooException(Exception):
        pass

    try:
        raise FooException('Bla bla bla')
    except Exception as e:
        print('Erro ------> %s' % e)


.. code-block:: console

    Erro ------> Bla bla bla



sdsdksdsd:

.. code-block:: python

    class EggsException(Exception):
        def __init__(self, value):
            self.value = value
        def __str__(self):
            return self.value

    try:
        raise EggsException(50)
    except EggsException as e:
        print('Ocorreu um erro da minha exceção, cujo valor é %s' % (e.value))

.. code-block:: console

    Ocorreu um erro da minha exceção, cujo valor é 50



sdaasasa:

.. code-block:: python

    raise EggsException('bla bla bla')

.. code-block:: console

    ---------------------------------------------------------------------------
    EggsException                             Traceback (most recent call last)
    <ipython-input-14-4cafda692601> in <module>()
    ----> 1 raise EggsException('bla bla bla')

    EggsException: bla bla bla