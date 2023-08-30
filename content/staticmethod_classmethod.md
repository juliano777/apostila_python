# Método de classe e método estático

|   Existem dois tipos de métodos que podem ser executados diretamente
  de uma
| classe, ou seja, sem precisar criar um objeto dela. Por serem
  independentes
| de objetos não esperam um \"[self]{.title-ref}\" como primeiro
  parâmetro.
|   A utilidade desses métodos é para processamento de dados de classes
  em vez
| de instâncias.
|   Mesmo que isso possa ser feito por uma função escrita externamente à
  classe,
| não terá uma associação a essa classe e não poderão ser herdados por
  classes
| filhas.
|   Métodos estáticos são usados para agrupar funções que têm conexão
  lógica com
| a classe.
|   Métodos de classe são usados para o mesmo fim que os métodos
  estáticos, mas
| que também podem processar dados da classe diretamente.

Observe no exemplo a seguir as diferentes assinaturas para
respectivamente os métodos comum, de classe e estático:

``` python
class Foo(object):

    def metodo_comum(self):
        print(f'Método comum {self}')

    @classmethod
    def metodo_de_classe(cls):
        print(f'Método de classe {cls}')

    @staticmethod
    def metodo_estatico():
        print('Método estático')
```

|   Na classe foram declarados três métodos, sendo que o primeiro que é
  um
| método comum, cujo primeiro argumento é o tradicional self que
  representa a
| instância (objeto) criada a partir da classe.
|   O segundo método é decorado com \@classmethod, faz desse um método
  de
| classe, o qual não faz necessária a criação de um objeto para ser
| utilizado.
|   Esse tipo de método é invocado da seguinte forma:
| 
| [Classe.metodo_de_classe().]{.title-ref}
| 
|   Ainda sobre o método de classe um detalhe interessante é o \"cls\"
  em vez de
| self.
|   A variável \"cls\" é utilizada com um propósito similar ao de self.
  No caso
| representa a classe à qual o método pertence.
|   Como self, cls é apenas uma convenção, deixando ao gosto do usuário,
  se o
| mesmo quiser utilizar outro nome.
|   E por fim o método estático, decorado com \@staticmethod é como uma
  função
| definida externamente à classe. Não recebe um \"self\" ou um \"cls\".

Chamada do método comum pela classe:

``` python
Foo.metodo_comum()
```

``` console
TypeError: metodo_comum() missing 1 required positional argument: 'self'
```

|   Observa-se que se for feita uma tentativa de invocar a partir da
  classe um
| método que não seja nem de classe e nem estático será retornado um
  erro.

Invocando um método de classe a partir da classe:

``` python
Foo.metodo_de_classe()
```

``` console
Método de classe <class '__main__.Foo'>
```

Invocando um método estático a partir da classe:

``` python
Foo.metodo_estatico()
```

``` console
Método estático
```

Criação de objeto:

``` python
o = Foo()
```

|   A instância \"o\" é implicitamente passada como argumento para o
  método
| construtor que não foi declarado.

Chamada do método comum pela instância:

``` python
o.metodo_comum()
```

``` console
Método comum <__main__.Foo object at 0x7f40d812d410>
```

Chamada do método de classe pela instância:

``` python
o.metodo_de_classe()
```

``` console
Método de classe <class '__main__.Foo'>
```

Chamada do método estático pela instância:

``` python
o.metodo_estatico()
```

``` console
Método estático
```
