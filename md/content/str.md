# Strings

Em Ciências da Computação chamamos de string um texto, também conhecido como
cadeia de caracteres.  
Strings representam textos, frases ou palavras.  
É um recurso muito caro em termos de recursos computacionais (processamento e
memória) e que portanto deve ser utilizado com cuidado, pois escalabilidade é
algo que deve ser sempre um fator a ser levado em conta.

[https://docs.python.org/3/library/string.html](https://docs.python.org/3/library/string.html)

## Strings em Python

Pode-se usar tanto entre aspas como entre apóstrofos.

``` python
# Declaração de uma variável string utilizando apóstrofos
s1 = 'string'
```

``` python
# Declaração de uma variável string utilizando aspas
s2 = "string"
```

``` python
# Declaração de uma variável string utilizando a função str
s = str('foo')
```

## Apóstrofos ou aspas? Qual devo utilizar?

Se não tivessem essas duas opções, se fosse apenas aspas como em outras
linguagens, em uma string que precisa ter aspas, seria preciso escapar com a
contrabarra desta maneira: `\"`. O que também funcionaria.  
Fazer uso de contrabarra para escapar por muitas vezes pode ser um tanto
confuso e tornar o código menos legível.  
Com a facilidade de se poder utilizar ambos torna o *escape* desnecessário
para a maioria dos casos em que aspas ou apóstrofos façam parte de uma
*string*.  
   
Dois exemplos com `print` de *strings* com aspas e apóstrofos dentro:  

``` python
print('Uma string que contém "aspas" em si')
```

``` console
Uma string que contém "aspas" em si
```

``` python
print("Uma string que contém 'apóstrofos' em si")
```

``` console
Uma string que contém 'apóstrofos' em si
```

``` python
# Um caso clássico é em strings com um comando SQL
sql = "SELECT * FROM tb_musica WHERE artista = 'Mozart';"

# Exibindo o conteúdo da variável:
print(sql)
```

``` console
SELECT * FROM tb_musica WHERE artista = 'Mozart';
```

## Strings de múltiplas linhas

É possível se fazer uma string de múltiplas linhas quando colocamos como
fechamento e abertura três apóstrofos ou aspas.  

``` python
# String de múltiplas linhas com triplos apóstrofos:
s1 = '''
Um 
exemplo
de string
de várias
linhas
'''

# String de múltiplas linhas com triplas aspas:
s2 = """
Um
exemplo
de string
de várias
linhas
"""

# String de múltiplas linhas entre parênteses:
s3 = ('Um exemplo de string feito para não ultrapassar os setenta \n'
      'e nove caracteres da PEP8 (Python Enhancement Proposal), \n'
      'Proposta de aprimoramento do Python, que visa boas práticas'
      ' de programação.')

# Exibindo s3:
print(s3)
```

``` console
Um exemplo de string feito para não ultrapassar os setenta 
e nove caracteres da PEP8 (Python Enhancement Proposal), 
Proposta de aprimoramento do Python, que visa boas práticas de programação.
```

# Caracteres especiais

```
| Escape             | Descrição                                             | Exemplo      | Saída         |
|--------------------|-------------------------------------------------------|--------------|---------------|
| \\                 | Imprime uma contrabarra                               | '\\'         | \             |
| \'                 | Imprime um apóstrofo                                  | '\''         | '             |
| \"                 | Imprime uma aspa                                      | "\""         | "             |
| \a                 | ASCII bell (beep)                                     | '\a'         |               |
| \b                 | ASCII backspace (BS) remove o caractere anterior      | 'Casas\b'    | Casa          |
| \f                 | ASCII formfeed (FF)                                   | 'foo\fbar'   | foo      bar  |
| \n                 | ASCII linefeed (LF)                                   | 'foo\nbar'   | foo           |
|                    |                                                       |              | bar           |
| \r                 | ASCII carriage return (CR)                            | 'foo\rbar'   | bar           |
| \t                 | ASCII horizontal tab (TAB)                            | 'foo\tbar'   | foo    bar    |
| \v                 | ASCII vertical tab (VT)                               | 'foo\vbar'   | foo           |
|                    |                                                       |              |     bar       |
| \N                 | Imprime um caractere da base de dados Unicode         | '\N{DAGGER}' | †             |
| \uxxxx  ou  \Uxxxx | Imprime 16-bit valor hexadecimal de caractere Unicode | '\u041b'     | Л             |
| \                  | Imprime 32-bit valor hexadecimal de caractere Unicode | '\U000001a9' | Ʃ             |
| \ooo               | Imprime o character baseado em seu valor octal        | '\077'       | ?             |
| \xhh               | Imprime o character baseado em seu valor hexadecimal  | '1\xaa'      | 1ª            |
```


## Formatação

Há casos que é necessário fazer formatação de strings colocando uma string
como um template.  
Inicialmente tinha-se a interpolação que utiliza o sinal de porcentagem (%),
posteriormente foi adicionado o método format.

``` python
# Interpolação
'%s %s' % ('foo', 'bar')
```

ou

``` python
# Método format
'{} {}'.format('foo', 'bar')    
```

``` console
'foo bar'
```

``` python
# Valores numéricos decimais (interpolação)
'%d %d' % (70, 90)
```

ou

``` python
# Valores numéricos decimais (método format)
'{} {}'.format(70, 90)    
```

``` console
'70 90'    
```

``` python
# Interpolação pegando o valor de um dicionário
print('%(variavel)s' % {'variavel': 'valor'})
```

``` console
valor
```

``` python
# Variável que vai receber os valores formatados
foo = '''Produto: %(prod)s
      Preco: R$ %(preco).2f
      Cód: %(cod)05d
      '''

# Declaração de um dicionário que conterá as chaves e valores desejados
d = {'prod': 'Pente', 'preco': 3.5, 'cod': 157}

# Exibindo o resultado via interpolação
print(foo % d)
```

``` console
Produto: Pente
Preco: R$ 3.50
Cód: 00157
```

``` python
# Exibindo o resultado via método format
print(foo.format(**d))
```

``` console
Produto: Pente
Preco: R$ 3.50
Cód: 00157
```

``` python
# String com índice posicional
'O {1} {2} quando é {0}.'.format('compartilhado', 'conhecimento', 'aumenta')
```

``` console
'O Conhecimento aumenta quando se compartilhado'
```

## Métodos string e de representação

Em objetos temos os *dunders* str (`__str__`) e repr (`__repr__`) que podem
ser usados em uma string.

``` python
# Criação de uma classe de exemplo
class Foo(object):

    def __str__(self):
        return 'STRING'

    def __repr__(self):
        return 'REPRESENTAÇÃO'


# Valores dos métodos __str__ e __repr__ da classe Foo
'%s %r' % (Foo(), Foo())  # interpolação
'{0!s} {0!r}'.format(Foo())  # format
```

``` console
'STRING REPRESENTAÇÃO'
```

``` python
# Método de representação e em caracteres ASCII
'%r %a' % (Foo(), Foo())  # interpolação
'{0!r} {0!a}'.format(Foo())  # format
```

``` console
'REPRESENTAÇÃO REPRESENTA\\xc7\\xc3O'
```

## Preenchimento (padding) e alinhamento de Strings

``` python
# Alinhamento à direita dentro de 7 colunas
'%7s' % 'foo'  # interpolação
'{:>7}'.format('foo')  # format
```

``` console
'    foo'
```

``` python
# Alinhamento à esquerda dentro de 7 colunas
'%-7s' % 'foo'  # interpolação
'{:7}'.format('foo')  # format
'{:<7}'.format('foo')
```

``` console
'foo    '
```

``` python
# Alinhamento centralizado dentro de 7 colunas
'{:^7}'.format('foo')
```

``` console
'  foo  '
```

``` python
# Alinhamento à esquerda dentro de 7 colunas preenchendo com o caractere "_"
'{:_<7}'.format('foo')
```

``` console
'foo____'
```

``` python
# Alinhamento à direita dentro de 7 colunas preenchendo com o caractere "_"
'{:_>7}'.format('foo')
```

``` console
'____foo'
```

``` python
# Alinhamento centralizado dentro de 7 colunas preenchendo com o caractere "_"
'{:^7}'.format('foo')
```

``` console
'__foo__'
```

``` python
# Número decimal
'{:.3f}'.format(93.85741)
```

``` console
'93.857'
```

``` python
# 
'{:.3f}'.format(70000)
```

``` console
'70000.000'
```

## Representações de inteiros

``` python
# b) Formato binário; número de saída na base 2
format(10, '#05b')
```

``` console
'0b1010'
```

``` python
# c) Caractere; converte o inteiro para o caractere unicode correspondente
format(93, 'c')
```

``` console
']'
```

``` python
# d) Inteiro Decimal; saída numérica na base 10 (decimal)
format(0b111, '#05d')
```

``` console
'00007'
```

``` python
# o) Formato Octal; saída numérica na base 8 (octal)
format(9, '#05o')
```

``` console
'0o011'
```

``` python
# x ou X) Formato Hexadecimal; saída numérica na base 16 (hexadecimal),
# a saída é conforme o "x" maiúsculo ou minúsculo
format(200, '#05x')
```

``` console
'0x0c8'
```

``` python
format(200, '#05X')
```

``` console
'0X0C8'
```

``` python
# n) Numérico; o mesmo que "d", exceto que ele usa as configurações
# de idioma (locale) para exibir caracteres
format(31259.74, 'n')
```

``` console
'31259.7'
```

``` python
format(31259.75, 'n')
```

``` console
'31259.8'
```

``` python
# None) Nulo; o mesmo que "d"
format(0b111)
```

``` console
'7'
```

``` python
# Para representação exponencial pode-se utilizar tanto "e" ou "E",
# cuja precisão padrão é 6
format(1000, '.3e')
```

``` console
'1.000e+03'
```

``` python
format(1000, '.3E')
```

``` console
'1.000E+03'
```

``` python
# "f" ou "F" faz exibição de número com ponto flutuante podendo determinar
# a precisão, cujo padrão é 6.
```

``` python
# format(1000, '10.2f')
```

``` console
'   1000.00'
```

``` python
format(1000, 'F')
```

``` console
'1000.000000'
```

``` python
# "g" ou "G"; formato geral. Para uma dada precisão, sendo essa precisão
# maior ou igual a ' (um), arredonda o número para p (precisão) de dígitos significantes
format(1000, '10.2G')
```

``` console
'     1E+03'
```

``` python
format(1000, '10.3G')
```

``` console
'     1e+03'
```

``` python
format(100000, 'g')
```

``` console
'100000'
```

``` python
format(1000000, 'g')
```

``` console
'1e+06'
```

``` python
format(999.5, '10.4G')
```

``` console
'     999.5'
```

``` python
# format(999.5, '10.3G')
```

``` console
'     1E+03'
```

## Tipos de strings em Python

Em Python temos algumas variações de strings, cada qual é designada por um
prefixo, que é uma letra que representa o tipo de string e por omissão é
unicode.  
Cada tipo de string tem um prefixo, que são `b` bytes, `f` format, `r` raw e
`u` unicode.

``` python
# Como unicode é padrão, podemos omitir o prefixo
print(u'Foo' == 'Foo')
```

``` console
True
```

### Bytes (b)

Strings de bytes utilizam o prefixo `b` e quando contém caracteres especiais,
esses são representados pelo código hexadecimal da codificação utilizada.  

``` python
# Criação de 3 (três) strings comuns
s1 = 'Sem caracteres especiais'
s2 = 'Macarrão'
s3 = 'Ação'

# A partir das três strings criadas anteriormente, criar outras três strings,
# mas strings de bytes
sb1 = s1.encode('utf-8')
sb2 = s2.encode('utf-8')
sb3 = s3.encode('utf-8')
```

O método encode, utilizando a codificação UTF-8 faz a codificação de
cada caractere para bytes.

``` python
# Exibir o conteúdo das strings de bytes
print(sb1)
```

``` console
b'Sem caracteres especiais'
```

``` python
print(sb2)
```

``` console
b'Macarr\xc3\xa3o'
```

``` python
print(sb3)
```

``` console
b'A\xc3\xa7\xc3\xa3o'
```

As strings que tinham caracteres especiais ficaram um tanto
\"estranhas\"\...

| `\xc3\xa3 -> ã`
| `\xc3\xa7 -> ç`

``` python
# Conversão de bytes
print(b'\xc3\xa3'.decode('utf-8'))
```

``` console
ã
```

``` python
print(b'\xc3\xa7'.decode('utf-8'))
```

``` console
ç
```

``` python
# A letra grega sigma é considerada como um caractere especial
print('∑'.encode('utf-8'))
```

``` console
b'\xe2\x88\x91'
```

``` python
# Caminho reverso
print(b'\xe2\x88\x91'.decode('utf-8'))
```

``` console
∑
```

``` python
# A partir das strings de bytes obter o texto
print(sb1.decode('utf-8'))
```

``` console
Sem caracteres especiais
```

``` python
# Decodificação UTF-8:
print(sb2.decode('utf-8'))
```

``` console
Macarrão
```

``` python
print(sb3.decode('utf-8'))
```

``` console
Ação
```

``` python
# Pode-se também criar um objeto bytes a partir da classe
b = bytes('∑'.encode('utf-8'))
```

``` python
# Verificando o tipo
print(type(b))
```

``` console
<class 'bytes'>
```

Uma byte string tem um tipo específico, bytes.

``` python
# Exibindo a byte string
print(b)
```

``` console
b'\xe2\x88\x91'
```

``` python
# Decodificando para unicode
print(b.decode('utf-8'))
```

``` console
∑
```

``` python
# Verificando o tipo quando o objeto é decodificado
type(b.decode('utf-8'))
```

``` console
str
```

Ao ser decodificado passa a ser uma string.

### Format strings

> Ou também conhecidas como \"f strings\" foi um recurso adicionado à
> versão 3.6 de Python.

``` python
# Definição de variáveis
marca = 'Fiat'
modelo = '147'
ano = 1985
cor = 'azul'
```

``` python
# Exibir mensagem com uma f string
print(f'Comprei um {marca} {modelo} {cor} ano {ano}')
```

``` console
Comprei um Fiat 147 azul ano 1985
```

``` python
# Uma f string também permite que se use expressões
print(f'{5 + 2}')
```

``` console
7
```

``` python
# Métodos e funções também são permitidos
print(f'{cor.upper()}')
```

``` console
AZUL
```

``` python
# Criação de uma classe de exemplo que recebe quatro parâmetros
class Carro(object):
    # Método de inicialização (construtor)
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    # Método string
    def __str__(self):
        return f'{marca} {modelo} / {cor} / {ano}'

    # Método de representação
    def __repr__(self):
        return f'{marca} {modelo} | {cor} | {ano}'
```

``` python
# Criação de um objeto Carro
c = Carro(marca, modelo, ano, cor)
```

``` python
# Print do método __str__ do objeto:
print(f'{c}')
```

``` console
Fiat 147 / azul / 1985
```

``` python
# Print do método __repr__ do objeto
print(f'{c!r}')
```

``` console
Fiat 147 | azul | 1985
```

``` python
# f string de múltiplas linhas
msg = f'Marca: {marca}\n'\
    f'Modelo: {modelo}\n'\
    f'Ano: {ano}\n'\
    f'Cor: {cor}'

# Exibir a mensagem
print(msg)
```

``` console
Marca: Fiat
Modelo: 147
Ano: 1985
Cor: azul
```

``` python
# f String entre parênteses
msg = (f'Marca: {marca} - '
     f'Modelo: {modelo} - '
     f'Ano: {ano} - '
     f'Cor: {cor}')

# Exibir a mensagem
print(msg)
```

``` console
Marca: Fiat - Modelo: 147 - Ano: 1985 - Cor: azul
```

Raw Strings (r) \~\~\~\~\~\~\~\~\~\~\~\~\~\~

> É o tipo de string cujo conteúdo é interpretado literalmente.

``` python
# Exemplo de print com raw string
print(r'foo\tbar')
```

``` console
foo\tbar
```

É de se notar que a string não teve interpretação do caractere especial
de tab (t), ou seja, não houve qualquer interpretação.

### Unicode strings (u)

> É o padrão para uma string em Python, não há a necessidade de
> adicionar o sufixo \"u\" antes do apóstrofo ou aspas.

``` python
# Comparação de strings
u'Foo' == 'Foo'
```

``` console
True
```

Das duas strings, somente a primeira tem o sufixo \"u\".

## Operações de Strings

### Concatenação

``` python
# 
print("Curso" + " de " + "Python")
```

``` console
Curso de Python
```

``` python
#
spam = "Curso".__add__(" de ".__add__("Python"))

# 
print(spam)
```

``` console
Curso de Python
```

### Multiplicação

``` python
# 
print('<' + 'Python' * 3 + '>')
```

``` console
<PythonPythonPython>
```

``` python
#
print('<' + 'Python'.__mul__(3) + '>')
```

``` console
'<PythonPythonPython>'
```

### Split

> Quebra a string em palavras formando uma lista.

``` python
# 
print('Curso de Python'.split())
```

``` console
['Curso', 'de', 'Python']
```

``` python
# 
print('Curso de Python'.split('de'))
```

``` console
['Curso ', ' Python']
```

### Slice

|   Corte de string - `'string'[inicio:fim - 1:incremento]`. É
  importante salientar que no intervalo início:fim começam por zero, o
  ínício é fechado e o fim é aberto \[início:fim). Por padrão o
  incremento é 1.

``` python
# Primeira posição (começa com zero) da string:
print("Curso de Python”[0])
```

``` console
'C'
```

``` python
# Da segunda à quarta posição da string:
print("Curso de Python"[1:5])
```

``` console
'urso'
```

``` python
# Da segunda à quarta posição com incremento 2:
print("Curso de Python"[1:5:2])
```

``` console
'us'
```

``` python
# Da posição 9 em diante:
print("Curso de Python"[9:])
```

``` console
'Python'
```

``` python
# Até a posição 4:
print("Curso de Python"[:5])
```

``` console
'Curso'
```

``` python
# Padrão...:
print("Curso de Python"[::])
```

``` console
'Curso de Python'
```

``` python
# String reversa, incremento negativo:
print("Curso de Python"[::-1])
```

``` console
'nohtyP ed osruC'
```

## Docstrings

São strings que vêm logo após a definição de uma função, de um método ou de
uma classe.  
É muito útil para fins de documentação.  
Para visualizar o conteúdo dessa string utiliza-se o atributo mágico `__doc__`
ou a função `help()`.

``` python
# Criação de uma função
def foo():
    'Uma simples função'
```

``` python
# Exibe a docstring da função
print(foo.__doc__)
```

``` console
Uma simples função
```

``` python
# Criação de função
def bar():
    '''
    Mais outra
    função
    que não faz
    nada
    '''
```

``` python
# Exibe a docstring da função
print(bar.__doc__)
```

``` console
Mais outra
função
que não faz 
nada
```

``` python
# Criação de uma classe
class Foo(object):
    '''
    Uma classe
    de teste
    '''
```

``` python
# Exibe a docstring da classe
print(Foo.__doc__)
```

``` console
Uma classe
de teste
```

``` python
# Help da classe:
help(Foo)
```

``` console
Help on class Foo in module __main__:

class Foo(__builtin__.object)

|  Uma classe
|  de teste
|  
|  Data descriptors defined here:
|  
|  __dict__
|      dictionary for instance variables (if defined)
|  
|  __weakref__
|      list of weak references to the object (if defined)
```

## Imutabilidade

> Strings em Python são imutáveis.

``` python
# Criação de uma string
foo = 'bar'

# Primeiro elemento da string
foo[0]
```

``` console
'b'
```

``` python
# Tentativa de redefinição do primeiro elemento da string
foo[0] = 'B'
```

``` console
TypeError: 'str' object does not support item assignment
```

``` python
# Id da string
id(foo)
```

``` console
139876439773904
```

``` python
# Criação de uma string com o mesmo nome da anterior
# utilizando concatenação e slice
foo = 'B' + foo[1:]
```

``` python
# Verificando o Id da variável
id(foo)
```

``` console
140159122071800
```

Nota-se que o Id é diferente, pois agora é outro objeto.

``` python
# Exibindo o valor da variável
print(foo)
```

``` console
Bar
```

``` python
# Criação de uma nova string
s = 'Black'

# Id da string
 id(s)
```

``` console
140159159537600
```

``` python
# Criando uma nova string com o mesmo nome 
# da anterior via concatenação
```

``` python
# 
s += ' Sabbath'
```

``` python
# Id da nova variável
id(s)
```

``` console
140159122296368
```

Novamente nota-se que o Id é diferente, pois é na verdade um novo
objeto.

``` python
# Exibindo a string
print(s)
```

``` console
Black Sabbath
```

## Concatenação de Strings em Loops

### Método 1 - ineficaz

``` python
# Criação de uma string vazia
s = ''

# Loop de concatenação
for i in range(50):
    s += str(i)

# String pronta
print(s)
```

``` console
012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849
```

Para cada iteração a referência do objeto antigo é retirada e sendo criado um
novo a partir do resultado da concatenação do valor antigo com o valor de do
atual e o garbage collector é acionado. Isso faz muita alocação de memória, o
que torna o desempenho horrível para coisas maiores.

### Método 2 - eficaz

``` python
# Criação de uma lista vazia
s = []

# Loop de concatenação
for i in range(50):
    s.append(str(i))

# Fazendo a junção de uma string vazia com a lista criada 
# com seus elementos via método append
print(''.join(s))
```

``` console
012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849
```

``` python
# Criando uma string via método join da lista de mesmo nome
s = ''.join(s)

# Exibindo o valor da variável
print(s)
```

``` console
012345678910111213141516171819202122232425262728293031323334353637383940414243444546474849
```

Foi criada uma lista de strings no loop em que a cada iteração é
utilizado o método append da lista para adicionar o item atual. No final
é utilizado o método de string join que utiliza como separador uma
string vazia (\'\') juntando em uma string (o novo s) todos os valores
da lista. A estrutura de dados de uma lista Python é mais eficiente para
crescer, pois o método append apenas adiciona um novo elemento, de forma
rápida e eficiente. O método join, que é escrito em C, que faz a junção
de todos elementos concatenando em um único passo.Muito melhor do que o
método anterior em que um novo objeto é criado a cada iteração.

## Métodos de Strings

-   join; junta elementos de uma lista ou tupla utlizando uma string.

``` python
# Criação de uma lista
foo = list('Python')

# Exibe a lista
print(foo)
```

``` console
['P', 'y', 't', 'h', 'o', 'n']
```

``` python
# Criação de uma nova variável juntando os elementos
# da lista com uma string vazia
bar = ''.join(foo)

# Exibindo a nova string
print(bar)
```

``` console
Python
```

``` python
# Criando uma tupla
foo = tuple('Python')

# Exibindo os elementos da tupla
print(foo)
```

``` console
('P', 'y', 't', 'h', 'o', 'n')
```

``` python
# Criação de uma nova variável juntando os elementos
# da tupla com uma string vazia
bar = ''.join(foo)

# Exibindo o valor da variável
print(bar)
```

``` console
Python
```

-   find & index - Qual é a diferença entre eles?

``` python
# Dada a seguinte string
foo = 'Python FreeBSD PostgreSQL'
```

Temos seus caracteres e suas respectivas posições: :

    P|y|t|h|o|n| |F|r|e|e |B |S |D |  |P |o |s |t |g |r |e |S |Q |L
    0|1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|23|24

``` python
# A partir de qual posição aparece a string?
foo.index('FreeBSD')
foo.find('FreeBSD')
```

``` console
7
```

No exemplo dado o texto existe na string. E se não existisse?

``` python
# Buscando um texto que não existe dentro da string
foo.index('Linux')
```

``` console
ValueError: substring not found
```

``` python
#
foo.find('Linux')
```

``` console
-1
```

Nota-se que que index lança uma exceção, enquanto find retorna -1 ao não
encontrar o que foi pedido. O -1 não deve ser confundido como último
elemento.

-   count

``` python
# Na frase em latim abaixo, quantas vezes aparece a letra "u"?
'sic mundus creatus est'.count('u')
```

``` console
3
```

``` python
# Quantas vezes aparece a sequência de caracteres "foo"?
'XXXfooXXXfooXXXbar'.count('foo')
```

``` console
2
```
