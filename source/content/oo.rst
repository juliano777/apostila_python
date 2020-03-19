Orientação a Objetos
********************

	Python suporta herança múltipla;
	Tudo em Python é objeto (inclusive classes);
	O método construtor é o método inicializador, o método mágico __init__;



bla bla bla:

.. code-block:: python
    
    class NomeClasse(ClasseMae):
        # Método construtor ou método inicializador (sem parâmetro)
        def __init__(self):        
            pass

        # Método comum com 1 (um) parâmetro
        def metodo(self, foo):
            return foo


|   Em Python a definição de uma classe é bem simples. Usamos o comando class seguindo do nome da classe a ser criada, logo em seguida vindo entre parênteses os nomes das classes mãe separados por vírgulas, pois em Python é permitida herança múltipla.
|   O método construtor, também chamado de método inicializador é o __init__.


bla bla bla:

.. code-block:: python

    class Foo(object):
        nome = ''

    class Bar(object):
        idade = 0

        def metodo_teste(self):
            print('Teste')

    class Baz(Foo, Bar):

        def __init__(self, nome):
            self.nome = nome 

        altura = 0.0

bla bla bla:

.. code-block:: python

    o = Baz('Chiquinho da Silva')
    o.idade = 51
    o.altura = 1.60
    print('%s tem %s anos e %.2fm de altura' % (o.nome, o.idade, o.altura))
    Chiquinho da Silva tem 51 anos e 1.60m de altura


Obs.: Em Python todos métodos e atributos são públicos.
Há uma convenção que colocando um unerline como primeiro caractere no nome de um atributo ou um método o sinaliza como privado.
Porém, isso é apenas uma convenção. Nada impede que sejam acessados externamente.
Para que haja um bloqueio efetivo há um recurso na linguagem chamado "property".



bla bla bla:

.. code-block:: python

    class Carro(object):
        motor_ligado = False    

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def ignicao(self):
            if (self.motor_ligado):
                self.motor_ligado = False
                print('Motor desligado!')
            else:
                self.motor_ligado = True
                print('Motor ligado!')



bla bla bla:

.. code-block:: python

    c1 = Carro()

.. code-block:: console

    TypeError                                 Traceback (most recent call last)
    <ipython-input-13-e2526cbd1648> in <module>()
        15 
        16 
    ---> 17 c1 = Carro()

    TypeError: __init__() takes exactly 3 arguments (1 given)



bla bla bla:

.. code-block:: python

    c1 = Carro('Fiat', '147')
    c1.ignicao()

.. code-block:: console

    Motor ligado!



bla bla bla:

.. code-block:: python

    c1.ignicao()

.. code-block:: console

    Motor desligado!



bla bla bla:

.. code-block:: python

    print(f'Marca: {c1.marca}\nModelo: {c1.modelo}')

.. code-block:: console

    Marca: Fiat
    Modelo: 147


Método __str__:

.. code-block:: python

    print(c1)

.. code-block:: console

    <__main__.Carro object at 0x7f1f6313eed0>



bla bla bla:

.. code-block:: python

    repr(c1)

.. code-block:: console

    '<__main__.Carro object at 0x7f1f6313eed0>'



bla bla bla:

.. code-block:: python

    class Carro(object):
        motor_ligado = False    

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def __str__(self):
            return '%s - %s' % (self.marca, self.modelo)

        def ignicao(self):
            if (self.motor_ligado):
                self.motor_ligado = False
                print('Motor desligado!')
            else:
                self.motor_ligado = True
                print('Motor ligado!')

    c1 = Carro('Fiat', '147')
    print(c1)

.. code-block:: console

    Fiat - 147


bla bla bla:

.. code-block:: python

    repr(c1)

.. code-block:: console

    '<__main__.Carro object at 0x7f1f631273d0>'


Método Definido Externamente à Classe
-------------------------------------



bla bla bla:

.. code-block:: python

    def metodo_externo(self, frase, numero):
        self.numero = numero
        print(frase)


    class MinhaClasse(object):
        pass

    o = MinhaClasse()

    MinhaClasse.metodo = metodo_externo

    o.metodo('Bla bla bla', 800)


Bla bla bla



bla bla bla:

.. code-block:: python

    print(o.numero)

.. code-block:: console

    800

Método Definido Externamente ao Objeto:

.. code-block:: python

    def metodo_objeto(self):
        return 'X'

    o.metodo_x = metodo_objeto

    o.metodo_x()


.. code-block:: console

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-41-2f98daa957c2> in <module>()
    ----> 1 o.metodo_x()

    TypeError: metodo_objeto() takes exactly 1 argument (0 given)



bla bla bla:

.. code-block:: python

    o.metodo_x(o)

.. code-block:: console

    'X'


Objetos com Atributos Dinâmicos
-------------------------------


Criação da classe Carro:

.. code-block:: python

    class Carro(object):
        marca = ''
        modelo = ''




Criação de um objeto da classe Carro:

.. code-block:: python

    c1 = Carro()


Vejamos agora o dicionário de atributos com seus respectivos valores:

.. code-block:: python

    print(c1.__dict__)

.. code-block:: console

    {}

O atributo especial __dict__, em um objeto, é um dicionário que é usado para guardar atributos e seus respectivos valores.
O dicionário em questão apresentou um conjunto vazio.

Agora vamos preencher os atributos:

.. code-block:: python

    c1.marca = 'Porsche'
    c1.modelo = '911'

Consulta ao dicionário do objeto novamente:
	
print(c1.__dict__)

.. code-block:: console

    {'modelo': '911', 'marca': 'Porsche'}


Com os atributos preenchidos com valores agora o dicionário não está mais vazio.
Python é tão flexível que nos permite até criar um atributo “on the fly”:

.. code-block:: python

    c1.ano = 1993
	print(c1.__dict__)

.. code-block:: console

    {'ano': 1993, 'modelo': '911', 'marca': 'Porsche'}

E que tal se pudermos no momento da criação do objeto, além de poder atribuir valores
aos atributos existentes, também criar atributos que não existem na classe?

Criação da classe Carro agora utilizando o método construtor (__init__()), o qual fará
o trabalho de associar ao objeto instanciado cada par chave / valor declarado:

.. code-block:: python

    class Carro(object):
        marca = ''
        modelo = ''
        
        # Metodo construtor
        def __init__(self, **kargs):
            for chave,valor in kargs.items():
                self.__dict__[chave] = valor


Criação do objeto com atributos dinâmicos:

.. code-block:: python

    c1 = Carro(marca = 'Porsche', modelo = '911', cor = 'verde', ano = 1991)


Verificando o dicionário do objeto:

.. code-block:: python

    print(c1.__dict__)

.. code-block:: console

    {'ano': 1991, 'modelo': '911', 'marca': 'Porsche', 'cor': 'verde'}


O Método super()

bla bla bla:

.. code-block:: python

    class Mae(object):
        def metodo(self):
            print('Método da classe Mae')

    class Filha(Mae):
        def metodo(self):
            super().metodo() # Chamando o método da classe mãe
            print('Método da classe Filha')


    o = Filha()

    o.metodo()