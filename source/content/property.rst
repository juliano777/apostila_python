Encapsulamento
**************

|   O conceito de encapsulamento no geral consiste em isolar atributos e / ou métodos de acesso externo deixando-os como privados.
|   Atributos privados devem ser acessados ou modificados através de *getters* e *setters*, respectivamente.
|   Métodos privados têm sua área de atuação restrita somente internamente na classe.


Modificador Private (__)
------------------------

|   Colocando 2 (dois) underscores antecedendo o atributo, ele fica privado, ou seja, não é acessível fora da classe.
|   Em Python não existem modificadores de atributos e métodos como em outras linguagens, ou seja, não existe *public*, *private* ou *protected*.



Criação de uma classe de teste:

.. code-block:: python

    class Foo(object):
        __atributo = 0



Instância da classe:

.. code-block:: python

    f = Foo()




Tentativa de acesso a atributo privado:

.. code-block:: python

    f.__atributo

.. code-block:: console

    . . .
    AttributeError: 'Foo' object has no attribute '__atributo'

|   Por ser um atributo privado, seu acesso externo não foi reconhecido.    



Property
--------

|   Property é a solução pythônica para implementar getters e setters de forma inteligente e podendo inclusive impor restrições.



Criação da classe Carro:

.. code-block:: python

    class Carro(object):
        def __init__(self):
            self.__velocidade = 0
        
        # Métodos privados para a property

        def __get__velocidade(self):
            print(f'Velocidade: {self.__velocidade} km/h')
            return self.__velocidade
        
        def __set__velocidade(self, velocidade):
            if velocidade > 300:
                raise ValueError('A velocidade máxima permitida é de 300 km/h')        
            self.__velocidade = velocidade
            print(f'Velocidade = {self.__velocidade} km/h')
            
        def __del__velocidade(self):
            print('Removendo a propriedade de velocidade')
            del self.__velocidade
        
        # Definição da property velocidade
        velocidade = property(__get__velocidade,  # getter
                              __set__velocidade,  # setter
                              __del__velocidade,  # deleter
                              'Velocidade máxima do carro')  # Descrição



Instância da classe Carro:

.. code-block:: python

    c = Carro()



Tentativa de acesso ao atributo privado:

.. code-block:: python

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



O que acontece se pegarmos o nome do atributo privado e o definirmos externamente?:

.. code-block:: python

    c.__velocidade = 'valor equivocado'
    
    
    
Acessando o atributo adicionado:

.. code-block:: python

    c.__velocidade                                                                                                                                                                                            
.. code-block:: console

    'valor equivocado'
    
    
    
Será que a property foi afetada?:

.. code-block:: python

    c.velocidade

.. code-block:: console

    Velocidade: 200 km/h
    
|   Felizmente a property não foi afetada e o encapsulamento foi mantido :)



Reatribuir um novo valor:

.. code-block:: python

    c.velocidade = 170                                                                                                                                                                                        

.. code-block:: console

    Velocidade = 170 km/h
    
    
    
Consultar o valor do atributo:

.. code-block:: python

    c.velocidade
    
.. code-block:: console

    Velocidade: 170 km/h
    170    



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

    AttributeError: 'Carro' object has no attribute '_Carro__velocidade'



Property como Decorator
-----------------------

|   Além da já citada implementação de property, pode-se também fazer isso por meio de decorators.



Criação de classe com definição de properties via decorators:

.. code-block:: python

    class Carro(object):
        def __init__(self):
            self.__velocidade = 0

        # Properties    
            
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

|   Repetir os comandos do exercício anterior ;) 



Descriptors
-----------

|   São objetos Python que implementam um método do protocolo descritor, que nos permite criar objetos que
tenham um comportamento desejado quando seus atributos são acessados por outros objetos.



Criação de uma classe descriptor:

.. code-block:: python

    class Verbose(object):

        def __get__(self, obj, type=None) -> object:
            return 7
            
        def __set__(self, obj, value) -> None:
            raise AttributeError('Não pode mudar o valor!!!')
            
        def __delete__(self, obj, type=None) -> None:
            raise AttributeError('Não pode remover o atributo!!!')
        
        
        
        
        
Criação de uma classe de teste para o descriptor:

.. code-block:: python

    class Foo(object):
        atributo = Verbose()



    
Instanciação da classe Foo:

.. code-block:: python

    o = Foo()




Verificação do tipo do atributo que utiliza o descriptor:

.. code-block:: python

    type(o.atributo)                                                                                                                                                                                           

.. code-block:: console

    int




Exibe o valor do atributo:

.. code-block:: python

    print(o.atributo)                                                                                                                                                                                          

.. code-block:: console

    7



Tentativa de atribuir um novo valor ao atributo:

.. code-block:: python

    o.atributo = 9

.. code-block:: console

    AttributeError: Não pode mudar o valor!!!

|   Houve um lançamento de exceção ao tentar redefinir o valor do atributo.



Tentativa de remover o atributo do objeto:

.. code-block:: python

    del o.atributo

.. code-block:: console

    AttributeError: Não pode remover o atributo!!!

|   Houve um lançamento de exceção ao tentar remover o atributo.



Verificando se o atributo foi alterado:

.. code-block:: python

    print(o.atributo)

.. code-block:: console

    7