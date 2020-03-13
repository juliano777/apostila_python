Módulos
*******

	Módulos são as bibliotecas de Python.
	São simples arquivos de código Python (.py) e têm que estar dentro do PYTHONPATH.

> import sys

> dir(sys)
['__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spe
c__', '__stderr__', '__stdin__', '__stdout__', '_clear_type_cache', '_current_frames', '_debugmallocstats', '_getframe'
, '_home', '_mercurial', '_xoptions', 'abiflags', 'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_mo
dule_names', 'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dont_write_bytecode', 'exc_info', '
excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'getallocatedblocks', 'get
checkinterval', 'getdefaultencoding', 'getdlopenflags', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'ge
trefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'hash_info', 'hexversion', 'implementation', 'int_info', 'int
ern', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks
', 'path_importer_cache', 'platform', 'prefix', 'setcheckinterval', 'setdlopenflags', 'setprofile', 'setrecursionlimit'
, 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info', 'version', 'version_info', 'warnoptions'
]

> print(sys.path)

['', '/usr/bin', '/usr/lib/python3.4', '/usr/lib/python3.4/plat-x86_64-linux-gnu', '/usr/lib/python3.4/lib-dynload', '/usr/local/lib/python3.4/dist-packages', '/usr/lib/python3/dist-packages']


	A primeira incidência é uma string vazia (''), o que significa ser o diretório corrente.

$ vim foo.py

# _*_ encoding: utf-8 _*_

print('Este arquivo, {} é um módulo!'.format(__file__))
print('Seu nome é {}.'.format(__name__))


> import foo
Este arquivo, /tmp/foo.py é um módulo!
Seu nome é foo.


$ python3 foo.py 
.. code-block:: console

    Este arquivo, foo.py é um módulo!
    Seu nome é __main__.


$ vim foo.py

# _*_ encoding: utf-8 _*_

if __name__ == '__main__':
    print('Executado a partir da linha de comando.')
else:
    print('Módulo importado.')

> import foo
Módulo importado.

> type(foo)
<class 'module'>

$ python3 foo.py
Executado a partir da linha de comando.

Recarregando um Módulo

> import importlib
> importlib.reload(foo)
.. code-block:: console

    Módulo importado.
    <module 'foo' from '/tmp/foo.py'>


$ vim foo.py

# _*_ encoding: utf-8 _*_

class Pessoa(object):
    nome = ''
    idade = 0

    def saudacao(self):
        print('Olá, meu nome é {}'.format(self.nome))

class Funcionario(Pessoa):
    matricula = ''

def cubo(x):
    return x ** 3


Recarregando um módulo

> importlib.reload(foo)

.. code-block:: console

    <module 'foo' from '/tmp/foo.py'>

> f1 = foo.Funcionario()
> f1.nome = 'Chiquinho'
> f1.saudacao()
.. code-block:: console

    Olá, meu nome é Chiquinho

> print(foo.cubo(7))

.. code-block:: console

    343





import as ...

> import foo as meu_modulo
> f1 = meu_modulo.Funcionario()
> f1.matricula = 'xyz12345'
> print(f1.matricula)
.. code-block:: console

    xyz12345


from módulo import ...

.. code-block:: python

    from foo import Funcionario
    f1 = Funcionario()
    f1.nome = 'Chiquinho'
    f1.saudacao()

.. code-block:: console

    Olá, meu nome é Chiquinho