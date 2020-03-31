Encapsulamento
**************

Modificador Private (__)
------------------------

|   Colocando 2 (dois) caracteres underscore antecedendo o atributo, ele fica
| privado, ou seja, não é acessível fora da classe.

.. code-block:: python

    # Criação de classe de teste:
    class Foo(object):
        __atributo = 0

    # Instância da classe:
    f = Foo()

    # Tentativa de acesso a atributo privado:
    f.__atributo

.. code-block:: console

    . . .
    AttributeError: 'Foo' object has no attribute '__atributo'



Property
--------

|   Property é a solução pythônica para implementar getters e setters de forma
| inteligente e podendo inclusive impor restrições.

.. code-block:: python

    # Classe com property:
    class Carro(object):
        def __init__(self):
            self.__velocidade = 0
        
        def _get__velocidade(self):
            print(f'Velocidade: {self.__velocidade} km/h')
            return self.__velocidade
        
        def _set__velocidade(self, velocidade):
            if velocidade > 300:
                raise ValueError('A velocidade máxima permitida é de 300 km/h')        
            self.__velocidade = velocidade
            print(f'Velocidade = {self.__velocidade} km/h')
            
        def _del__velocidade(self):
            print('Removendo a propriedade de velocidade')
            del self.__velocidade
        
        # Definição da property velocidade
        velocidade = property(_get__velocidade,
                              _set__velocidade,
                              _del__velocidade,
                              'Velocidade máxima do carro')


    # Instância da classe:
    c = Carro()

    # Tentativa de acesso ao atributo privado:
    c.__velocidade


.. code-block:: console

    .  .  .
    AttributeError: 'Carro' object has no attribute '__velocidade'



Acessando a property velocidade:    

.. code-block:: python

    c.velocidade

.. code-block:: console

    Velocidade: 0 km/h
    0



Atribuindo um valor para a property:

.. code-block:: python

    c.velocidade = 200

.. code-block:: console

    Velocidade = 200 km/h



Tentativa de atribuir um valor não permitido:    

.. code-block:: python

    c.velocidade = 301

.. code-block:: console
    
    . . .

    ValueError: A velocidade máxima permitida é de 300 km/h



Remover a property:

.. code-block:: python

    del c.velocidade

.. code-block:: console

    Removendo a propriedade de velocidade



Tentativa de acesso à property apagada:

.. code-block:: python

    c.velocidade

.. code-block:: console

    . . .

    AttributeError: 'Carro' object has no attribute '__velocidade'



Property como Decorator
-----------------------

|   Além da já citada implementação de property, pode-se também fazer isso
| por meio de decorators.

.. code-block:: python

    # Criação de classe com definição de properties via decorators:
    class Carro(object):
        def __init__(self):
            self.__velocidade = 0
            
        @property 
        def velocidade(self):
            '''
            Velocidade máxima do carro
            '''
            print(f'Velocidade: {self.__velocidade} km/h')
            return self.__velocidade
        
        @velocidade.setter    
        def velocidade(self, velocidade):
            if velocidade > 300:
                raise ValueError('A velocidade máxima permitida é de 300 km/h')        
            self.__velocidade = velocidade
            print(f'Velocidade = {self.__velocidade} km/h')
            
        @velocidade.deleter   
        def velocidade(self):
            print('Removendo a propriedade de velocidade')
            del self.__velocidade