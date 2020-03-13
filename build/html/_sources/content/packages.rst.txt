Pacotes
*******


Criação de diretório (pacote):

.. code-block:: bash

    mkdir pack_0



Criação de um módulo dentro do pacote:

.. code-block:: bash

    vim pack_0/foo.py

.. code-block:: python

    # _*_ encoding: utf-8 _*_

    print(__name__)

    
    class Pessoa(object):
        nome = ''
        idade = 0

        def saudacao(self):
            print('Olá, meu nome é {}'.format(self.nome))

    class Funcionario(Pessoa):
        matricula = ''

    def cubo(x):
        return x ** 3



import pacote.modulo:

.. code-block:: python

    import pack_0.foo
    f1 = pack_0.foo.Funcionario()
    f1.nome = 'Zezinho'
    f1.saudacao()
    Olá, meu nome é Zezinho

$ ls pack_0/
foo.py  __init__.py  __pycache__

$ ls pack_0/__pycache__/
foo.cpython-34.pyc  __init__.cpython-34.pyc

$ file pack_0/__pycache__/foo.cpython-34.pyc 
pack_0/__pycache__/foo.cpython-34.pyc: python 3.4 byte-compiled

$ vim pack_0/__init__.py

# _*_ encoding: utf-8 _*_

if __name__ != '__main__':
    print('Pacote {} importado'.format(__name__))

> import pack_0.foo
Pacote pack_0 importado
pack_0.foo

> import pack_0
Pacote pack_0 importado

$ mkdir -p pack_0/pack_1/pack_2

$ mv pack_0/foo.py pack_0/pack_1/pack_2/

> import pack_0.pack_1.pack_2.foo
Pacote pack_0 importado
pack_0.pack_1.pack_2.foo

> f1 = pack_0.pack_1.pack_2.foo.Funcionario()

Apesar de terem sido declarados, os diretórios pack_1 e pack_2 não são pacotes.


Transformando os subdiretórios em pacotes:

$ > pack_0/pack_1/__init__.py
$ > pack_0/pack_1/pack_2/__init__.py

> from pack_0.pack_1.pack_2 import foo
Pacote pack_0 importado
pack_0.pack_1.pack_2.foo
> f1 = foo.Funcionario()

> from pack_0.pack_1.pack_2.foo import Funcionario
Pacote pack_0 importado
pack_0.pack_1.pack_2.foo
> f1 = Funcionario()

$ echo 'print(__name__)' > pack_0/pack_1/__init__.py 
$ echo 'print(__name__)' > pack_0/pack_1/pack_2/__init__.py


> from pack_0.pack_1.pack_2.foo import Funcionario
Pacote pack_0 importado
pack_0.pack_1
pack_0.pack_1.pack_2
pack_0.pack_1.pack_2.foo


> from pack_0.pack_1.pack_2.foo import *
Pacote pack_0 importado
pack_0.pack_1
pack_0.pack_1.pack_2
pack_0.pack_1.pack_2.foo
> f1 = Funcionario()

$ python3 pack_0/__pycache__/foo.cpython-34.pyc 

__main__