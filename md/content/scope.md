# Escopo


|   Por escopo entende-se o contexto onde um identificador será
  considerado.
|   Um identificador pode ser uma variável, um comando, uma função uma
  clase ou um objeto.
|   A ordem de busca de um identificador em escopos é a seguinte:

1.  Local ou dentro de função;
2.  Função externa;
3.  Global ou de módulo;
4.  \_\_builtins\_\_

# Escopo Local ou Dentro de Função

> É o escopo que tem a maior prioridade.

Declaração de uma variável com seu valor:

``` python
foo = 7
```

Exibindo na tela o valor da variável:

``` python
print(foo)
```

``` console
7
```

## Função locals

|   A função locals() retorna um dicionário com os identificadores
  locais e seus respectivos valores.
| Então é pedido o valor dada a chave que é o nome da variável local.

Usando locals para retornar o valor de uma variável:

``` python
locals()['foo']
```

``` console
7
```

## Escopo Interno de uma Função

|   Diz respeito ao espaço delimitado de alcance, dentro de uma função.

Declaração de uma variável externamente ao escopo da função:

``` python
foo = 7
```

Definição de uma função:

``` python
def funcao():
    foo = 9
    print(id(foo))
    print(foo)
```

|   Nota-se que dentro da função também há uma variável chamada \"foo\".
  Essa função imprime o ID desse identificador e depois imprime seu
  valor.

Exibindo o ID de foo:

``` python
print(id(foo))
```

``` console
162857064
```

Exibindo o valor de foo:

``` python
print(foo)
```

``` console
7
```

Acionando a função:

``` python
funcao()
```

``` console
162857040
9
```

|   Nota-se também que bem como o ID e o valor retornados pela função,
  da variável interna foo são diferentes da variável externa de mesmo
  nome.

# Escopo de Função Externa

|   Ao se criar uma função dentro de outra, a função mais interna pode
  utilizar um identificador que esteja no nível mais acima.

Definição de uma função com uma função interna:

``` python
def funcao_principal():
    x = 1
    def funcao_secundaria():
        print(x)
    funcao_secundaria()
```

|   A função principal tem uma variável x, cujo valor é impresso em tela
  pela função secundária.
|   A função principal invoca a função secundária.

Chamando a função:

``` python
funcao_principal()
```

``` console
1
```

Uma nova definição da função:

``` python
def funcao_principal():
    x = 1
    def funcao_secundaria():
        x = 2
        print(x)
    funcao_secundaria()
```

|   Diferente do exemplo anterior, a função secundária declarou sua
  própria variável \"x\".

Testando a função:

``` python
funcao_principal()
```

``` console
2
```

|   Nota-se que o valor considerado foi o de \"x\", que é o
  identificador mais interno.

# Escopo Global ou Escopo do Módulo

|   É também conhecido como escopo de módulo devido ao fato de estar na
  endentação do mesmo.

Criação de variável:

``` python
foo = 'bar'
```

Criação de função:

``` python
def funcao():
    foo = 'eggs'
    print(foo)
```

|   A função criada tem uma variável com o mesmo nome que uma variável
  global, a ela dá um valor e imprime esse valor em tela.
|   Será que isso altera o valor da variável global?

Execução da função:

``` python
funcao()
```

``` console
eggs
```

|   Nota-se que o valor impresso é igual ao da variável \"foo\" dentro
  da função.
|   Pra saber se a variável global foi alterada, vamos testar com a
  função print.

Imprimindo o valor da variável global:

``` python
print(foo)
```

``` console
bar
```

|   Pode-se concluir que a função criada não interferiu na variável
  global.
|   Para alterar uma variável global em um contexto local precisamos
  utilizar o comando global.

Criação de função que altera a variável global:

``` python
def funcao():
    global foo
    foo = 'eggs'
    print(foo)
```

Executar função:

``` python
funcao()
```

``` console
eggs
```

|   OK, a função imprimiu o valor local da função.
|   Mas será que a variável global também foi alterada?

Imprimir o valor da variável global:

``` python
print(foo)
```

``` console
eggs
```

|   Agora a função pôde alterar a variável global. Isso se deve ao fato
  do comando global ter sido empregado.
|   A variável global a ser alterada deve ser declarada como global
  antes de sua atribuição.

# Escopo \_\_builtins\_\_

|   O escopo \_\_builtins\_\_ abrange identificadores que já estão
  definidos antes mesmo do código a ser escrito.
|   São funções, comandos e variáveis internas de Python.

\"str\" é está em \_\_builtins\_\_?:

``` python
'str' in dir(__builtins__)
```

``` console
True
```

|   Resposta afirmativa (True), ou seja, \"str\" faz parte desse escopo.
|   E se sobescrevermos esse item localmente?

Criando uma variável cujo identificador pertence ao escopo
\_\_builtins\_\_:

``` python
str = 1
```

Qual é o tipo?:

``` python
type(str)
```

``` console
int
```

|   \"str\" que inicialmente era um identificador para o tipo de strings
  em Python, aqui agora virou uma variável de inteiro.
|   Mas e o tipo \"str\" deixou de existir?

Qual tipo?

``` python
type(__builtins__.str)
```

``` console
type
```

|   É do tipo \"tipo\"

Valor de str?:

``` python
str
```

``` console
1
```

Chamar a str built-in para converter a str redefinida:

``` python
__builtins__.str(str)
```

``` console
'1'
```

Apagando a variável:

``` python
del str
```

Função built-in str:

``` python
str(7)
```

``` console
'7'
```

|   Observe que a função não foi removida, apenas a variável criada por
  redefinição.

Verificar todos identificadores built-ins:

``` python
dir(__builtins__)
```

|   . . .

# Funções globals(), locals() e vars() e Comando global

|   Cada uma das funções retornam dicionários de variáveis e seus
  respectivos valores.

-   globals(): Retorna variáveis globais (escopo do módulo);
-   locals(): Retorna variáveis locais (escopo local);
-   vars(obj): sem argumentos é equivalente a locals(), com um
    argumento, equivalente a objeto.\_\_dict\_\_.

Variável em um escopo global:

``` python
foo = 'escopo global'
```

Função de teste:

``` python
def f():
    foo = 'escopo local'
    bar = 'uma variável qualquer...'
    print(globals()['foo'])  # Valor do identificador global
    print(locals()['foo'])  # Valor do identificador local
```

Chamada da função:

``` python
f()
```

``` console
escopo global
escopo local
```

Criação de uma classe de teste:

``` python
class Spam(object):
    foo = ''
    bar = ''
```

\"foo\" e \"bar\" ambos identificadores estão contidos em
\"vars(Spam)\"?:

``` python
set(('foo', 'bar')).issubset(vars(Spam))
```

``` console
True
```

Função de teste:

``` python
def f():
    global x
    x = 7
```

Verificando o tipo:

``` python
type(x)
```

``` console
NameError: name 'x' is not defined
```

|   A variável \"x\" não existe ainda.

Executando a função:

``` python
f()
```

Verificando o tipo:

``` python
type(x)
```

``` console
int
```

Exibir o valor da variável:

``` python
print(x)
```

``` console
7
```
