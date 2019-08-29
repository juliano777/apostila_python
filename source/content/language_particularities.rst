Particularidades da Linguagem
*****************************

Palavras Reservadas
-------------------

Palavras reservadas ou em inglês *keywords* são

.. code-block:: text

    False   class     finally  is        return  
    None    continue  for      lambda    try     
    True    def       from     nonlocal  while   
    and     del       global   not       with    
    as      elif      if       or        yield   
    assert  else      import   pass              
    break   except    in       raise

Podemos verificar as palavras reservdas de Python usando código:

.. code-block:: python

    from keyword import kwlist as keywords

    for i in keywords:
        print(i)

.. code-block:: console

    . . .



Definição do Interpretador de Comandos
--------------------------------------

	Para scripts Python, na primeira linha podemos especificar o interpretador de comandos a ser utilizado, também conhecido como shebang;

.. code-block:: python
    :linenos:

    #!/usr/bin/env python3

.. note::

    Em ambientes Windows não é preciso espeficar, isso é pertinente a ambientes Unix.

Codificação (Conjunto de Caracteres - Encoding)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	É possível utilizar codificações diferentes de ASCII em arquivos de código-fonte.
	A melhor maneira de se fazer isso é colocar uma linha especial no começo do arquivo, se foi especificado o interpretador, deve vir logo depois dele:

.. code-block:: python
    :linenos:

    # _*_ encoding: utf-8 _*_


.. code-block:: bash

     vim /tmp/hello.py

.. code-block:: python
    :linenos:

    #!/usr/bin/env python

    print('Olá!')

.. code-block:: bash

    $ python /tmp/hello.py

.. code-block:: console

    File "/tmp/hello.py", line 4
    SyntaxError: Non-ASCII character '\xc3' in file /tmp/hello.py on line 4, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details

Editar o script Python:

.. code-block:: bash
    vim /tmp/hello.py

.. code-block:: python
    :linenos:

    #!/usr/bin/env python
    #_*_ coding: utf-8 _*_

    print('Olá!')

Executar o script:

.. code-block:: bash

    python /tmp/hello.py

.. code-block:: console

    Olá!

Case Sensitive
--------------

	Python é case sensitive, ou seja, letras maiúsculas e minúsculas são interpretadas de formas diferentes.


.. code-block:: python

    foo = 'bar'
    Foo = 'foo'
    print(foo)

.. code-block:: console

    bar

.. code-block:: python

    print(Foo)

.. code-block:: console

    foo

Não Suporta Sobrecarga de Funções / Métodos
-------------------------------------------

	Àqueles que vêm de Java deve estranhar dentre outras coisas o fato de Python não suportar sobrecarga de funções e métodos.
	Quando uma mesma função é escrita duas ou mais vezes, o que prevalece é a última definição.

.. code-block:: python

    def hello_world():
        print('Hello World')


.. code-block:: python

    def hello_world(string):
        print(string)

hello_world()

TypeError                                 Traceback (most recent call last)
<ipython-input-3-2c5bb141a5c6> in <module>()
----> 1 hello_world()

TypeError: hello_world() takes exactly 1 argument (0 given)

hello_world('foo')
foo

Orientada a Objetos
-------------------

	Em Python tudo é objeto.
	Ainda fazendo comparação com o mundo Java, em Python não existem tipos primitivos.
	Até mesmo um número inteiro é uma instância de int e tem seus atributos e métodos.

x = 45

x.__hex__()
'0x2d'

x.real
45

x.imag
0

	A criação de classes em Python é extremamente simples, sendo que uma classe primária a herança é feita da classe object e cada classe pode herdar mais de uma. Ou seja, também é aceita herança múltipla.
	
class Carro(object):
    marca = ''
    modelo = ''
    ano = 0

c1 = Carro()

c1.marca = 'Porsche'

c1.modelo = 'Carrera'

c1.ano = 1995

print('O %s %s fabricado em %i estava estacionado.' % (c1.marca, c1.modelo, c1.ano))

O Porsche Carrera fabricado em 1995 estava estacionado.


class Animal(object):
    peso = 0.0

class Humano(Animal):
    quoficiente_inteligencia = 0.0

class Touro(Animal):
     envergadura_chifre = 	0.0

class Minotauro(Humano, Animal):
    pass


Tipagem Dinâmica
----------------

	O interpretador define o tipo de acordo com o valor atribuído à variável.
	A mesma variável pode ter seu tipo mudado de acordo com valores a ela atribuídos ao longo do código-fonte e em seu tempo de execução.

foo = 'bar'

type(foo)
str

foo = 123

type(foo)
int

foo = 7.0

type(foo)
float

Tipagem Forte 
-------------

	O interpretador verifica se a operação é válida e não faz coerção automática entre tipos incompatíveis. Caso haja operações de tipos incompatíveis é preciso fazer a conversão explícita da variável ou variáveis antes da operação.

foo = '2'

bar = 5

type(foo)
str

type(bar)
int

foobar = foo + bar

TypeError                                 Traceback (most recent call last)
<ipython-input-28-36cb556c8cf9> in <module>()
----> 1 foobar = foo + bar

TypeError: cannot concatenate 'str' and 'int' objects

foobar = int(foo) + bar

print(foobar)7


foo = 2.0

type(foo)
float

bar = 5

type(bar)
int

foobar = foo + bar

print(foobar)
7.0

Bytecode
--------

	Formato binário multiplataforma resultante da compilação de um código Python.


Criação de estrutura de diretórios para teste de pacote e bytecode:

.. code-block:: bash

    mkdir -p /tmp/python/PacoteA/PacoteA1

Editar o módulo "Modulo1" que está dentro do pacote "PacoteA":

.. code-block:: bash

    vim /tmp/python/PacoteA/Modulo1.py
    

.. code-block:: python

    def funcao():
        print('Hello World!!!')

Editar o módulo "Modulo2" que está dentro do pacote "PacoteA":

.. code-block:: bash

    vim /tmp/python/PacoteA/PacoteA1/Modulo2.py


.. code-block:: python
    
    def funcao(numero):
        print(numero ** 3)


Edição de script de exemplo:

.. code-block:: bash

    vim /tmp/python/foo.py

.. code-block:: python

    #!/usr/bin/env python
    # _*_ encoding: utf-8 _*_

    from PacoteA.Modulo1 import funcao
    from PacoteA.PacoteA1 import Modulo2

    print('\nAtenção!!!\n')
    print('O teste vai começar...\n')

    funcao()

    Modulo2.funcao(3)

Execução do script:

.. code-block:: bash

    python3 /tmp/python/foo.py

.. code-block:: console

    Atenção!!!

    O teste vai começar...

    Hello World!!!
    27

Quando um módulo é carregado pela primeira vez ou se seu código é mais novo do que o arquivo binário ele é compilado e então gera ou gera novamente o arquivo binário .pyc.

Listar o conteúdo de "PacoteA":

.. code-block:: bash

    ls /tmp/python/PacoteA/

.. code-block:: console

    Modulo1.py  PacoteA1  __pycache__


Listar o conteúdo de __pycache__:

.. code-block:: bash

    ls /tmp/python/PacoteA/__pycache__/

.. code-block:: console

    Modulo1.cpython-36.pyc


Com o comando "file" verificar informações de tipo de arquivo:    

.. code-block:: bash

    file /tmp/python/PacoteA/__pycache__/Modulo1.cpython-36.pyc

.. code-block:: console

    /tmp/python/PacoteA/__pycache__/Modulo1.cpython-36.pyc: python 3.6 byte-compiled

Quebra de linhas
----------------

Pode ser usada a barra invertida ou por vírgula.

Exemplos:

varTeste = 3 * 5 + \
(10 + 7)

varLista = [7,14,25,
81,121]

Blocos
------

	São delimitados por endentação e a linha anterior ao bloco sempre termina com dois pontos.

Exemplo:

#Definição de uma classe
class Carro(object):
    ano = 0
    marca = ''
    estado_farois = False

    #Definição de um método da classe
    def interruptor_farois(self):
        #Bloco if
        if(self.estado_farois):
            print('Apagando faróis')
            self.estado_farois = False            
        else:   
            print('Acendendo faróis')
            self.estado_farois = True

Comentários
-----------

	Inicia-se com o caractere "#" em cada linha.

# um simples comentário

# A seguir uma soma

x = 5 + 2

print(x) # Imprime o valor de x

2.10.1 Docstrings ou Strings de Múltiplas Linhas

	Feitos dentro de funções e classes, que geram documentação automaticamente que pode ser acessado pela função help().
	São usados três pares de apóstrofos (') ou três pares de aspas ("), 3 (três) no início e 3 (três) no fim.


Com apóstrofos:

'''Esta função faz isso de forma
x, y e z além de bla bla bla bla'''

Com aspas:

"""Esta função faz isso de forma
x, y e z além de bla bla bla bla"""

Recurso para criar documentação automaticamente:

def funcao():
    '''Esta função não faz absolutamente nada'''
    pass

help(funcao)

Help on function funcao in module __main__:

funcao()
    Esta função não faz absolutamente nada


Operadores
----------

Aritméticos

Lógicos

Bit a Bit
Soma 

+

Menor
<

Deslocamento para esquerda
<<
Subtração
-

Maior
>

Deslocamento para direita
>>
Multiplicação
*

Menor ou igual
<=

E bit-a-bit (AND)
&

Divisão
/

Divisão Inteira
//


Python 2:

7 / 2
3

7 / 2.0
3.5

7 // 2.0
3.0


Python 3:

>>> 7 / 2
3.5
>>> 7 / 2.0
3.5
>>> 7 // 2.0
3.0
>>> 7 // 2
3




Maior ou igual
>=

Ou bit-a-bit (OR)
|


Igual
==

Ou exclusivo bit-a-bit (XOR)
^
Módulo
%

Diferente
!=

Inversão (NOT) 
~
Potência
**

O Comando del
-------------

	Este comando tem como objetivo remover a referência de um objeto.
	Se esse objeto não tiver outra referência, o garbage collector atuará liberando recursos.

sogra = 'Edelbarina'
print(sogra)
Edelbarina
del sogra
print(sogra)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sogra' is not defined

a = ['Z', 1, 5, 'm']

del a[2]

print(a)
['Z', 1, 'm']


print

	Antes era somente um comando, a partir da série 3.X será apenas interpretado como função.


print('Teste')
Teste


Python 3.X:

print 'Teste'
  File "<ipython-input-1-2957621f454d>", line 1
    print 'Teste'
                ^
SyntaxError: invalid syntax


In [2]: print('Teste')
Teste

	
Atribuição de Valores
---------------------

Atribuição Simples
~~~~~~~~~~~~~~~~~~

foo = 0
bar = 'bla bla bla'

print(foo)
0

print(bar)
bla bla bla

2.12.1 - Atribuição Composta ou Atribuição por Tupla

x, y, z = (1, 2, 3)

print(x)
1

print(y)
2

print(z)
3

Invertendo valores:

x = 10

y = 20

x, y = y, x

print(x)
20

print(y)
10


Atribuição por Incremento ou Decremento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

x = 0
x +=1
x +=1
x +=1
x +=1

print(x)
4

x /= 2

print(x)
2

x -= 1

print(x)
1

x *= 7

print(x)
7

foo ='bla '

foo *= 3

print(foo)
bla bla bla


Referência de Identificadores
-----------------------------

x = 7
y = x
z = x

id(x)
29786312

id(y)
29786312

id(z)
29786312

3 (três) referências ao mesmo objeto

del x

Agora são 2 (duas) referências...

print(y)
7


del y

Resta apenas 1 (uma) referência...

print(z)
7


del z

O contador de referências chegou a 0 (zero), ou seja, não há mais referência para o objeto.
Então entra em ação o Garbage Collector para limpar a memória.