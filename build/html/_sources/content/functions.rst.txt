Funções
*******

|   Uma funçao é um recurso de linguagens de programação, que armazena instruções contidas em um bloco de forma a evitar escrever novamente essas mesmas instruções reaproveitando o código ali escrito.
|   No âmbito (escopo) da função podem ser definidas variáveis que só terão visibilidade dentro da função.
|   Após definida a função, a mesma é invocada pelo seu nome e seus argumentos (se ela requerir).
|   Funções em Python são definidas a partir do comando def.
|   Funções ajudam o código a dividir, agrupar, reusar, reduzir, deixar mais legível além de ser uma boa prática.


Funções sem Argumentos
----------------------

Definição da função sem argumentos:

.. code-block:: python

    def funcao():
        numero = 7 ** 2
        msg = 'O quardrado de 7 é %d' % numero
        print(msg)      
        
    funcao()


.. code-block:: console

    O quardrado de 7 é 49

O Comando return
----------------

	O comando return dá um retorno para a função.
	Uma função pode retornar um ou mais valores (coleções).
	Deve ser o último comando da função, pois se tiver algum código depois será ignorado.
	Vale lembrar que return não é a mesma coisa que imprimir em tela. Quando se digita algo que retorne um valor dentro de um shell interativo, esse valor por conveniência é impresso em tela.
	Mas em um aplicativo ou script isso não acontecerá, portanto se deseja imprimir um valor em tela, isso deve ser explicitado, o que é mais comumente feito por print().
	Quando uma função não tem um comando return, seu retorno é None implícito, o que para outras linguagens como C e Java é a mesma coisa que void.



Definição da função:

.. code-block:: python

    def funcao():
        return 7



Utilizando print para imprimir em tela o valor retornado pela função
multiplicado por 3:

.. code-block:: python

    print(funcao() * 3)    

.. code-block:: console

    21
    
    
    
Definição de uma função que retorna mais de um valor:

.. code-block:: python

    def funcao():
        return 3, 9



Atribuindo à variável o valor de retorno da função:

.. code-block:: python

    x = funcao()




Imprimindo o valor da variável:

.. code-block:: python

    print(x)

.. code-block:: console

    (3, 9)




Verificando o tipo da variável:

.. code-block:: python

    type(x)

.. code-block:: console

    tuple



Definição de uma função com código após return:

.. code-block:: python

    def funcao():
        return 7
        print('Teste')



Execução da função:

.. code-block:: python

    funcao()

.. code-block:: console

    7

|   Como pode-se notar, o código inserido após return foi completamente
| ignorado.
|   Devido ao fato de os comandos serem digitados no shell interativo foi
| impresso em tela o valor de retorno da função.



Argumentos Simples (Argumentos Não Nomeados)
--------------------------------------------

	Uma função pode ter um ou mais argumentos a serem pasados.
	Esses argumentos podem ser ou não obrigatórios. Sendo que os argumentos não obrigatórios têm um valor inicial.


Definição de uma função

def funcao(x):
  return x

Execução da função sem passar argumentos

funcao()  

---------------------------------------------------------------------------
.. code-block:: console

    TypeError                                 Traceback (most recent call last)
    /home/beethoven/<ipython-input-22-7473677d9fe3> in <module>()
    ----> 1 funcao()

    TypeError: funcao() takes exactly 1 argument (0 given)

Devido ao fato de a função exigir que seja passado um argumento

Execução da função passando um argumento

funcao(7)

.. code-block:: console

    7
    
    
    
Argumentos Nomeados
-------------------

	Podemos definir uma função em que um ou mais argumentos tenham valores padrões de forma que ao invocar a função podemos omitir a declaração, pois será considerado o padrão ou explicitando um valor.
	Quando houver mais de um argumento, os argumentos obrigatórios devem vira primeiro.

Definição de função com um argumento 

def funcao(x = 7):
    return x

Chamando a função sem declarar valor de argumento

funcao()
7

Chamando a função explicitando um valor de argumento
funcao(9)
9

funcao(x = 9)
9        

Definindo uma função mesclando argumentos padrão e obrigatórios

def funcao(x = 7, y):
         return x + y

SyntaxError: non-default argument follows default argument

Houve um erro, pois primeiro são os argumentos não padrões.

def funcao(x, y = 7):
     return x + y     


funcao(3)
10

funcao(2, 3)
5

funcao()

TypeError: funcao() takes at least 1 argument (0 given)

def funcao(x, y = 1, z = 2):
    return x + y + z
    
funcao(0)
3

funcao(1, 2)
5

funcao(1, 2, 90)
93

funcao(10, z = 30, y = 50)
90



Argumentos em Lista Não Nomeados
--------------------------------

	É possível passar uma lista de argumentos sem nomear cada um deles, ou seja, atribuir uma variável.
	Essa lista, internamente é interpretada como uma tupla (tuple).
	Tal recurso nos possibilita passar uma quantidade indeterminada de argumentos.
	O identificador da variável que representa esse tipo de argumento vem logo depois do caractere asterisco (*).

    

def funcao(*args):
    qtd = len(args)
    primeiro = args[0]
    ultimo = args[-1]
    print('Foram passados %d argumentos' % qtd)
    print('O primeiro é "%s"' % primeiro)
    print('O último é "%s"' % ultimo)
    print('Os argumentos passados foram: %s' % str(args))

funcao('abacaxi', 3, 'p', 8.3, 5 + 9j)
Foram passados 5 argumentos
O primeiro é "abacaxi"
O último é "(5+9j)"
Os argumentos passados foram: ('abacaxi', 3, 'p', 8.3, (5+9j))
    
    
def funcao(*args):
    for arg in args:
        print('Argumento %d = %s' % (args.index(arg), arg)) 

ou

def funcao(*args):
    for i, arg in enumerate(args):
        print('Argumento %d = %s' % (i, arg))
        
funcao('a', 1.5, 7, 99)

Argumento 0 = a
Argumento 1 = 1.5
Argumento 2 = 7
Argumento 3 = 99


def funcao(x, *args):
     return args
    
spam = (1, 2, 3, 4)

funcao(spam)
()

funcao(*spam)
(2, 3, 4)

def funcao(*args):
    return args

funcao(spam)
((1, 2, 3, 4),)

funcao(*spam)
(1, 2, 3, 4)

Quando o caractere asterisco é posicionado antes de uma variável faz com que considere que aquela variável (coleções) seja
"desempacotada". Seus elementos são passados como se fossem uma tupla, ou seja, uma sequência de valores estraídos separados
por vírgulas.



Argumentos em Lista Nomeados
----------------------------

	O identificador da variável desse tipo de argumento é precedido por dois asteriscos (**).
	É uma lista com quantidade indeterminada e cada elemento da lista tem um identificador próprio.

def funcao(**kargs):
    return kargs
   
funcao(a = 1, b = 2)
{'a': 1, 'b': 2}



def funcao(**kargs):
    for k, v in kargs.items():
        print('%s = %s' % (k.capitalize(), v))
        
        
funcao(
    nome = 'Chiquinho',
    sobrenome = 'da Silva',
    idade = 30,
    telefone = '(11) 99999-9999',
  )


Idade = 30
Sobrenome = da Silva
Telefone = (11) 99999-9999
Nome = Chiquinho  


def funcao(**kargs):
    return kargs

eggs = {'a': 3, 'b': 5, 'c': 'x'}

funcao(eggs)

TypeError: funcao() takes exactly 0 arguments (1 given)

funcao(**eggs)

.. code-block:: console

    {'a': 3, 'b': 5, 'c': 'x'}



Funções com Argumentos Variados
-------------------------------

	E se precisarmos fazer uma função que utilize tipos diferentes conforme visto anteriormente?
	A ordem dos tipos de argumentos é a seguinte:

	Simples, Nomeados, Lista de Não Nomeados e Lista de Nomeados

def foo(a, b = 3, *c, **d):
    print(a + b)
    print(c)
    print(d)

    foo(4, 5, 'Alemanha', 'Holanda', 'Inglaterra', continente = 'Europa', hemisferio = 'Norte')

.. code-block:: console

    9
    ('Alemanha', 'Holanda', 'Inglaterra')
    {'continente': 'Europa', 'hemisferio': 'Norte'}



Estruturas de Dados como Parâmetro para Funções
-----------------------------------------------

	Em algumas situações pode ser útil utilizar uma estrutura de dados como tupla (tuple), lista (list), dicionário (dict) ou mesmo um conjunto (set / frozenset).



Criação da função de teste:

def param_test(x, y):
    return x + y



Declaração das variáveis de estrutura de dados que serão utilizadas como parâmetro para a função:

tupla = (5, 2)

lista = [5, 2]

dicio = {'x': 5, 'y': 2}

conjunto = {2, 5, 2}



Testes utilizando as estruturas de dados criadas:

param_test(**dicio)  # Dicionário (dict) como parâmetro

param_test(*tupla)  # Tupla (tuple) como parâmetro  

param_test(*lista)  # Lista (list) como parâmetro

param_test(*conjunto)  # Conjunto (set) como parâmetro

.. code-block:: console

    7



Boas Práticas: Função Main
--------------------------

	Evite execuções globais, quebre seu código em funções o que facilita o reúso e teste de código.
	Crie uma função principal (main). Crie primeiro as outras funções e por último a ser definida a função principal.
	Na função principal serão feitas as chamadas às outras funções.
	Outra coisa interessante a ser feita é colocar a função principal dentro de um if. Sendo que se for executado, terá a variável especial "__name__" como valor "__main__".


vim hello.py

#!/usr/bin/env python
#_*_ coding: utf-8 _*_

def funcao():
     print('Função executada')


def Main():
     print('==== Início ====')
     funcao()
     print('==== Fim ====')


if __name__ == '__main__':
    Main()

python hello.py 

.. code-block:: console

    ==== Início ====
    Função executada
    ==== Fim ====



Funções Geradoras
-----------------

	Uma função geradora ao invés de utilizar o comando return, utiliza o comando yield, que retorna um objeto generator.

def f_gen(var):
    print('INÍCIO')

    for i in var:
        yield i
    
    print('FIM')        

g = f_gen('Python')

type(g)

.. code-block:: console

    generator

g.next()

.. code-block:: console

    INÍCIO
    'P'

g.next()


.. code-block:: console

    'y'

g.next()

.. code-block:: console

    't'

g.next()

.. code-block:: console

    'h'

g.next()

.. code-block:: console

    'o'

g.next()

.. code-block:: console

    'n'

g.next()

.. code-block:: console

    FIM

StopIteration: 


Funções Lambda
--------------

	São funções anônimas, ou seja, que não são associadas a um nome. Um recurso similar às funções anônimas em PL/pgSQL (PostgreSQL) e PL/SQL (Oracle).
	Sua estrutura é composta apenas por expressões, o que a torna muito limitada, no entanto consome menos recursos do que uma função convencional. 
	Por só aceitar expressões, o comando return não é permitido em sua estrutura.



.. code-block:: python

    (lambda x, y: x + y)(5, 2)

.. code-block:: console

    7

foo = lambda x, y: x ** y

.. code-block:: python

    print(foo(2, 5))

.. code-block:: console

    32