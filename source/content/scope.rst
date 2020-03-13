Escopo
******

    Por escopo entende-se o contexto onde um identificador será considerado.
    Um identificador pode ser uma variável, um comando, uma função uma clase ou um objeto.
    A ordem de busca de um identificador em escopos é a seguinte:
    
  1º) Local ou dentro de função;
  2º) Função externa;
  3º) Global ou de módulo;
  4º) __builtins__


- Escopo Local ou Dentro de Função

    É o escopo que tem a maior prioridade.
    
 
Prática:

Declaração de uma variável com seu valor:

.. code-block:: python

    foo = 7



Exibindo na tela o valor da variável:

.. code-block:: python

    print(foo)

.. code-block:: console

    7

A função locals() retorna um dicionário com os identificadores locais e seus
respectivos valores.
Então é pedido o valor dada a chave que é o nome da variável local.


blablabla:

.. code-block:: python

    locals()['foo']

.. code-block:: console

    7


Dentro de função

Declaração de uma variável externamente ao escopo da função

foo = 7

Definição de uma função:

.. code-block:: python

    def funcao():
        foo = 9
        print(id(foo))
        print(foo)
    
Nota-se que dentro da função também há uma variável chamada "foo".
Essa função imprime o ID desse identificador e depois imprime seu valor.
    
Exibindo o ID de foo    

print(id(foo))
.. code-block:: console

    162857064

Exibindo o valor de foo

print(foo)
.. code-block:: console

    7

Acionando a função

funcao()
162857040
9

Nota-se também que bem como o ID e o valor retornados pela função,
da variável interna foo são diferentes da variável externa de mesmo nome.


- Escopo de Função Externa

    Ao se criar uma função dentro de outra, a função mais interna pode utilizar um
identificador que esteja no nível mais acima.

Prática:

Definição da funcao

def funcao_principal():
    x = 1
    def funcao_secundaria():
        print(x)
    funcao_secundaria()     
    
    A função principal tem uma variável x, cujo valor é impresso em tela
pela função secundária.
    A função principal invoca a função secundária.
    

Chamando a função     
funcao_principal()
.. code-block:: console

    1


Uma nova definição da função

def funcao_principal():
    x = 1
    def funcao_secundaria():
        x = 2
        print(x)
    funcao_secundaria()     
    
Diferente do exemplo anterior, a função secundária declarou sua própria variável "x".    
    

Testando a função    
funcao_principal()
.. code-block:: console

    2

Nota-se que o valor considerado foi o de "x", que é o identificador mais interno.

- Escopo Global ou Escopo do Módulo

  É também conhecido como escopo de módulo devido ao fato de estar na endentação do mesmo.

Prática:  

Criação de variável

foo = 'bar'

Criação de função

def funcao():
    foo = 'eggs'
    print(foo)
    
A função criada tem uma variável com o mesmo nome que uma variável global, a ela dá um valor e 
imprime esse valor em tela.
Será que isso altera o valor da variável global?
        
Execução da função
        
funcao()
.. code-block:: console

    eggs

Podemos notar que o valor impresso é igual ao da variável "foo" dentro da função.
Pra saber se a variável global foi alterada, vamos testar com a função print.

Imprimindo o valor da variável global

print(foo)
.. code-block:: console

    bar

Pode-se concluir que a função criada não interferiu na variável global.
Para alterar uma variável global em um contexto local precisamos utilizar o comando global.


Criação de função que altera a variável global

def funcao():
    global foo
    foo = 'eggs'
    print(foo)
    
Executar função
    
funcao()
.. code-block:: console

    eggs
      
OK, a função imprimiu o valor local da função.
Mas será que a variável global também foi alterada?


Imprimir o valor da variável global
      
print(foo)
.. code-block:: console

    eggs

Agora a função pôde alterar a variável global.
Isso se deve ao fato do comando global ter sido empregado.
A variável global a ser alterada deve ser declarada como global antes de sua 
atribuição.
  
Escopo __builtins__

  O escopo __builtins__ abrange identificadores que já estão definidos antes mesmo do código a ser escrito.
  São funções, comandos e variáveis internas de Python.
  
Prática:  
  
"str" é está em __builtins__?

'str' in dir(__builtins__)
True

Resposta afirmativa (True), ou seja, "str" faz parte desse escopo.
E se subscrevermos esse item localmente?


Criando uma variável cujo identificador pertence ao escopo __builtins__
str = 1

Qual é o tipo?

type(str)
.. code-block:: console

    int

"str" que inicialmente era um identificador para o tipo de strings em Python, 
aqui agora virou uma variável de inteiro.
Mas e o tipo "str" deixou de existir?

Qual o tipo?
type(__builtins__.str)
type

É do tipo "tipo"

Valor de str?

str
1



__builtins__.str(str)
'1'

del str

str(7)
.. code-block:: console

    '7'


dir(__builtins__)


.. code-block:: console

    global nome_variavel
    nome_variavel = valor



# ==============================================================================

Funções globals(), locals() e vars() e Comando global

	Cada uma das funções retornam dicionários de variáveis e seus respectivos valores.
	globals(): Retorna variáveis globais (escopo do módulo);
	locals(): Retorna variáveis locais (escopo local);
	vars(obj): sem argumentos é equivalente a locals(), com um argumento, equivalente a objeto.__dict__



bla bla bla:

> foo = 'escopo global'



bla bla bla:

> def f():
    foo = 'escopo local'
    bar = 'uma variável qualquer...'
    print(globals()['foo'])
    print(locals()['foo'])



bla bla bla:

> f()

.. code-block:: console

    escopo global
    escopo local



bla bla bla:

> class Spam(object):
    foo = ''
    bar = ''



bla bla bla:

> vars(Spam)

.. code-block:: console

    <dictproxy {'__dict__': <attribute '__dict__' of 'Spam' objects>,
     '__doc__': None,
     '__module__': '__main__',
     '__weakref__': <attribute '__weakref__' of 'Spam' objects>,
     'bar': '',
     'foo': ''}>



bla bla bla:

> def f():
    global x
    x = 7



bla bla bla:

> type(x)

.. code-block:: console

    NameError: name 'x' is not defined



bla bla bla:

> f()



bla bla bla:

> type(x)

.. code-block:: console

    int



bla bla bla:

> print(x)

.. code-block:: console

    7