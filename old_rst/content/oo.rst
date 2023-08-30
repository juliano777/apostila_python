Orientação a Objetos
********************

|   Python suporta herança múltipla;
|	Tudo em Python é objeto (inclusive classes);
|	O método construtor é o método inicializador, o método mágico `__init__`;



Exemplo de criação de uma classe:

.. code-block:: python
    
    class NomeClasse(ClasseMae):
        # Método construtor ou método inicializador (sem parâmetro)
        def __init__(self):        
            pass

        # Método comum com 1 (um) parâmetro
        def metodo(self, foo):
            return foo


|   Em Python a definição de uma classe é bem simples. Usamos o comando class
| seguindo do nome da classe a ser criada, logo em seguida vindo entre
| parênteses os nomes das classes mãe separados por vírgulas, pois em Python é
| permitida herança múltipla.
|   O método construtor, também chamado de método inicializador é o `__init__`.



Herança múltipla; a terceira classe herda das duas primeiras:

.. code-block:: python

    class Foo(object):
        nome = ''

    class Bar(object):
        idade = 0

        def metodo_teste(self):
            print('Teste')

    class Baz(Foo, Bar):

        # Método construtor exige que se passe o sobrenome
        def __init__(self, sobrenome):
            self.sobrenome = sobrenome 

        altura = 0.0

Instanciação da classe e testes com seus atributos:

.. code-block:: python

    o = Baz('da Silva')
    o.nome = 'Chiquinho'
    o.idade = 51
    o.altura = 1.6

    s = (f'{o.nome} {o.sobrenome} '
         f'tem {o.idade} anos e '
         f'{o.altura:.2f}m de altura')

    print(s)



.. code-block:: console

    Chiquinho da Silva tem 51 anos e 1.60m de altura


|   Obs.: Em Python todos métodos e atributos são públicos.
|   Há uma convenção que colocando um unerline como primeiro caractere no nome
| de um atributo ou um método o sinaliza como privado.
|   Porém, isso é apenas uma convenção. Nada impede que sejam acessados
| externamente.
|   Para que haja um bloqueio efetivo há um recurso na linguagem chamado
| "property".



Criação de classe com método construtor e um método personalizado:

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

|   O método construtor requer que sejam passados dois parâmetros: marca e
| modelo.                



Tentativa de criar uma instância da classe sem passar parâmetros:

.. code-block:: python

    c1 = Carro()

.. code-block:: console

    TypeError                                 Traceback (most recent call last)
    <ipython-input-13-e2526cbd1648> in <module>()
        15 
        16 
    ---> 17 c1 = Carro()

    TypeError: __init__() takes exactly 3 arguments (1 given)



Instanciação correta da classe Carro:

.. code-block:: python

    c1 = Carro('Fiat', '147')
    c1.ignicao()

.. code-block:: console

    Motor ligado!



Método ignicao:

.. code-block:: python

    c1.ignicao()

.. code-block:: console

    Motor desligado!



Exibindo atributos via print:

.. code-block:: python

    print(f'Marca: {c1.marca}\nModelo: {c1.modelo}')

.. code-block:: console

    Marca: Fiat
    Modelo: 147



Métodos __str__ e __repr__
--------------------------

**__str__**

|   É o método dunder cujo objetivo é a representação em string do objeto.
|   Esse método é chamado quando as funções `print()` e `str()` tem um objeto
| como parâmetro.

**__repr__**

|   É o método dunder de representação do objeto, que pode ser algo além de
| uma string.
|   Este método é chamado quando se apenas usa o nome da instância.


Diferenças entre __str__ e __repr__
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Se não houver implementação de __str__ então __repr__ será chamado no lugar.
Por outro lado se __repr__ não for implementado, nada fará seu papel;
- Se o método __repr__ retornar uma string, pode-se pular a implementação de
__str__.
- Costuma-se dizer que __str__ é um método para usuários enquanto __repr__ é
um método para desenvolvedores.   



Aproveitando o exercício anterior, usando a função print no objeto:

.. code-block:: python

    print(c1)

.. code-block:: console

    <__main__.Carro object at 0x7f1f6313eed0>



Função repr com o objeto:

.. code-block:: python

    repr(c1)

.. code-block:: console

    '<__main__.Carro object at 0x7f1f6313eed0>'

|   Nem __str__ nem __repr__ originais foram humanamente amigáveis...



Criação da classe carro com implementação do método __str__ e teste com
objeto:

.. code-block:: python

    class Carro(object):
        motor_ligado = False    

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def __str__(self):
            return f'{self.marca} - {self.modelo}'

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


Função repr com o objeto:

.. code-block:: python

    repr(c1)

.. code-block:: console

    '<__main__.Carro object at 0x7f1f631273d0>'



Criação da classe carro com implementação do método __repr__ e teste
com objeto:

.. code-block:: python

    class Carro(object):
        motor_ligado = False    

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def __repr__(self):
            return f'{self.marca} - {self.modelo}'

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


Função repr com o objeto:

.. code-block:: python

    repr(c1)

.. code-block:: console

    Fiat - 147



Criação da classe carro com implementação dos métodos __repr__ e __str__ e
teste com objeto:

.. code-block:: python

    class Carro(object):
        motor_ligado = False    

        def __init__(self, marca, modelo):
            self.marca = marca
            self.modelo = modelo

        def __str__(self):
            return f'{self.marca} - {self.modelo}'
            
        def __repr__(self):
            return {'marca': self.marca, 'modelo': self.modelo}

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



Método __repr__ do objeto:

.. code-block:: python

    c1.__repr__()

.. code-block:: console

    {'marca': 'Fiat', 'modelo': '147'}



Função repr com o objeto:

.. code-block:: python

    repr(c1)

.. code-block:: console

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-58-3772d9a2a4c4> in <module>
    ----> 1 repr(c1)

    TypeError: __repr__ returned non-string (type dict)

|   A função repr exige que seja passado como string...



Como o método __repr__ tem seu retorno como um dicionário ele pode ser
aproveitado:

.. code-block:: python

    print(c1.__repr__()['modelo'])

.. code-block:: console

    147



Método Definido Externamente à Classe
-------------------------------------

|   Após criarmos uma classe é possível adicionar novos métodos a ela
| definindo-os externamente.



Criação de uma classe se, métodos:

.. code-block:: python

    class MinhaClasse(object):
        pass



Criação de uma função:

.. code-block:: python

    def metodo_externo(self, frase, numero):
        self.numero = numero
        print(frase)



Instanciação da classe:

.. code-block:: python

    o = MinhaClasse()



Atribuindo um novo método à classe através da função externa criada:

.. code-block:: python

    MinhaClasse.metodo = metodo_externo



Mesmo o método ter sido adicionado depois:

.. code-block:: python

    o.metodo('Bla bla bla', 800)

.. code-block:: python

    Bla bla bla



Verificando o atributo novo:

.. code-block:: python

    print(o.numero)

.. code-block:: console

    800




Objetos com Atributos Dinâmicos
-------------------------------

|   Sua serventia está em poder definir um objeto com atributos definidos
| arbitrariamente.



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

|   O atributo especial __dict__, em um objeto, é um dicionário que é usado
| para guardar atributos e seus respectivos valores.
|   O dicionário em questão apresentou um conjunto vazio.

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

|   E se no momento da criação do objeto, além de atribuir valores aos
| atributos existentes, também ser possível criar atributos que não existem
| na classe?

Criação da classe Carro agora utilizando o método construtor (__init__()), o
qual fará o trabalho de associar ao objeto instanciado cada par chave / valor
declarado:

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


super()
-------

|   É uma função built-in que retorna o objeto proxy que nos permite 
| referenciar à uma classe superior (uma classe herdada).
|   super() pode ser usada para ter acesso a métodos herdados que são da
| classe superior.



Uma herança simples na qual a classe filha chama o métod da classe mãe:

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

.. code-block:: console

    Método da classe Mae
    Método da classe Filha



Herança de Nível Múltiplo
~~~~~~~~~~~~~~~~~~~~~~~~~

|   Podem ter casos em que uma classe que deriva de outra tenha uma classe que
| deriva dela.



A classe C herda de B, que por sua vez herda de A:

.. code-block:: python

    # Classe primária A
    class A(object):
        def __init__(self):
            print('__init__ da classe A')
            
    # Classe derivada B
    class B(A):
        def __init__(self):
            print('__init__ da classe B')
            super().__init__()

    # Classe derivada C
    class C(B):
        def __init__(self):
            print('__init__ da classe C')
            super().__init__()



Instanciação da classe de nível mais baixo:

.. code-block:: python

    c = C()

.. code-block:: python

    __init__ da classe C
    __init__ da classe B
    __init__ da classe A

|   Nota-se que ordem de chamada do método __init__.



MRO - Method Resolution Order / Ordem de Resolução de Método
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|   MRO é a forma que Python utiliza para determinar a ordem de busca em
| classes.



Definição de duas classes primárias e mais duas derivadas delas com múltipla
herança:

.. code-block:: python

    # Classe primária A
    class A(object): 
        def metodo(self): 
            print('Método da classe A')
            
    # Classe primária B 
    class B(object): 
        def metodo(self): 
            print('Método da classe B')
            

    #=============================================================================
    # Herança de Múltiplas Classes
    #=============================================================================

    # Classe C, derivada respectivamente de A e B
    class C(A, B): 
        def metodo(self):
            super().metodo()
            print('Método da classe C')
            
    # Classe D, derivada respectivamente de B e A        
    class D(B, A): 
        def metodo(self):
            super().metodo()
            print('Método da classe D')



Instanciação de dois objetos, respectivamente das classes C e D:

.. code-block:: python

    c = C()
    d = D()



Em cada instância criada execução do método:

.. code-block:: python

    c.metodo()

.. code-block:: console

    Método da classe A
    Método da classe C

.. code-block:: python

    d.metodo()

.. code-block:: console

    Método da classe B
    Método da classe D

|   Nota-se que prevaleceu a lógica de Ordem de Resolução de Método (em inglês
| MRO).
|   Tal ordem foi conforme a ordem de definição de herança da classe.



Agora além do primeiro método, igual ao exercício anterior, vamos definir um
método particular para a cada classe primária:

.. code-block:: python

    #=============================================================================
    # Classes Primárias com Métodos de Nomes Diferentes
    #=============================================================================

    # Classe primária A
    class A(object): 
        def metodo(self): 
            print('Método da classe A')
            
        def metodo_alpha(self):
            print('Método alpha da classe A')
            
    # Classe primária B 
    class B(object): 
        def metodo(self): 
            print('Método da classe B')
        
        def metodo_beta(self):
            print('Método beta da classe B')
            

    #=============================================================================
    # Herança de Múltiplas Classes
    #=============================================================================

    # Classe C, derivada respectivamente de A e B
    class C(A, B): 
        def metodo(self):
            super().metodo()
            print('Método da classe C')
            
        def metodo2(self):
            super().metodo_alpha()
            super().metodo_beta()        
            
    # Classe D, derivada respectivamente de B e A        
    class D(B, A): 
        def metodo(self):
            super().metodo()
            print('Método da classe D')
            
        def metodo2(self):
            super().metodo_alpha()
            super().metodo_beta()

Instanciação das classes derivadas:

.. code-block:: python

    c = C()
    d = D()



Execução dos métodos:

.. code-block:: python

    c.metodo()

.. code-block:: console

    Método da classe A
    Método da classe C    
    
.. code-block:: python

    d.metodo()

.. code-block:: console

    Método da classe B
    Método da classe D

|   Até aqui, na execução do método está igual ao exercício anterior.



Agora em cada objeto vamos chamar o segundo método, o qual faz chamada a
métodos de nomes diferentes que são próprios à sua respectiva classe:

.. code-block:: python

    c.metodo2()

.. code-block:: console

    Método alpha da classe A
    Método beta da classe B        

.. code-block:: python

    d.metodo2()

.. code-block:: console

    Método alpha da classe A
    Método beta da classe B

|   Mais uma vez notamos a aplicação do conceito de MRO.
|   Quando super chamou os métodos metodo_alpha e metodo_beta não havia uma
| menção explícita onde estavam.