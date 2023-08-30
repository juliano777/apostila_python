# Expressões vs comandos (statements)

> Expressão: é algo que pode ser reduzido para um valor.
>
> Statement: sinônimo de comando.

# exec

> É uma função que executa um comando (statement) passado como string.

bla bla bla:

``` python
exec('print(5)')  # prints 5.
```

``` comando
5
```

``` python
exec('print(5)\nprint(6)')  # prints 5{newline}6.
```

``` console
5
6
```

sdsdsdsdsd:

``` python
exec('if True: print(6)')  # prints 6.
```

``` console
6
```

``` python
exec('5')  # does nothing and returns nothing.
exec('x = 7')  # does nothing and returns nothing.
```

# eval

> É uma função que retorna o resultado de uma expressão.

bla bla bla:

``` python
x = eval('5')  # x <- 5
x = eval('%d + 6' % x)  # x <- 11
x = eval('abs(%d)' % -100)  # x <- 100
x = eval('x = 5')  # INVÁLIDO; atribuição não é uma expressão
```

``` console
SyntaxError: invalid syntax
```

wewewewe:

``` python
x = eval('if 1: x = 4')  # INVÁLIDO; if é um statement e não uma expressão
```

``` console
SyntaxError: invalid syntax
```

bla bla bla:

``` python
execfile(file)
```

bla bla bla:

``` bash
cat << EOF > /tmp/foo.py
print('hello, world!')
EOF
```

bla bla bla:

``` bash
python /tmp/foo.py
```

``` console
hello, world!
```

bla bla bla:

``` bash
execfile('/tmp/foo.py')
```

``` console
hello, world!
```

# compile

compile is a lower level version of exec and eval. It does not execute
or evaluate your statements or expressions, but returns a code object
that can do it. The modes are as follows:

> compile(string, \'\', \'eval\') returns the code object that would
> have been executed had you done eval(string). Note that you cannot use
> statements in this mode; only a (single) expression is valid.
> compile(string, \'\', \'exec\') returns the code object that would
> have been executed had you done exec(string). You can use any number
> of statements here. compile(string, \'\', \'single\') is like the exec
> mode, but it will ignore everything except for the first statement.
> Note that an if/else statement with its results is considered a single
> statement.
