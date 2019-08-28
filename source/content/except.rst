Exceções
Exceções
********

https://docs.python.org/2/tutorial/errors.html
https://docs.python.org/2/library/exceptions.html

Blocos de Comandos:

try: Tenta executar o bloco de comandos.

except: Em outras linguagens de programação é conhecido como "catch", captura e trata a exceção.

else: Só é executado se não tiver nenhuma exceção.

finally: Tendo exceção ou não é executado de qualquer jeito.


                        try:
                         | 
                   | Deu erro? |
                        / \                    
                  sim  /   \ não
                      /     \
                     /       \
                 else:         except:
                     \       /
                      \     /
                       \   /
                        \ /
                      finally:


raise
-----



The class hierarchy for built-in exceptions is:

BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration
      +-- StandardError
      |    +-- BufferError
      |    +-- ArithmeticError
      |    |    +-- FloatingPointError
      |    |    +-- OverflowError
      |    |    +-- ZeroDivisionError
      |    +-- AssertionError
      |    +-- AttributeError
      |    +-- EnvironmentError
      |    |    +-- IOError
      |    |    +-- OSError
      |    |         +-- WindowsError (Windows)
      |    |         +-- VMSError (VMS)
      |    +-- EOFError
      |    +-- ImportError
      |    +-- LookupError
      |    |    +-- IndexError
      |    |    +-- KeyError
      |    +-- MemoryError
      |    +-- NameError
      |    |    +-- UnboundLocalError
      |    +-- ReferenceError
      |    +-- RuntimeError
      |    |    +-- NotImplementedError
      |    +-- SyntaxError
      |    |    +-- IndentationError
      |    |         +-- TabError
      |    +-- SystemError
      |    +-- TypeError
      |    +-- ValueError
      |         +-- UnicodeError
      |              +-- UnicodeDecodeError
      |              +-- UnicodeEncodeError
      |              +-- UnicodeTranslateError
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



print(1 / 0)


---------------------------------------------------------------------------
ZeroDivisionError                         Traceback (most recent call last)
<ipython-input-18-79ea940cf5e7> in <module>()
----> 1 print('Resultado = %s' % (x / y))

ZeroDivisionError: integer division or modulo by zero


try:
    print(1 / 0)

# catch all exceptions
except:
    print('\n\nErro: Não dividirás por zero!\n\n')

Erro: Não dividirás por zero!




try:
    print(1 / 0)
# specified exception
except ZeroDivisionError:
    print('\n\nErro: Não dividirás por zero!\n\n')

Erro: Não dividirás por zero!



numeros = ('zero', 'um', 'dois')

In [10]: try:                            
    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print(numeros[3])
except IndexError:    
    print('\n\nERRO: Índice não encontrado\n\n')
   
zero
um
dois


ERRO: Índice não encontrado


try:                            
    print(numeros[0])
    print(numeros[1])
    print(numeros[2])
    print(numeros[3])
except IndexError, e:    
    print('\n\nERRO: Índice não encontrado\n\n%s' % e)
   ....:     
zero
um
dois


ERRO: Índice não encontrado

tuple index out of range


O "e" é a mensagem de erro "tuple index out of range"



$ vim excecao.py

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


$ python excecao.py 
zero
um
dois


ERRO: Índice não encontrado

tuple index out of range


$ echo $?
1



$ vim excecao3.py

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



$ python3 excecao3.py 

zero
um
dois


ERRO: Índice não encontrado

tuple index out of range



$ echo $?
1



f = open('/tmp/blablabla.txt', 'r')

---------------------------------------------------------------------------
IOError                                   Traceback (most recent call last)
<ipython-input-20-11fa3db68c79> in <module>()
----> 1 f = open('/tmp/blablabla.txt', 'r')

IOError: [Errno 2] No such file or directory: '/tmp/blablabla.txt'


try:
    f = open('/tmp/blablabla.txt', 'r')
except IOError as e:
    print('O arquivo não existe!')


O arquivo não existe!


type(e)
IOError

dir(e)

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

repr(e)

"IOError(2, 'No such file or directory')"


e.<TAB>
e.args      e.errno     e.filename  e.message   e.strerror 

print(e.errno)
2



$ vim excecao.py


#_*_ encoding: utf-8 _*_

import sys 

try:    
    f = open('/tmp/blablabla.txt', 'r')
 
except IOError as e:       
    print >> sys.stderr, '\n\nERRO: Arquivo não encontrado\n\n%s' % e 
    sys.exit(e.errno)



$ python excecao.py 


ERRO: Arquivo não encontrado

[Errno 2] No such file or directory: '/tmp/blablabla.txt'

$ echo $?
2





$ vim excecao3.py


#_*_ encoding: utf-8 _*_

import sys 

try:    
    f = open('/tmp/blablabla.txt', 'r')
 
except IOError as e:       
    print('\n\nERRO: Arquivo não encontrado\n\n%s' % e, file = sys.stderr) 
    sys.exit(e.errno)



$ python3 excecao3.py 


ERRO: Arquivo não encontrado

[Errno 2] No such file or directory: '/tmp/blablabla.txt'

$ echo $?
2




else



$ vim excecao.py

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



$ python excecao.py /tmp/blablabla.txt
Não existe o arquivo

$ > /tmp/blablabla.txt

$ python excecao.py /tmp/blablabla.txt
Sim, o arquivo existe!

$ rm /tmp/blablabla.txt


finally


$ vim excecao.py

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



$ python excecao.py /tmp/blablabla.txt
Não existe o arquivo
Se deu certo ou errado, o programa termina aqui :/

$ > /tmp/blablabla.txt

$ python excecao.py /tmp/blablabla.txt
Sim, o arquivo existe!
Se deu certo ou errado, o programa termina aqui :/



raise

raise Exception('Provocando uma exceção')
---------------------------------------------------------------------------
Exception                                 Traceback (most recent call last)
<ipython-input-62-69ebfeaaf513> in <module>()
----> 1 raise Exception('Provocando uma exceção')

Exception: Provocando uma exceção


try:
    raise ZeroDivisionError()
except IOError:
    print('Exceção IOError')
except IndexError:    
    print('Exceção IndexError')
except:
    print('Exceção não declarada')

Exceção não declarada


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

Exceção ZeroDivisionError


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

Exceção ZeroDivisionError


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

	Para criarmos uma exceção personalizada preciamos criar uma classe que herde de uma outra classe de exceção, cuja raiz é Exception.


class FooException(Exception):
    pass


try:
    raise FooException('Bla bla bla')
except Exception as e:
    print('Erro ------> %s' % e)

Erro ------> Bla bla bla



class EggsException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return self.value

try:
    raise EggsException(50)
except EggsException as e:
    print('Ocorreu um erro da minha exceção, cujo valor é %s' % (e.value))


Ocorreu um erro da minha exceção, cujo valor é 50



raise EggsException('bla bla bla')

---------------------------------------------------------------------------
EggsException                             Traceback (most recent call last)
<ipython-input-14-4cafda692601> in <module>()
----> 1 raise EggsException('bla bla bla')

EggsException: bla bla bla






















