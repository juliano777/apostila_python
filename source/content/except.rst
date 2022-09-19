Exceções
********

.. https://docs.python.org/3/tutorial/errors.html
.. https://docs.python.org/3/library/exceptions.html


**Blocos de Comandos**:

- | `try`: Tenta executar o bloco de comandos;
- | `except`: Em outras linguagens de programação é conhecido como "catch",
  | captura e trata a exceção;
- | `else`: Só é executado se não tiver nenhuma exceção;
- | `finally`: Tendo exceção ou não é executado de qualquer jeito.

::

                        try:
                         | 
                   Lançou exceção?   
                        / \                    
                  Sim  /   \  Não
                      /     \
                     /       \
                  except:   else: 
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



Tratamento geral para exceções:

.. code-block:: python

    try:
        print(1 / 0)  # print "malicioso" com divisão por zero

    # Captura todas exceções: generalista
    except:
        print('\n\nOcorreu um erro!\n\n')

.. code-block:: console

    Ocorreu um erro!

Dizer que ocorreu um erro não diz muita coisa...  
  
  
Utilizando try e capturando uma exceção específica para divisão por zero:

.. code-block:: python

    try:
        print(1 / 0)
    # specified exception
    except ZeroDivisionError:
        print('\n\nErro: Não dividirás por zero!\n\n')


.. code-block:: console

    Erro: Não dividirás por zero!


Tratamento de erro específico para índice de elementos:

.. code-block:: python

    # Tupla com três elementos
    numeros = ('zero', 'um', 'dois')

    try:                            
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])  # ! quarto elemento
    except IndexError:    
        print('\n\nERRO: Índice não encontrado\n\n')
   
.. code-block:: console

    zero
    um
    dois

    ERRO: Índice não encontrado



Agora exibindo além da mensagem customizada, a mensagem original de erro:

.. code-block:: python

    try:                            
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])  # ! quarto elemento
    except IndexError, e:    
        print(f'\n\nERRO: Índice não encontrado\n\n{e}')

.. code-block:: console

    zero
    um
    dois


    ERRO: Índice não encontrado

    tuple index out of range

O "e" é a mensagem de erro "tuple index out of range"



Com o editor vim ou outro de sua preferência criar o script Python:

.. code-block:: bash

    $ vim excecao.py

.. code-block:: python

    #_*_ encoding: utf-8 _*_

    # Do módulo sys importar a função exit dando um apelido
    from sys exit as sys_exit

    # Tupla de três elementos
    numeros = ('zero', 'um', 'dois')

    try:
        print(numeros[0])
        print(numeros[1])
        print(numeros[2])
        print(numeros[3])  # ! quarto elemento

    except IndexError, e:
        # Mensagem para a saída de erro
        print(file=sys.stderr, f'\n\nERRO: Índice não encontrado!\n\n{e}')
        
        # Retorno 1 do script em caso de exceção
        sys_exit(1)



Execução do script:

.. code-block:: bash

    python excecao.py

.. code-block:: console

    zero
    um
    dois


    ERRO: Índice não encontrado

    tuple index out of range


Exibe o código de execução:

.. code-block:: bash

    echo $?

.. code-block:: console

    1

Nota-se que o código foi 1, de acordo com o passado para a função exit do módulo sys.    


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

O comando `raise` é uma facilidade dada ao programador para forçar uma exceção
específica.  Muito útil para testar tratamentos de exceções.

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
