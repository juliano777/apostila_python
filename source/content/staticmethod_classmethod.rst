Método de Classe e Método Estático
**********************************

|   Existem dois tipos de métodos que podem ser executados diretamente de uma
| classe, ou seja, sem precisar criar um objeto dela. Justamente por serem
| independentes de objetos não esperam um "`self`" como primeiro parâmetro.
|   A utilidade desses métodos é para processamento de dados de classes em vez
| de instâncias.
|   Mesmo que isso possa ser feito por uma função escrita externamente à classe,
| não terá uma associação a essa classe e não poderão ser herdados por classes
| filhas. 
|   Métodos estáticos são usados para agrupar funções que têm conexão lógica com
| a classe.
|   Métodos de classe são usados para o mesmo fim que os métodos estáticos, mas
| que também podem processar dados da classe diretamente.	

Prática:

Observe no exemplo a seguir as diferentes assinaturas para respectivamente os
métodos comum, de classe e estático:

.. code-block:: python

    class Foo(object):
        
        def metodo_comum(self):
            print('Método comum {}'.format(self))

        @classmethod
        def metodo_de_classe(cls):
            print('Método de classe {}'.format(cls))

        @staticmethod
        def metodo_estatico():
        print('Método estático')

	
|   Na classe foram declarados três métodos, sendo que o primeiro que é um
| método comum, cujo primeiro argumento é o tradicional self que representa a
| instância (objeto) criada a partir da classe.
|   O segundo método é decorado com @classmethod, faz desse método um método de
classe, o qual não faz necessária a criação de um objeto para ser utilizado.
Esse tipo de método é invocado da seguinte forma: Classe.metodo_de_classe().
Ainda sobre o método de classe um detalhe interessante é o "cls" ao invés de
self.
A variável "cls" é utilizada com um propósito similar ao de self, mas ao invés
de representar uma instância criada, representa a classe à qual o método
pertence.
Assim como self, cls é apenas uma convenção, deixando ao gosto do usuário, se
o mesmo desejar utilizar outro nome.
E por fim o método estático, decorado com @staticmethod é como uma função
definida externamente à classe. Não recebe um "self" ou um "cls".


Chamada do método comum pela classe:

.. code-block:: python

    Foo.metodo_comum()

.. code-block:: console

    TypeError: unbound method metodo_comum() must be called with Foo instance as first argument (got nothing instead)

Aqui podemos ver que se for feita uma tentativa de invocar a partir da classe
um método que não seja nem de classe e nem estático será retornado um erro.



Invocando um método de classe a partir da classe:

.. code-block:: python

    Foo.metodo_de_classe()

.. code-block:: console

    Método de classe <class '__main__.Foo'>



Invocando um método estático a partir da classe

.. code-block:: python

    Foo.metodo_estatico()

.. code-block:: console

    Método estático



Criação de objeto:

.. code-block:: python

    o = Foo()

A instância "o" é implicitamente passada como argumento para o método
construtor que não foi declarado.



Chamada do método comum pela instância:

.. code-block:: python

    o.metodo_comum()


.. code-block:: console

    Método comum <__main__.Foo object at 0x7f40d812d410>

Chamada do método de classe pela instância:

.. code-block:: python

    o.metodo_de_classe()


.. code-block:: console

    Método de classe <class '__main__.Foo'>

Chamada do método estático pela instância:

.. code-block:: python

    o.metodo_estatico()
    
.. code-block:: console

    Método estático