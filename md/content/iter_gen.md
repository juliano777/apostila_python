# Iteratoradores e geradores

## Iterator

> Um iterator (iterador) permite acessar elementos de uma coleção /
> sequência, retornando cada elemento sequencialmente. Todo objeto que
> tiver o método \_\_next\_\_() é um iterator.

Criação de um iterator com uma string:

``` python
it = iter('bar')
```

Representação:

``` python
repr(it)
```

``` console
'<iterator object at 0x7f123cd62c50>'
```

Executando o método \_\_next\_\_ até seu fim:

``` python
it.__next__()
```

``` console
'b'
```

``` python
it.__next__()
```

``` console
'a'
```

``` python
it.__next__()
```

``` console
'r'
```

``` python
it.__next__()
```

``` console
StopIteration:

    Bla bla bla
```

|   Nota-se que a iteração foi feita sobre a string declarada, de forma
  a
| retornar caractere por caractere e após o último foi lançada uma
  exceção
| indicando que não há mais elementos a serem retornados.

## Classe Iterator

|   É possível também implementar um iterador como um objeto de uma
  classe
| personalizada.
|   É necessário implementar os métodos \_\_iter\_\_ e \_\_next\_\_.
|   \_\_iter\_\_ retorna o objeto iterador por si.
|   \_\_next\_\_ retorna o próximo item da coleção e ao alcançar o fim e
  se
| houver uma chamada sequente uma exceção é lançada (StopIteration).

Criação da classe de iterador:

``` python
class FirstNumbers(object):

def __init__(self, n):
    self.n = n
    self.i = 0

def __iter__(self):
    return self


def __next__(self):
    if self.i <= self.n:
        cur = self.i
        self.i += 1
        return cur
    else:
        raise StopIteration()
```

Somatória dos 10 primeiros números:

``` python
print(sum(FirstNumbers(10)))
```

``` console
45
```

## Generator

Um generator é um objeto iterável assim como um iterator, mas nem todo
iterator é um generator.  
Funções de generator permite declarar uma função que se comporta como um
iterador, podendo ser usadas em *loops*.  
Um generator implementa o conceito de *lazy evaluation*, o que faz com que em
determinadas situações economize-se recursos de processamento, pois cada 
elemento é processado conforme a demanda.  
   
Criando um objeto range que vai de 0 a 9:

``` python
numeros = range(0, 10)
```

Se for utilizado list comrprehension será gerada uma lista:

``` python
rq = [x ** 2 for x in numeros]
```

Verificando os elementos:

``` python
rq
```

``` console
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

Verificando o tipo:

``` python
type(rq)
```

``` console
list
```

Tuple comprehension é uma maneira de se criar um generator:

``` python
rq = (x ** 2 for x in numeros)
```

Verificando o tipo do objeto:

``` python
type(rq)
```

``` console
generator
```

Executando o método dunder next até o fim dos elementos:

``` python
rq.__next__()
```

``` console
0
```

``` python
rq.__next__()
```

``` console
1
```

. . .

``` console
81
```

``` python
rq.__next__()
```

``` console
StopIteration:

    Bla bla bla
```

### Funções Generator

|   Uma função generator utiliza o comando yield em vez de return, o que
  faz
| com que retorne o próximo elemento da sequência.

Criação de uma função generator:

``` python
def gen():

i = 0

while i < 10:
    yield i
    i += 1
```

Criação do gerador via execução da função:

``` python
x = gen()
```

Verificando os tipos:

``` python
type(gen)
```

``` console
function
```

``` python
type(x)
```

``` console
generator
```

Execução do método \_\_next\_\_ até o fim:

``` python
x.__next__()
```

``` console
0
```

. . .

``` python
x.__next__()
```

``` console
9
```

``` python
x.__next__()
```

``` console
StopIteration:
```

## Iterator vs generator

- Para criar um generator utilizamos ou uma função com `yield` no lugar de
  `return` ou *tuple comprehension*.
  Para criar um iterador utiliza-se a função `iter()`;
- Generator utiliza `yield`, iterator não;
- Gerador salva o estado de variáveis locais a cada vez que o `yield` pausa o
  *loop*.
  Um iterador não faz uso de variáveis locais, tudo o que ele precisa é faz a
  iteração.
- Iteradores fazem uso mais eficiente de memória.

Do módulo `timeit` importar a função de mesmo nome:

``` python
from timeit import timeit
```

Verificação de tipos:

``` python
type(iter([x for x in range(1, 1001)]))
```

``` console
list_iterator
```

``` python
type((x for x in range(1, 1001)))
```

``` console
generator
```

Strings com código em loop sobre iterador e gerador, respectivamente:

``` python
code_it = '''                                
for i in (iter([x for x in range(1, 1001)])):
    pass
'''
```

``` python
code_gen = '''                                
for i in ((x for x in range(1, 1001))):
    pass
'''
```

Cronometrando os códigos de iterador e gerador, respectivamente:

``` python
timeit(code_it)
```

``` console
42.666774257901125
```

``` python
timeit(code_gen)
```

``` console
53.58039242995437
```
