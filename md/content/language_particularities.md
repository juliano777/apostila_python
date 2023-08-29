# Particularidades da Linguagem

## Palavras Reservadas

Palavras reservadas ou em inglês *keywords* são

``` text
False   class     finally  is        return  
None    continue  for      lambda    try     
True    def       from     nonlocal  while   
and     del       global   not       with    
as      elif      if       or        yield   
assert  else      import   pass              
break   except    in       raise
```

Podemos verificar as palavras reservdas de Python usando código:

``` python
from keyword import kwlist as keywords

for i in keywords:
    print(i)
```

``` console
. . .
```

## Definição do Interpretador de Comandos

> Para scripts Python, na primeira linha podemos especificar o
> interpretador de comandos a ser utilizado, também conhecido como
> shebang;

``` {.python linenos=""}
#!/usr/bin/env python3
```

::: note
::: title
Note
:::

Em ambientes Windows não é preciso espeficar, isso é pertinente a
ambientes Unix.
:::

## Codificação (Conjunto de Caracteres - Encoding)

> É possível utilizar codificações diferentes de ASCII em arquivos de
> código-fonte. A melhor maneira de se fazer isso é colocar uma linha
> especial no começo do arquivo, se foi especificado o interpretador,
> deve vir logo depois dele:

``` {.python linenos=""}
# _*_ encoding: utf-8 _*_
```

``` bash
vim /tmp/hello.py
```

``` {.python linenos=""}
#!/usr/bin/env python

print('Olá!')
```

``` bash
$ python /tmp/hello.py
```

``` console
File "/tmp/hello.py", line 4
SyntaxError: Non-ASCII character '\xc3' in file /tmp/hello.py on line 4, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details
```

Editar o script Python:

``` bash
vim /tmp/hello.py
```

``` {.python linenos=""}
#!/usr/bin/env python
#_*_ coding: utf-8 _*_

print('Olá!')
```

Executar o script:

``` bash
python /tmp/hello.py
```

``` console
Olá!
```

# Case sensitive

> Python é case sensitive, ou seja, letras maiúsculas e minúsculas são
> interpretadas de formas diferentes.

``` python
foo = 'bar'
Foo = 'foo'
print(foo)
```

``` console
bar
```

``` python
print(Foo)
```

``` console
foo
```

## Não suporta sobrecarga de funções / métodos

Àqueles que vêm de Java deve estranhar dentre outras coisas o fato de Python
não suportar sobrecarga de funções e métodos.  
Quando uma mesma função é escrita duas ou mais vezes, o que prevalece é a
última definição.

``` python
# Definição da função sem parâmetro
def hello_world():
    print('Hello World')

# (Re)Definição da função com um parâmetro
def hello_world(string):
    print(string)

# Tentativa de execução sem parâmetro    
hello_world()
```

``` console
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    hello_world()
TypeError: hello_world() missing 1 required positional argument: 'string'
```

``` python
hello_world('foo')
```

``` console
foo
```

## Orientada a objetos

Em Python tudo é objeto. Ainda fazendo comparação com o mundo Java, em Python
não existem tipos primitivos. 
Até mesmo um número inteiro é uma instância de int e tem seus atributos e
métodos.   
   
``` python
x = 45
x.__hex__()
```

``` console
'0x2d'
```

``` python
x.real
```

``` console
45
```

``` python
x.imag
```

``` console
0
```

A criação de classes em Python é extremamente simples, sendo que uma
classe primária a herança é feita da classe object e cada classe pode
herdar mais de uma. Ou seja, também é aceita herança múltipla.

``` python
class Carro(object):
    marca = ''
    modelo = ''
    ano = 0

c1 = Carro()

c1.marca = 'Porsche'

c1.modelo = 'Carrera'

c1.ano = 1995

print('O {} {} fabricado em {} estava estacionado.'.format(c1.marca, c1.modelo, c1.ano))
```

``` console
O Porsche Carrera fabricado em 1995 estava estacionado.
```

``` python
class Animal(object):
    peso = 0.0

class Humano(Animal):
    quoficiente_inteligencia = 0.0

class Touro(Animal):
    envergadura_chifre = 0.0

class Minotauro(Humano, Animal):
    pass
```

## Tipagem dinâmica

> O interpretador define o tipo de acordo com o valor atribuído à
> variável. A mesma variável pode ter seu tipo mudado de acordo com
> valores a ela atribuídos ao longo do código-fonte e em seu tempo de
> execução.

``` python
foo = 'bar'
type(foo)
```

``` console
str
```

``` python
foo = 123
type(foo)
```

``` console
int
```

``` python
foo = 7.0
type(foo)
```

``` console
float
```

## Tipagem forte

O interpretador verifica se a operação é válida e não faz coerção
automática entre tipos incompatíveis. Caso haja operações de tipos
incompatíveis é preciso fazer a conversão explícita da variável ou
variáveis antes da operação.

``` python
foo = '2'
bar = 5
type(foo)
```

``` console
<class 'str'>
```

``` python
type(bar)
```

``` console
<class 'int'>
```

``` python
foobar = foo + bar
```

``` console
Traceback (most recent call last):
    File "<input>", line 1, in <module>
        foobar = foo + bar
TypeError: can only concatenate str (not "int") to str
```

``` python
foobar = int(foo) + bar
print(foobar)
```

``` console
7
```

``` python
foo = 2.0
type(foo)
```

``` console
<class 'float'>
```

``` python
bar = 5
type(bar)
```

``` console
<class 'int'>
```

``` python
foobar = foo + bar
print(foobar)
```

``` console
7.0
```

## Bytecode

Formato binário multiplataforma resultante da compilação de um código
Python.  

  
Criação de estrutura de diretórios para teste de pacote e bytecode:

``` bash
mkdir -p /tmp/python/PacoteA/PacoteA1
```

Editar o módulo \"Modulo1\" que está dentro do pacote \"PacoteA\":

``` bash
vim /tmp/python/PacoteA/Modulo1.py
```

``` {.python linenos=""}
def funcao():
    print('Hello World!!!')
```

Editar o módulo \"Modulo2\" que está dentro do pacote \"PacoteA\":

``` bash
vim /tmp/python/PacoteA/PacoteA1/Modulo2.py
```

``` {.python linenos=""}
def funcao(numero):
    print(numero ** 3)
```

Edição de script de exemplo:

``` bash
vim /tmp/python/foo.py
```

``` {.python linenos=""}
#!/usr/bin/env python
# _*_ encoding: utf-8 _*_

from PacoteA.Modulo1 import funcao
from PacoteA.PacoteA1 import Modulo2

print('\nAtenção!!!\n')
print('O teste vai começar...\n')

funcao()

Modulo2.funcao(3)
```

Execução do script:

``` bash
python3 /tmp/python/foo.py
```

``` console
Atenção!!!

O teste vai começar...

Hello World!!!
27
```

Quando um módulo é carregado pela primeira vez ou se seu código é mais
novo do que o arquivo binário ele é compilado e então gera ou gera
novamente o arquivo binário .pyc.

Listar o conteúdo de \"PacoteA\":

``` bash
ls /tmp/python/PacoteA/
```

``` console
Modulo1.py  PacoteA1  __pycache__
```

Listar o conteúdo de \_\_pycache\_\_:

``` bash
ls /tmp/python/PacoteA/__pycache__/
```

``` console
Modulo1.cpython-36.pyc
```

Com o comando \"file\" verificar informações de tipo de arquivo:

``` bash
file /tmp/python/PacoteA/__pycache__/Modulo1.cpython-36.pyc
```

``` console
/tmp/python/PacoteA/__pycache__/Modulo1.cpython-36.pyc: python 3.6 byte-compiled
```

# Quebra de linhas

Pode ser usada a barra invertida ou por vírgula.

``` python
varTeste = 3 * 5 + \
(10 + 7)

varLista = [7,14,25,
            81,121]
```

# Blocos

> São delimitados por endentação e a linha anterior ao bloco sempre
> termina com dois pontos.

``` python
#Definição de uma classe
class Carro(object):
    ano = 0
    marca = ''
    estado_farois = False

    #Definição de um método da classe
    def interruptor_farois(self):
        #Bloco if
            if(self.estado_farois):
                print('Apagando faróis')
                self.estado_farois = False
            else:
                print('Acendendo faróis')
                self.estado_farois = True
```

# Comentários

> Inicia-se com o caractere \"#\" em cada linha.

``` python
# um simples comentário

# A seguir uma soma

x = 5 + 2

print(x)  # Imprime o valor de x
```

# Docstrings ou strings de múltiplas linhas

> Feitos dentro de funções e classes, que geram documentação
> automaticamente que pode ser acessado pela função help(). São usados
> três pares de apóstrofos (\') ou três pares de aspas (\"), 3 (três) no
> início e 3 (três) no fim.

``` python
# Com apóstrofos

'''Esta função faz isso de forma
x, y e z além de bla bla bla bla'''

# Com aspas

"""Esta função faz isso de forma
x, y e z além de bla bla bla bla"""
```

Recurso para criar documentação automaticamente:

``` python
def funcao():
    '''Esta função não faz absolutamente nada'''

help(funcao)
```

``` console
Help on function funcao in module __main__:

funcao()
    Esta função não faz absolutamente nada
```

# Operadores

Python suporta operadores dos tipos:

-   Aritiméticos: +, -, *, /, //,*\*, %;
-   Relacionais: \>, \<, \>=, \>=, ==, !=;
-   Atribuição: =, +=, +=, -=, /=, *=, %=,*\*=, //=;
-   Lógicos: and, or, not;
-   Associação: in, not in;
-   Identidade: is, is not;
-   Bitwise: &, \|, \^, \~, \<\<, \>\>.

Operadores serão discutidos em mais detalhes em um capítulo posterior.

# O Comando del

> Este comando tem como objetivo remover a referência de um objeto. Se
> esse objeto não tiver outra referência, o garbage collector atuará
> liberando recursos.

``` python
sogra = 'Edelbarina'
print(sogra)
```

``` console
Edelbarina
```

``` python
del sogra
print(sogra)
```

``` console
Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
NameError: name 'sogra' is not defined
```

``` python
a = ['Z', 1, 5, 'm']
del a[2]
print(a)
```

``` console
['Z', 1, 'm']
```

# print

Antes era somente um comando, a partir da série 3.X será apenas interpretado
como função.

``` python
print('Teste')
```

``` console
Teste
```

# Referência de identificadores

``` python
x = 7
y = x
z = x

id(x)
```

``` console
29786312
```

``` python
id(y)
```

``` console
29786312
```

``` python
id(z)
```

``` console
29786312
```

3 (três) referências ao mesmo objeto

``` python
del x
```

Agora são 2 (duas) referências\...

``` python
print(y)
```

``` console
7
```

``` python
del y
```

Resta apenas 1 (uma) referência\...

``` python
print(z)
```

``` console
7
```

``` python
del z
```

O contador de referências chegou a 0 (zero), ou seja, não há mais
referência para o objeto. Então entra em ação o Garbage Collector para
limpar a memória.
