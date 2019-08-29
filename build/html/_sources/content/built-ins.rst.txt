Comandos e Funções Importantes
******************************

	Neste capítulo são abordados comandos e funções interessantes e / ou imprescindíveis para a linguagem.

print()
-------

    Em Python 2 era um comando e em Python 3 passou a ser exclusivamente uma função.
    Seu objetivo é imprimir uma mensagem que por padrão é STDOUT.

.. code-block:: python

    # Um simples "Hello, world!":

    print('Hello, world!')

.. code-block:: console

    Hello, world!

.. code-block:: python

    # Pode-se passar mais de uma string como parâmetro:

    print('foo', 'bar', 'baz')

.. code-block:: console

    foo bar baz

.. code-block:: python

    # Colocando como separador uma nova linha para cada string passada como parâmetro

    print('foo', 'bar', 'baz', sep='\n')

.. code-block:: console

    foo
    bar
    baz

range()
-------

    É uma função que retorna um objeto com uma faixa inteiros (range object).
    Muito útil para uso em loops.

Sintaxe:

    range(stop)
    range(start, stop[, step])

    start: Valor inicial da sequência, por padrão é 0 (zero).
    stop:  Valor final da sequẽncia - 1.
    step:  Valor de incremento, cujo padrão é 1 (um), quando start é maior que stop, ou seja, para se fazer uma sequência regressiva é preciso um número negativo.

.. code-block:: python

    # Um parâmetro (stop)
    for i in range(5):
        print(i)

.. code-block:: console

    0
    1
    2
    3
    4

.. code-block:: python

    # Dois parâmetros (start e stop)
    for i in range(3, 10):
        print(i)

.. code-block:: console

    3
    4
    5
    6
    7
    8
    9

.. code-block:: python

    # Três parâmetros (start, stop e step)
    for i in range(1, 10, 2):
        print(i)

.. code-block:: console

    1
    3
    5
    7
    9

.. code-block:: python

    # Sequẽncia regressiva
    for i in range(20, 1, -5):
        print(i)

.. code-block:: console

    20
    15
    10
    5


filter()
--------

    Função que retorna um iterador produzindo os itens iteráveis para os quais a função(item) for True.

.. code-block:: python

    # Criação de uma função que retorna True se o objeto for ímpar
    def impar(x):
        return x % 2 != 0

    # Testando a função
    impar(7)

.. code-block:: console

    True

.. code-block:: python

    impar(6)

.. code-block:: console

    False


Em uma sequência de 0 a 19, pela função impar criar um objeto filter somente com os elementos ímpares e posteriormente ser convertido para lista:

.. code-block:: python

    f = filter(impar, range(0, 20))
    print(list(f))

.. code-block:: python

    [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



map()
-----

    Cria um iterador que aplica uma função para cada elemento do iterável.



Dada uma tupla com várias strings, criar uma lista com o tamanho de cada string respectivamente:

> m = map(len, ('spam', 'foo', 'bar', 'eggs', 'Python'))

> list(m)

[4, 3, 3, 4, 6]



Para cada item da lista, criar uma nova lista com seus respectivos tipos:

> m = map(type, ['foo', 1.4, 2 + 5j, 1000])

> list(m)

[str, float, complex, int]



Para cada item da primeira lista elevar (potência) ao elemento respectivo na segunda lista e criar uma nova lista com os resultados:

> m = map(pow, [3, 7, 5, 10], [2, 1, 7, 3])

> list(m)

[9, 7, 78125, 1000]



reduce()
--------

    Em Python 2 estava disponível sem a necessidade de fazer importação, hoje em Python 3 está no módulo functools.



Via loop somar todos elementos de uma tupla:

> soma = 0  # Variável que terá o valor da soma após o loop

> for i in (2, 1, 4, 3):  # Loop e incrementação
    soma += i

> print(soma)  # Exibe o resultado

10



Importando reduce de functools;

> from functools import reduce



Função reduce para executar a mesma tarefa anterior com apenas um comando:

> reduce(int.__add__, (2, 1, 4, 3))

10



del
---

    Pode ser tanto um comando como uma função cuja finalidade é remover a referência de um objeto.
	Também apaga elemento de uma coleção.



Teste de del em um objeto mutável (lista):

> lista = ['a', 'b', 'c']  # Definição da lista

> del lista[1]  # Apaga o segundo elemento da lista

ou

> del(lista[1])  # Equivalência ao comando anterior em forma de função

> print(lista)  # Exibe a lista após o elemento ser retirado da mesma

['a', 'c']



Teste de del para desalocar um objeto criado:

> foo = 'bar'  # Objeto string criado

> print(foo)  # Verificando o valor da string

bar

> del foo  # Apagando o objeto string

> print(foo)  # Tentativa de imprimir o valor do objeto desalocado

NameError: name 'foo' is not defined

    Nota-se que após o del não é possível mais fazer referência ao objeto.



ord e chr
---------

    A função ord retorna o código Unicode de um caractere.
    A função chr faz o caminho inverso, ou seja, retorna um caractere dado um código Unicode. Em Python 2 chr era unichr.    



ord e chr

    A função ord retorna o código Unicode de um caractere.
    A função chr faz o caminho inverso, ou seja, retorna um caractere dado um código Unicode. Em Python 2 chr era unichr.    



Exemplos de ord e chr:

> ord('\n')  # Qual é o código Unicode para new line?

10


> chr(10)  # Qual caractere Unicode corresponde ao código 10?

'\n'


> ord('\r')  # Qual é o código unicode para carriage return?

13

> chr(13)  # Qual caractere Unicode corresponde ao código 13?

'\r'

> chr(97)  # Qual caractere Unicode corresponde ao código 97?

'a'

> ord('a')  # Qual é o código unicode para o caractere "a"?

97

> chr(120)  # Qual caractere Unicode corresponde ao código 120?

'x'

> chr(981)  # Qual caractere Unicode corresponde ao código 981?

'ϕ'



dir()
-----

	Função que lista atributos e métodos de um elemento.
    Se chamada sem nenhum argumento retorna os nomes do escopo atual.
    A chamada dessa função é correspondente ao executar o método __dir__.
    


Definição de variáeis:

> x = 0

> y = 1

> z = 2



Execução da função dir sem parâmetros:

> dir()

['In',
 'Out',
. . .
 'x',
 'y',
 'z']



A variável foi declarada no escopo?:

> 'x' and 'y' and 'y' and 'z' in dir()

True

> 'w' in dir()                                                                                                                                         

False



Criação de uma classe:

> class Pessoa(object):
    # Atributos

    nome = '' 
    rg = '' 
    cpf = 0
    email = ''
    
    # Métodos
    def saudacao(self): 
        print('Olá')

    def dizer_nome(self):
        print('Meu nome é {}'.format(self.nome))



Verificando o conteúdo da classe (atributos e métodos):

> dir(Pessoa)

ou

> p.__dir__()

['__class__',
 '__delattr__',
 '__dict__',

. . . 

 'cpf',
 'dizer_nome',
 'email',
 'nome',
 'rg',
 'saudacao']



Criação de um objeto da classe e definição de atributos:

> p = Pessoa()  # 

> p.nome = 'Chiquinho'

> p.rg = '00000000'

> p.cpf = 12345678901                                                                                                                                  

> p.email = 'chiquinho@chiquinhodasilva.xx'



Atributo __dict__, que é um dicionário que contém os atributos do objeto:

> p.__dict__                                                                                                                                           

{'nome': 'Chiquinho',
 'rg': '00000000',
 'cpf': 12345678901,
 'email': 'chiquinho@chiquinhodasilva.xx'}



Pegando o valor do atributo pelo dicionário:

> p.__dict__['nome']                                                                                                                                   

'Chiquinho'



Com o auxílio de da função dir, listar todos os métodos do objeto:

> def is_dunder(s):  # Função que servirá para a função principal
    '''
    Função que retorna True para dunder strings
    '''

    # Se começar e terminar com "__" retornar True
    if s.startswith('__') and s.endswith('__'):
        return True
    else:
        return False
   


> def mostra_metodos(objeto):
    '''
    Função que mostra em tela todos os nomes de métodos de um objeto
    '''

    # Generator que conterá os nomes dos métodos por tuple comprehension
    metodos = (metodo for metodo in dir(objeto)  # Para cada item do objeto
               if (not is_dunder(metodo)) and  # se não for um dunder
               callable(getattr(objeto, metodo))  # e se for "chamável"
              )

    # Loop para exibir os nomes dos métodos
    for i in metodos:
        print(i)



Chamando a função criada para imprimir em tela os nomes dos métodos:

> mostra_metodos(p)                                                                                                                                   

dizer_nome
saudacao


pass
----

    É um comando de  operação nula, ou seja, quando é executado nada acontece. É útil como um marcador quando um statement é requerido sintaticamente, mas não tem necessidade de um código a ser executado.



Função que nada faz:

> def nula():
    '''
    Função sem utilidade
    '''
    pass



assert
------

    Um statements assert é uma maneira conveniente para inserir asserções de debug.
    O comando assert verifica em tempo de execução uma determinada condição e se a mesma não for verdadira uma exceção AssertionError é lançada e se essa exceção não for tratada, o programa pára.



Criação do script com assert sem tratamento de exceção:

$ cat << EOF > /tmp/assert_sem_try.py
print('Começo')

assert 1 == 1  # OK
assert 2 == 1  # Ops...

print('Fim')
EOF



Execução:

$ python3.7 /tmp/assert_sem_try.py

Começo
Traceback (most recent call last):

. . .

AssertionError

    Nota-se que a execução do script não chegou até o fim.



Criação do script com assert com tratamento de exceção:

$ cat << EOF > /tmp/assert_com_try.py
print('Começo')

try:
    assert 1 == 1  # OK
    assert 2 == 1  # Ops...

except AssertionError:
    print('Teve erro...')


print('Fim')
EOF



Execução:

$ python3.7 /tmp/assert_com_try.py

Começo
Teve erro...
Fim



abs()
-----

    Retorna o valor absoluto do argumento.

    abs(x)



Exemplos:

> abs(3)

3

> abs(-3)

3



divmod()
--------

    Função que retorna uma tupla de dois elementos no formato (x//y, x%y), respectivamente resultado da divisão inteira e resto da divisão:



Exemplos:

> divmod(11, 4)  # Equivalente: 11 // 4, 11 % 4

(2, 3)



round()
-------

    Função que retorna um número de forma arredondada dada uma precisão em dígitos decimais.
    O valor de retorno é um inteiro se o número de dígitos for omitido ou None. Caso contrário, o valor de retorno terá o mesmo tipo do número. O número de dígitos pode ser negativo.



Arredondamento sem especificar o número de dígitos (segundo parâmetro):

> round(3.333333)

3



Arredondamento com quatro dígitos de precisão:

> round(3.333333, 4)

3.3333



Precisão variando de 1 a -3:

> round(1237.87431, 1)

1237.9

> round(1237.87431, 0)

1238.0

> round(1237.87431, -1)

1240.0

> round(1237.87431, -2)

1200.0

> round(1237.87431, -3)

1000.0



callable()
----------

    Função que retorna True se o objeto é "chamável" (callable) (i. e., algum tipo de função).
    Vale lembrar que classes também são chamáveis, bem como objetos de classes que implementam o método __call__().



Criação de uma função:

> def myfunction():
    pass



Criação de uma classe sem o método __call__():

> class Foo: 
    pass



Criação de uma classe com o método __call__():

> class Bar: 
    def __call__(self):
        pass



Instância da classe sem o método __call__():

> f = Foo()



Instância da classe com o método __call__():

> b = Bar()



Execuções de callable:

> callable('foo')

False

> callable(myfunction)                                                                                                                                  

True

> callable(Foo)                                                                                                                                        

True

> callable(Bar)

True

> callable(f)                                                                                                                                          

False

> callable(b)

True



oct()
-----

    Função que retorna a representação octal de um inteiro.



Exemplos:

> oct(9)

'0o11'

> oct(10)                                                                                                                                              

'0o12'



hash()
------

    Função que retorna o valor hash de um dado objeto.
    Dois objetos que são comparados também devem ter o mesmo valor de hash.



Testes com a função hash:

> hash(1)  # O hash de um inteiro vai ser seu próprio valor

1

> hash(2)

2

> x = 'foo'  # Hash de uma string

> hash(x)

8540844669962366372

> y = x  # Nova variável y igual a x

> hash(x) == hash(y)  # Por terem o mesmo valor, o hash será igual
                                                                                                                                  
True

> hash([1, 2, 3])  #  Alguns tipos como list, dict e set são unhashable

TypeError: unhashable type: 'list'

> # Quando um número é muito grande seu hash será diferente de seu valor
> hash(9999999999999999999)

776627963145224195


id()
----

    É uma função que retorna a identidade de um objeto.
    É a garantia que o objeto será único dentre outros.



Criação de duas tuplas:

> foo = ('x', 'y')

> bar = ('x', 'y')



Comparando as tuplas criadas:

> foo == bar

True



Verificando o a identidade das tuplas criadas:

> id(foo)                                                                                                                                             

139651439554952

> id(bar)

139651403802056



É o mesmo objeto?:

> foo is bar

False



Criação de uma nova variável atribuindo com base em um objeto pré-existente:

> baz = bar



Comparando as variáveis:

> baz == bar

True



É o mesmo objeto?:

> baz is bar

True

> id(bar) == id(baz)                                                                                                                                  

True

    Aqui fica demonstrado que quando se cria uma nova variável simplesmente por atribuição é na verdade a criação de uma nova referência (apontamento) para o mesmo objeto.



len

    Função que retorna a quantidade de itens de um contêiner.



Criação de um objeto contêiner e verificação da quantidade de elementos:

> foo = ('x', 'y', 'z', 123, 5.7)

> len(foo)

5



Tamanho de uma string:

> len('Heavy Metal')

11



input

    É uma função de entrada de dados pelo teclado (STDIN), cujos dados são interpretados como string.
    Opcionalmente podemos colocar uma mensagem para pedir uma entrada de teclado.



Entrada de dados sem prompt:

> foo = input()  # Digite algo...



Imprimindo o valor da variável:

> print(foo)

. . .



Entrada de dados com prompt:

> foo = input('Digite uma string qualquer... ')

Digite uma string qualquer...



Imprimindo o valor da variável:

> print(foo)

. . .



min e max

    Dada uma coleção, seja ela uma lista, tupla, conjunto ou string, as funções min e max trazem, respectivamente, o valor mínimo e o máximo.



Exemplos:

> min(0, 2, -50, 7)  # Valor mínimo entre inteiros

-50

> max(0, 2, -50, 7)  # Valor máximo entre inteiros

7

> max('c', 'x', 'k')  # Para caracteres a ordem alfabética é levada em conta

'x'



enumerate

    Função que retorna um objeto iterável.



Criação de uma tupla:

> x = ('verde', 'azul', 'amarelo')



Criação de um objeto iterável com base na tupla criada anteriormente:

> y = enumerate(x)



Exibindo o tipo de y:

> type(y)

enumerate



Loop sobre o iterável:

> for i, j in y:
    print('{} - {}'.format(i, j))

0 - verde
1 - azul
2 - amarelo



Criar o iterável novamente:

> y = enumerate(x)




Método __next__() que traz uma tupla com o índice e o valor:

> y. __next__()

(0, 'verde')

> y. __next__()

(1, 'azul')

> y. __next__()

(2, 'amarelo')