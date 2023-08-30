# Closures

Funções são objetos também. Closures são funções que constroem funções,
retorna outra função. Sua estrutura é uma função dentro de outra. A
função interna é também conhecida como função auxiliadora (helper).

Criação de uma closure:

``` python
def funcao_principal(x):
    def funcao_auxiliadora(y):
        return x ** y
    return funcao_auxiliadora
```

Criação de uma variável foo e passando o valor x para a função
principal:

``` python
foo = funcao_principal(2)
```

\"foo\" é uma nova função cujo o \"x\" de \"função_principal\" é 2.

Qual é o nome da função?:

``` python
print(foo.__name__)
```

``` console
funcao_auxiliadora
```

Tipo de \"foo\":

``` python
type(foo)
```

``` console
function
```

Representação de \"foo\":

``` python
repr(foo)
```

``` console
'<function funcao_principal.<locals>.funcao_auxiliadora at 0x7f9845369950>'
```

Imprimindo o valor resultante ao passar agora o valor y:

``` python
print(foo(6))
```

``` console
64
```

A operação realizada foi 2 elevado a 6 (x \*\* y).

Podemos também chamar a função principal passando o parâmetro da função
auxiliar:

``` python
funcao_principal(5)(2)
```

``` console
25
```

# Closures com Lambda

Criação de uma closure com lambda:

``` python
def funcao_principal(x):
    return lambda y: x ** y
```

O \"x\" será 3:

``` python
bar = funcao_principal(3)
```

Exibindo o nome do objeto:

``` python
print(bar.__name__)
```

``` console
<lambda>
```

Tipo:

``` python
type(bar)
```

``` console
function
```

Representação:

``` python
repr(bar)
```

``` console
'<function funcao_principal.<locals>.<lambda> at 0x7f9844527730>'
```

3 elevado a 2:

``` python
print(bar(2))
```

``` console
9
```

Passando o parâmetro da função principal e de lambda:

``` python
funcao_principal(2)(5)
```

``` console
32
```
