# Sequências

Com sequências podemos fazer iteração, indexação, fatiamento (*slice)* e
operações de *list comprehension*.  
Uma sequência pode ser mutável (listas) ou imutáveis (*strings* ou tuplas).  
Uma sequência mutável é interessante pela sua flexibilidade, porém consome mais
recursos.  

## Operações com Sequências

### Índices

Toda sequência, seguindo a mesma idéia de vetores de outras linguagens, como
C, por exemplo, começa com o índice 0 (zero).  
Para se obter um índice, fazemos da seguinte forma:  
  
`sequencia[indice]`

Segundo elemento da string:

``` python
'Python'[1]
```

``` console
'y'
```

Primeiro elemento da lista:

``` python
['foo', 'bar', 2.7, 80,  2 + 7j][0]
```

``` console
'foo'
```

Quarto elemento da tupla:

``` python
('Python', 'C', 'C++', 2.7, 3.7)[3]
```

``` console
2.7
```

### Iterações

Sequências nos permite também fazer iteração sobre cada elemento.

Definição de uma tupla:

``` python
regiao_sudeste = ('SP', 'MG', 'ES', 'RJ')
```

Loop sobre a tupla e impressão em tela de cada elemento:

``` python
for i in regiao_sudeste:
    print(i)
```

``` console
SP
MG
ES
RJ
```

Loop sobre a string e impressão em tela de cada caractere:

``` python
for i in 'Python':
    print(i)
```

``` console
P
y
t
h
o
n
```

Loop sobre um range de 0 (zero) a 20 (vinte) com a condição de exibir
somente 0 (zero) e divisíveis por 5 (cinco):

``` python
for i in range(21):
    if (i % 5 == 0):
        print(i)
```

``` console
0
5
10
15
20
```

### Fatiamento / Slicing

> É o corte de uma sequência.
>
> **[inicio:fim - 1:incremento]**

Fatiamento sem qualquer determinação:

``` python
'Python Language'[::]
```

``` console
'Python Language'
```

Não foram determinados início, fim e incremento.

Fatiamento determinando apenas o início, que é o último elemento:

``` python
'Python Language'[-1::]
```

``` console
'e'
```

Pelo sinal de subtração, os três últimos caracteres da string:

``` python
'Python Language'[-3::]
```

``` console
'age'
```

Determinando apenas o incremento de 4 (quatro) em 4:

``` python
(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)[::4]
```

``` console
(0, 4, 8)
```

Incremento negativo faz com que a string seja colocada em ordem reversa:

``` python
'Python Language'[::-1]
```

``` console
'egaugnaL nohtyP'
```

A partir do primeiro caractere:

``` python
'Python Language'[0:]
```

``` console
'Python Language'
```

Do primeiro ao primeiro caractere:

``` python
'Python Language'[0:1]
```

``` console
'P'
```

Do primeiro ao sexto caractere:

``` python
Python Language'[0:6]
```

``` console
'Python'
```

Do oitavo caractere em diante:

``` python
'Python Language'[7:]
```

``` console
'Language'
```

Criação de uma tupla de exemplo:

``` python
linux_distros = (
                 'Debian',
                 'RedHat',
                 'Slackware',
                 'Ubuntu',
                 'CentOS',
                 'SuSE',
                )
```

Do primeiro ao terceiro elemento:

``` python
linux_distros[0:3]
```

``` console
('Debian', 'RedHat', 'Slackware')
```
