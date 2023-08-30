# Comandos e funções importantes


> Neste capítulo são abordados comandos e funções interessantes e / ou
> imprescindíveis para a linguagem.

# all() e any()

> A função [all()]{.title-ref} analisa cada elemento de um iterável e
> retorna [True]{.title-ref} se **todos** esses elementos forem
> [True]{.title-ref}. Enquanto que para a função [any()]{.title-ref}
> basta que **apenas um elemento** seja [True]{.title-ref} para retornar
> [True]{.title-ref}.

``` python
# Todos elementos verdadeiros
x = (True, True, True)

# Todos elementos são verdadeiros?
all(x)
```

``` console
True
```

``` python
# Há pelo menos um elemento verdadeiro?
any(x)
```

``` console
True
```

``` python
# Todos elementos falsos
y = (False, False, False)

# Todos elementos são verdadeiros?
all(y)
```

``` console
False
```

``` python
# Há pelo menos um elemento verdadeiro?
any(y)
```

``` console
False
```

``` python
# Apenas um elemento verdadeiro
z = (False, True, False)

# Todos elementos são verdadeiros?
all(z)
```

``` console
False
```

``` python
# Há pelo menos um elemento verdadeiro?
any(z)
```

``` console
True
```

``` python
# Dentre todos os outros elementos verdadeiros, um nulo
w = (True, True, True, True, True, True, True, True, None)

# Todos elementos são verdadeiros?
all(w)
```

``` console
False
```

``` python
# Há pelo menos um elemento verdadeiro?
any(w)
```

``` console
True
```

# iter() e next()

A função [iter()]{.title-ref} cria um objeto iterador cujos elementos
podem ser acessados na sequência pela função [next()]{.title-ref}.

Sintaxes gerais:

[iter(object\[, sentinel\])]{.title-ref}

O parâmetro sentinela ([sentinel]{.title-ref}) é opcional. Porém, se o
mesmo for declarado, o objeto tem que ser \"chamável\" (*callable*).
Esse parâmetro sentinela

[next(iterator\[, default\])]{.title-ref}

O valor [default]{.title-ref} é opcional, cujo objetivo é ao se atingir
o fim dos elementos do objeto iterador em vez de retornar uma exceção,
seu valor exibido toda vez que for chamado.

``` python
# Criação de uma simples lista
lista = ['A', 0, True, 5.2, -3, 'z'1]

# Criação de um objeto iterador a partir da lista
my_iter = iter(lista)

# Executar a chamada do próximo elemento até a exaustão
next(my_iter)
```

``` 
'A'
```

``` 
next(my_iter)
```

``` console
0
```

``` python
next(my_iter)
```

``` console
True
```

``` python
next(my_iter)
```

``` console
5.2
```

``` python
next(my_iter)
```

``` console
-3
```

``` python
next(my_iter)
```

``` console
'z'
```

``` python
next(my_iter)    
```

``` console
In [103]: next(my_iter)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [103], line 1
----> 1 next(my_iter)

StopIteration:
```

Aqui nota-se uma exceção que foi lançada devido ao iterador ter sido
exaurido.

``` python
# Criação de um iterador a partir da lista
my_iter = iter(lista)

# Criação de uma função lambda que retorna o próximo valor do iterador
f = lambda : next(my_iter)

# Criação de um iterador com sentinela
iter_sentinel = iter(f, -3)

# Verificar o próximo valor
next(iter_sentinel)
```

``` console
'A'
```

``` python
next(iter_sentinel)
```

``` console
0
```

``` python
next(iter_sentinel)
```

``` console
True
```

``` python
next(iter_sentinel)
```

``` console
5.2
```

``` python
next(iter_sentinel)    
```

``` console
next(iter_sentinel)
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
Cell In [137], line 1
----> 1 next(iter_sentinel)

StopIteration:
```

Novamente o iterador foi exaurido e por isso lançou uma exceção.

``` python
# Criação de um iterador a partir de uma lista
my_iter = iter(lista)

# Criação de um iterador com sentinela
iter_sentinel = iter(f, -3)

# Execução de next() com um valor padrão
next(iter_sentinel, 'Fim')
```

``` console
'A'
```

``` python
next(iter_sentinel, 'Fim')
```

``` console
0
```

``` python
next(iter_sentinel, 'Fim')
```

``` console
True
```

``` python
next(iter_sentinel, 'Fim')
```

``` console
5.2
```

``` python
next(iter_sentinel, 'Fim')
```

``` console
'Fim'
```

``` python
next(iter_sentinel, 'Fim')
```

``` console
'Fim'
```

Após exaurido, por duas vezes, não foi lançada uma exceção, mas sim
retornado um valor padrão.

# print()

> Em Python 2 era um comando e em Python 3 passou a ser exclusivamente
> uma função. Seu objetivo é imprimir uma mensagem que por padrão é
> STDOUT.

``` python
# Um simples "Hello, world!":

print('Hello, world!')
```

``` console
Hello, world!
```

``` python
# Pode-se passar mais de uma string como parâmetro:

print('foo', 'bar', 'baz')
```

``` console
foo bar baz
```

``` python
# Colocando como separador uma nova linha para cada string passada como parâmetro

print('foo', 'bar', 'baz', sep='\n')
```

``` console
foo
bar
baz
```

# len()

> Função que retorna a quantidade de itens de um contêiner.

``` python
# Criação de um objeto contêiner e verificação da quantidade de elementos
foo = ('x', 'y', 'z', 123, 5.7)

# len(foo)
```

``` console
5
```

``` python
# Tamanho de uma string
len('Heavy Metal')
```

``` console
11    
```

# range()

> É uma função que retorna um objeto com uma faixa inteiros (range
> object). Muito útil para uso em loops.

Sintaxe:

> range(stop) range(start, stop\[, step\])
>
> start: Valor inicial da sequência, por padrão é 0 (zero). stop: Valor
> final da sequẽncia - 1. step: Valor de incremento, cujo padrão é 1
> (um), quando start é maior que stop, ou seja, para se fazer uma
> sequência regressiva é preciso um número negativo.

``` python
# Um parâmetro (stop)
for i in range(5):
    print(i)
```

``` console
0
1
2
3
4
```

``` python
# Dois parâmetros (start e stop)
for i in range(3, 10):
    print(i)
```

``` console
3
4
5
6
7
8
9
```

``` python
# Três parâmetros (start, stop e step)
for i in range(1, 10, 2):
    print(i)
```

``` console
1
3
5
7
9
```

``` python
# Sequẽncia regressiva
for i in range(20, 1, -5):
    print(i)
```

``` console
20
15
10
5
```

# filter()

> Função que retorna um iterador produzindo os itens iteráveis para os
> quais a função(item) for True.

``` python
# Criação de uma função que retorna True se o objeto for ímpar
def impar(x):
    return x % 2 != 0

# Testando a função
impar(7)
```

``` console
True
```

``` python
impar(6)
```

``` console
False
```

Em uma sequência de 0 a 19, pela função impar criar um objeto filter
somente com os elementos ímpares e posteriormente ser convertido para
lista:

``` python
f = filter(impar, range(0, 20))
print(list(f))
```

``` console
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

# map()

> Cria um iterador que aplica uma função para cada elemento do iterável.

``` python
# Dada uma tupla com várias strings, criar uma lista 
# com o tamanho de cada string respectivamente
m = map(len, ('spam', 'foo', 'bar', 'eggs', 'Python'))
print(list(m))
```

``` console
[4, 3, 3, 4, 6]
```

``` python
# Para cada item da lista, criar uma nova lista
# com seus respectivos tipos
m = map(type, ['foo', 1.4, 2 + 5j, 1000])
print(list(m))
```

``` console
[str, float, complex, int]
```

``` python
# Para cada item da primeira lista elevar (potência)
# ao elemento respectivo na segunda lista e criar uma 
# nova lista com os resultados
m = map(pow, [3, 7, 5, 10], [2, 1, 7, 3])
print(list(m))
```

``` console
[9, 7, 78125, 1000]
```

# reduce()

> Em Python 2 estava disponível sem a necessidade de fazer importação,
> hoje em Python 3 está no módulo functools.

``` python
# Via loop somar todos elementos de uma tupla
soma = 0  # Variável que terá o valor da soma após o loop

for i in (2, 1, 4, 3):  # Loop e incrementação
    soma += i

print(soma)  # Exibe o resultado
```

``` console
10
```

``` python
# Importando reduce de functools
from functools import reduce

# Função reduce para executar a mesma
# tarefa anterior com apenas um comando
reduce(int.__add__, (2, 1, 4, 3))
```

``` console
10
```

# del

> Pode ser tanto um comando como uma função cuja finalidade é remover a
> referência de um objeto. Também apaga elemento de uma coleção.

``` python
# Teste de del em um objeto mutável (lista)
lista = ['a', 'b', 'c']  # Definição da lista
del lista[1]  # Apaga o segundo elemento da lista
```

ou

``` python
del(lista[1])  # Equivalência ao comando anterior em forma de função
print(lista)  # Exibe a lista após o elemento ser retirado da mesma
```

``` console
['a', 'c']
```

``` python
# Teste de del para desalocar um objeto criado
foo = 'bar'  # Objeto string criado
print(foo)  # Verificando o valor da string
```

``` console
bar
```

``` python
del foo  # Apagando o objeto string
print(foo)  # Tentativa de imprimir o valor do objeto desalocado
```

``` console
NameError: name 'foo' is not defined
```

Nota-se que após o del não é possível mais fazer referência ao objeto.

# ord e chr

> A função ord retorna o código Unicode de um caractere. A função chr
> faz o caminho inverso, ou seja, retorna um caractere dado um código
> Unicode. Em Python 2 chr era unichr.

``` python
ord('\n')  # Qual é o código Unicode para new line?
```

``` console
10
```

``` python
chr(10)  # Qual caractere Unicode corresponde ao código 10?
```

``` console
'\n'
```

``` python
ord('\r')  # Qual é o código unicode para carriage return?
```

``` console
13
```

``` python
chr(13)  # Qual caractere Unicode corresponde ao código 13?
```

``` console
'\r'
```

``` python
chr(97)  # Qual caractere Unicode corresponde ao código 97?
```

``` console
'a'
```

``` python
ord('a')  # Qual é o código unicode para o caractere "a"?
```

``` console
97
```

``` python
chr(120)  # Qual caractere Unicode corresponde ao código 120?
```

``` console
'x'
```

``` python
chr(981)  # Qual caractere Unicode corresponde ao código 981?
```

``` console
'ϕ'
```

# dir()

> Função que lista atributos e métodos de um elemento. Se chamada sem
> nenhum argumento retorna os nomes do escopo atual. A chamada dessa
> função é correspondente ao executar o método \_\_dir\_\_.

``` python
# Definição de variáeis
x = 0
y = 1
z = 2
```

``` python
# Execução da função dir sem parâmetros
dir()
```

``` console
['In',
 'Out',
 . . .
 'x',
 'y',
 'z']
```

``` python
# A variável foi declarada no escopo?
'x' and 'y' and 'y' and 'z' in dir()
```

``` console
True
```

``` python
'w' in dir()
```

``` console
False
```

``` python
# Criação de uma classe

class Pessoa(object):
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
```

``` python
# Verificando o conteúdo da classe (atributos e métodos)
 dir(Pessoa)
```

``` console
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
```

``` python
# Criação de um objeto da classe e definição de atributos
p = Pessoa()
p.nome = 'Chiquinho'
p.rg = '00000000'
p.cpf = 12345678901
p.email = 'chiquinho@chiquinhodasilva.xx'
```

``` python
# Atributo __dict__, é um dicionário que contém os atributos do objeto
p.__dict__
```

``` console
{'nome': 'Chiquinho', 'rg': '00000000', 'cpf': 12345678901, 'email': 'chiquinho@chiquinhodasilva.xx'}
```

``` python
# Pegando o valor do atributo pelo dicionário
p.__dict__['nome']
```

``` console
'Chiquinho'
```

``` python
# Com o auxílio da função dir, listar todos os métodos do objeto
def is_dunder(s):
    '''
    Função auxiliar que retorna True para dunder strings
    '''

    # Se começar e terminar com "__" retornar True
    if s.startswith('__') and s.endswith('__'):
        return True
    else:
        return False
```

``` python
# Utilizando a função auxiliar criada criar uma nova função
def mostra_metodos(objeto):
    '''
    Função que mostra em tela todos os nomes de métodos de um objeto
    '''

    # Generator que conterá os nomes dos métodos por tuple comprehension
    metodos = (i for i in dir(objeto)
               if callable(getattr(objeto, i))
               and (not is_dunder(i))
              )

    for i in metodos:
        print(i)
```

``` python
# Chamando a função criada para imprimir em tela os nomes dos métodos:
mostra_metodos(p)
```

``` console
dizer_nome
saudacao
```

# pass

> É um comando de operação nula, ou seja, quando é executado nada
> acontece. É útil como um marcador quando um statement é requerido
> sintaticamente, mas não tem necessidade de um código a ser executado.

``` python
# Função que nada faz:
def nula():
    pass
```

# assert

> Um statements assert é uma maneira conveniente para inserir asserções
> de debug. O comando assert verifica em tempo de execução uma
> determinada condição e se a mesma não for verdadira uma exceção
> AssertionError é lançada e se essa exceção não for tratada, o programa
> pára.

``` bash
# Criação do script com assert sem tratamento de exceção
vim /tmp/assert_sem_try.py
```

``` {.python linenos=""}
print('Começo')

assert 1 == 1  # OK
assert 2 == 1  # Ops...

print('Fim')
```

``` bash
# Execução
$ python3 /tmp/assert_sem_try.py
```

``` console
Começo
Traceback (most recent call last):
. . .
AssertionError
```

Nota-se que a execução do script não chegou até o fim.

``` bash
$ # Criação do script com assert com tratamento de exceção
vim /tmp/assert_com_try.py
```

``` {.python linenos=""}
print('Começo')

try:
    assert 1 == 1  # OK
    assert 2 == 1  # Ops...
except AssertionError:
    print('Teve erro...')

print('Fim')
```

``` bash
$ # Execução
python3.7 /tmp/assert_com_try.py
```

``` console
Começo
Teve erro...
Fim
```

# abs()

> Retorna o valor absoluto do argumento.

``` python
abs(3)
```

``` console
3
```

``` python
abs(-3)
```

``` console
3
```

# divmod()

> Função que retorna uma tupla de dois elementos no formato (x//y, x%y),
> respectivamente resultado da divisão inteira e resto da divisão:

``` python
divmod(11, 4)  # Equivalente: 11 // 4, 11 % 4
```

``` console
(2, 3)
```

# round()

> Função que retorna um número de forma arredondada dada uma precisão em
> dígitos decimais. O valor de retorno é um inteiro se o número de
> dígitos for omitido ou None. Caso contrário, o valor de retorno terá o
> mesmo tipo do número. O número de dígitos pode ser negativo.

``` python
# Arredondamento sem especificar o número de dígitos (segundo parâmetro)
round(3.333333)
```

``` console
3
```

``` python
# Arredondamento com quatro dígitos de precisão:
round(3.333333, 4)
```

``` console
3.3333
```

``` python
# Precisão variando de 1 a -3:
round(1237.87431, 1)
```

``` console
1237.9
```

``` python
#
round(1237.87431, 0)
```

``` console
1238.0
```

``` python
# 
round(1237.87431, -1)
```

``` console
1240.0
```

``` python
#
round(1237.87431, -2)
```

``` console
1200.0
```

``` python
# 
round(1237.87431, -3)
```

``` console
1000.0
```

# callable()

> Função que retorna True se o objeto é \"chamável\" (callable) (i. e.,
> algum tipo de função). Vale lembrar que classes também são chamáveis,
> bem como objetos de classes que implementam o método \_\_call\_\_().

``` python
# Criação de função comum
def f1():
    pass

# Criação de função lambda
f2 = lambda : None

# Criação de classe
class Foo(object):
    pass

# Objeto da classe Foo
o = Foo()

# Dicionário cujos elementos são os objetos criados
d = {
    'f1': 'Função comum',
    'f2': 'Função lambda',
    'Foo': 'Classe',
    'o': 'Objeto da classe Foo',
}
```

``` python
# Loop sobre chave e valor do dicionário
for k, v in d.items():
    # String formatada
    c = f'callable({k})'

    # Execução da string "c", a qual será avaliada como um comando, cujo
    # retorno é armazenado na variável
    is_callable = eval(c)

    if is_callable:
        print(f'{v}: Sim')
    else:
        print(f'{v}: Não')
```

``` console
Função comum: Sim
Função lambda: Sim
Classe: Sim
Objeto da classe Foo: Não
```

# oct()

> Função que retorna a representação octal de um inteiro.

``` python
# 
oct(9)
```

``` console
'0o11'
```

``` python
# 
oct(10)
```

``` console
'0o12'
```

# hash()

> Função que retorna o valor hash de um dado objeto. Dois objetos que
> são comparados também devem ter o mesmo valor de hash.

``` python
# Testes com a função hash
hash(1)  # O hash de um inteiro vai ser seu próprio valor
```

``` console
1
```

``` python
hash(2)
```

``` console
2
```

``` python
# Hash de uma string
x = 'foo'  
```

``` python
# Hash de uma string
hash(x)
```

``` console
8540844669962366372
```

``` python
# Nova variável y igual a x
y = x

# Por terem o mesmo valor, o hash será igual
hash(x) == hash(y)
```

``` console
True
```

``` python
# Alguns tipos como list, dict e set são unhashable
hash([1, 2, 3])
```

``` console
TypeError: unhashable type: 'list'
```

``` python
# Quando um número é muito grande seu hash será diferente de seu valor
hash(9999999999999999999)
```

``` console
776627963145224195
```

# id()

> É uma função que retorna a identidade de um objeto. É a garantia que o
> objeto será único dentre outros.

``` python
# Criação de duas tuplas
foo = ('x', 'y')
bar = ('x', 'y')

# Comparando as tuplas criadas
foo == bar
```

``` console
True
```

``` python
# Verificando o a identidade das tuplas criadas
id(foo)
```

``` console
139651439554952
```

``` python
# id(bar)
```

``` console
139651403802056
```

``` python
# É o mesmo objeto?
foo is bar
```

``` console
False
```

``` python
# Criação de uma nova variável atribuindo com base em um objeto pré-existente
baz = bar

# Comparando as variáveis
baz == bar
```

``` console
True
```

``` python
# É o mesmo objeto?
baz is bar
```

``` console
True
```

``` python
# 
id(bar) == id(baz)
```

``` console
True
```

Aqui fica demonstrado que quando se cria uma nova variável simplesmente
por atribuição é na verdade a criação de uma nova referência
(apontamento) para o mesmo objeto.

# input

> É uma função de entrada de dados pelo teclado (STDIN), cujos dados são
> interpretados como string. Opcionalmente podemos colocar uma mensagem
> para pedir uma entrada de teclado.

``` python
# Entrada de dados sem prompt
foo = input()  # Digite algo...

# Imprimindo o valor da variável
print(foo)
```

``` console
. . .
```

``` python
# Entrada de dados com prompt
foo = input('Digite uma string qualquer... ')
```

``` console
Digite uma string qualquer...
```

``` python
# Imprimindo o valor da variável
print(foo)
```

``` console
. . .
```

# min e max

> Dada uma coleção, seja ela uma lista, tupla, conjunto ou string, as
> funções min e max trazem, respectivamente, o valor mínimo e o máximo.

``` python
# Valor mínimo entre inteiros
min(0, 2, -50, 7)
```

``` console
-50
```

``` python
# Valor máximo entre inteiros
max(0, 2, -50, 7)
```

``` console
7
```

``` python
# Para caracteres a ordem alfabética é levada em conta
max('c', 'x', 'k')
```

``` console
'x'
```

# enumerate

> Função que retorna um objeto iterável.

``` python
# Criação de uma tupla
x = ('verde', 'azul', 'amarelo')

# Criação de um objeto iterável com base na tupla criada anteriormente
y = enumerate(x)

# Exibindo o tipo de y
type(y)
```

``` console
enumerate
```

``` python
# Loop sobre o iterável
for i, j in y:
    print('{} - {}'.format(i, j))
```

``` console
0 - verde
1 - azul
2 - amarelo
```

``` python
# Criar o iterável novamente
y = enumerate(x)
```

| Método \_\_next\_\_() que traz uma tupla com o índice e o valor.
| Executar 3 (três) vezes:

``` python
y. __next__()
```

``` console
(0, 'verde')
```

``` console
(1, 'azul')
```

``` console
(2, 'amarelo')
```
