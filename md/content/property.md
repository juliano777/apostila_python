---
title: Encapsulamento
---

|   O conceito de encapsulamento no geral consiste em isolar atributos e
  / ou métodos de acesso externo deixando-os como privados.
|   Atributos privados devem ser acessados ou modificados através de
  *getters* e *setters*, respectivamente.
|   Métodos privados têm sua área de atuação restrita somente
  internamente na classe.

# Modificador Private (\_\_)

|   Colocando 2 (dois) underscores antecedendo o atributo, ele fica
  privado, ou seja, não é acessível fora da classe.
|   Em Python não existem modificadores de atributos e métodos como em
  outras linguagens, ou seja, não existe *public*, *private* ou
  *protected*.

Criação de uma classe de teste:

``` python
class Foo(object):
    __atributo = 0
```

Instância da classe:

``` python
f = Foo()
```

Tentativa de acesso a atributo privado:

``` python
f.__atributo
```

``` console
. . .
AttributeError: 'Foo' object has no attribute '__atributo'
```

|   Por ser um atributo privado, seu acesso externo não foi reconhecido.

# Property

|   Property é a solução pythônica para implementar getters e setters de
  forma inteligente e podendo inclusive impor restrições.

Criação da classe Carro:

``` python
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
```

Instância da classe Carro:

``` python
c = Carro()
```

Tentativa de acesso ao atributo privado:

``` python
c.__velocidade
```

``` console
AttributeError: 'Carro' object has no attribute '__velocidade'
```

Acessando a property velocidade:

``` python
c.velocidade
```

``` console
Velocidade: 0 km/h
0
```

Atribuindo um valor para a property:

``` python
c.velocidade = 200
```

``` console
Velocidade = 200 km/h
```

O que acontece se pegarmos o nome do atributo privado e o definirmos
externamente?:

``` python
c.__velocidade = 'valor equivocado'
```

Acessando o atributo adicionado:

``` python
c.__velocidade                                                                                                                                                                                            
```

``` console
'valor equivocado'
```

Será que a property foi afetada?:

``` python
c.velocidade
```

``` console
Velocidade: 200 km/h
```

|   Felizmente a property não foi afetada e o encapsulamento foi mantido
  :)

Reatribuir um novo valor:

``` python
c.velocidade = 170                                                                                                                                                                                        
```

``` console
Velocidade = 170 km/h
```

Consultar o valor do atributo:

``` python
c.velocidade
```

``` console
Velocidade: 170 km/h
170    
```

Tentativa de atribuir um valor não permitido:

``` python
c.velocidade = 301
```

``` console
. . .

ValueError: A velocidade máxima permitida é de 300 km/h
```

Remover a property:

``` python
del c.velocidade
```

``` console
Removendo a propriedade de velocidade
```

Tentativa de acesso à property apagada:

``` python
c.velocidade
```

``` console
AttributeError: 'Carro' object has no attribute '_Carro__velocidade'
```

## Property como Decorator

|   Além da já citada implementação de property, pode-se também fazer
  isso por meio de decorators.

Criação de classe com definição de properties via decorators:

``` python
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
```

|   Repetir os comandos do exercício anterior ;)

# Descriptors

|   São objetos Python que implementam um método do protocolo descritor,
  que nos permite criar objetos que

tenham um comportamento desejado quando seus atributos são acessados por
outros objetos.

Criação de uma classe descriptor:

``` python
class Verbose(object):

    def __get__(self, obj, type=None) -> object:
        return 7

    def __set__(self, obj, value) -> None:
        raise AttributeError('Não pode mudar o valor!!!')

    def __delete__(self, obj, type=None) -> None:
        raise AttributeError('Não pode remover o atributo!!!')
```

Criação de uma classe de teste para o descriptor:

``` python
class Foo(object):
    atributo = Verbose()
```

Instanciação da classe Foo:

``` python
o = Foo()
```

Verificação do tipo do atributo que utiliza o descriptor:

``` python
type(o.atributo)                                                                                                                                                                                           
```

``` console
int
```

Exibe o valor do atributo:

``` python
print(o.atributo)                                                                                                                                                                                          
```

``` console
7
```

Tentativa de atribuir um novo valor ao atributo:

``` python
o.atributo = 9
```

``` console
AttributeError: Não pode mudar o valor!!!
```

|   Houve um lançamento de exceção ao tentar redefinir o valor do
  atributo.

Tentativa de remover o atributo do objeto:

``` python
del o.atributo
```

``` console
AttributeError: Não pode remover o atributo!!!
```

|   Houve um lançamento de exceção ao tentar remover o atributo.

Verificando se o atributo foi alterado:

``` python
print(o.atributo)
```

``` console
7
```
