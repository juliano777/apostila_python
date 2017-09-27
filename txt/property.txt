Encapsulamento

Modificador Private (__)

	Colocando 2 (dois) caracteres underscore antecedendo o atributo, ele fica privado, ou seja, não é acessível fora da classe.

class Foo(object):
    __atributo = 0

f = Foo()

f.__atributo

. . . 

AttributeError: 'Foo' object has no attribute '__atributo'




class Carro(object):
    def __init__(self):
        self.__velocidade = 0
        
    def _get__velocidade(self):
        print('Velocidade: %d km/h' % self.__velocidade)
        return self.__velocidade
    
    def _set__velocidade(self, velocidade):
        if velocidade > 300:
            raise ValueError('A velocidade máxima permitida é de 300 km/h')        
        self.__velocidade = velocidade
        print('Velocidade = %d km/h' % self.__velocidade)
        
    def _del__velocidade(self):
        print('Removendo a propriedade de velocidade')
        del self.__velocidade
    
    velocidade = property(_get__velocidade, _set__velocidade, _del__velocidade,
                          'Velocidade máxima do carro')


c = Carro()

c.__velocidade

.  .  .

AttributeError: 'Carro' object has no attribute '__velocidade'


c.velocidade
Velocidade: 0 km/h
0

c.velocidade = 200
Velocidade = 200 km/h

c.velocidade = 301

. . .

ValueError: A velocidade máxima permitida é de 300 km/h



del c.velocidade
Removendo a propriedade de velocidade

c.velocidade

. . .

AttributeError: 'Carro' object has no attribute '__velocidade'


class Carro(object):
    def __init__(self):
        self.__velocidade = 0
        
    @property 
    def velocidade(self):
        '''Velocidade máxima do carro'''
        print('Velocidade: %d km/h' % self.__velocidade)
        return self.__velocidade
    
    @velocidade.setter    
    def velocidade(self, velocidade):
        if velocidade > 300:
            raise ValueError('A velocidade máxima permitida é de 300 km/h')        
        self.__velocidade = velocidade
        print('Velocidade = %d km/h' % self.__velocidade)
        
    @velocidade.deleter   
    def velocidade(self):
        print('Removendo a propriedade de velocidade')
        del self.__velocidade
