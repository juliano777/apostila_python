# Pacotes

Criação de diretório (pacote):

``` bash
mkdir pack_0
```

Criação de um módulo dentro do pacote:

``` bash
vim pack_0/foo.py
```

``` python
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
```

import pacote.modulo:

``` python
import pack_0.foo
f1 = pack_0.foo.Funcionario()
f1.nome = 'Zezinho'
f1.saudacao()
Olá, meu nome é Zezinho
```

\$ ls pack_0/ foo.py \_\_[init]().py \_\_pycache\_\_

\$ ls pack_0/\_\_pycache\_\_/ foo.cpython-34.pyc
\_\_init\_\_.cpython-34.pyc

\$ file pack_0/\_\_pycache\_\_/foo.cpython-34.pyc
pack_0/\_\_pycache\_\_/foo.cpython-34.pyc: python 3.4 byte-compiled

\$ vim pack_0/\_\_init\_\_.py

\# \_*\_ encoding: utf-8 \_*\_

if \_\_name\_\_ != \'\_\_main\_\_\':

:   print(\'Pacote {} importado\'.format(\_\_name\_\_))

\> import pack_0.foo Pacote pack_0 importado pack_0.foo

\> import pack_0 Pacote pack_0 importado

\$ mkdir -p pack_0/pack_1/pack_2

\$ mv pack_0/foo.py pack_0/pack_1/pack_2/

\> import pack_0.pack_1.pack_2.foo Pacote pack_0 importado
pack_0.pack_1.pack_2.foo

\> f1 = pack_0.pack_1.pack_2.foo.Funcionario()

Apesar de terem sido declarados, os diretórios pack_1 e pack_2 não são
pacotes.

Transformando os subdiretórios em pacotes:

\$ \> pack_0/pack_1/\_\_init\_\_.py \$ \>
pack_0/pack_1/pack_2/\_\_init\_\_.py

\> from pack_0.pack_1.pack_2 import foo Pacote pack_0 importado
pack_0.pack_1.pack_2.foo \> f1 = foo.Funcionario()

\> from pack_0.pack_1.pack_2.foo import Funcionario Pacote pack_0
importado pack_0.pack_1.pack_2.foo \> f1 = Funcionario()

\$ echo \'print(\_\_name\_\_)\' \> pack_0/pack_1/\_\_init\_\_.py \$ echo
\'print(\_\_name\_\_)\' \> pack_0/pack_1/pack_2/\_\_init\_\_.py

\> from pack_0.pack_1.pack_2.foo import Funcionario Pacote pack_0
importado pack_0.pack_1 pack_0.pack_1.pack_2 pack_0.pack_1.pack_2.foo

\> from pack_0.pack_1.pack_2.foo import \* Pacote pack_0 importado
pack_0.pack_1 pack_0.pack_1.pack_2 pack_0.pack_1.pack_2.foo \> f1 =
Funcionario()

\$ python3 pack_0/\_\_pycache\_\_/foo.cpython-34.pyc
