# Tupla

|   Tupla têm sua estrutura muito similar à da lista, no entanto, ela é
  imutável.
|   Ela é mais recomendada para uso de dados estáticos, pois comparada à
  lista, tem
| um desempenho melhor devido à sua simplicidade e consome menos
  recursos.

``` python
# Declaração de uma tupla vazia:
t = ()
```

ou

``` python
t = tuple()
```

``` python
# Declaração de uma tupla com três elementos:
t = tuple([1, 2, 3])
```

ou

``` python
t = (1, 2, 3)
```

ou

``` python
t = 1, 2, 3
```

``` python
# Exibindo o conteúdo da tupla:
t
```

``` console
(1, 2, 3)
```

``` python
# Criação de um conjunto (set) contendo todos atributos e 
# métodos de uma tupla:
tupla = set(dir(tuple))
```

``` python
# Criação de um conjunto (set) contendo todos atributos e 
# métodos de uma lista:
lista = set(dir(list))
```

``` python
# Via intersecção, o que há em comum entre lista e tupla?:
tupla.intersection(lista)
```

. . .

Tuplas tem apenas os métodos count e index.

``` python
# Tupla de um único elemento:
t = (1, )
```

``` python
# Exibir o conteúdo da tupla:
t
```

``` console
(1,)
```

``` python
# Função type para verificar o tipo do objeto:
type(t)
```

``` console
tuple
```

``` python
# Declaração de duas variáveis e trocando o valor entre elas:
x = 0
y = 1
x, y = y, x  # A troca se dá pela atribuição respectiva
```

``` python
# Verificando os valores das variáveis:
x
```

``` console
1
```

``` python
y
```

``` console
0
```

``` python
# Criação de uma variável que retorna uma tupla com três elementos:
def retorna_tupla():
    return 1, 2, 3
```

``` python
# Atribuição respectiva:
x, y, z = retorna_tupla()
```

``` python
# Verificando os valores das variáveis:
print(x)
```

``` console
1
```

``` python
print(y)
```

``` console
2
```

``` python
print(z)
```

``` console
3
```

Tuplas são imutáveis, mas seus elementos não necessariamente:

``` python
t = ({}, [])   # Tupla com dois elementos; um dicionário e uma lista
t[0].update({'chave': 'valor'})  # Alterando o primeiro elemento
t[1].append(7)  # Alterando o segundo elemento
t  # Exibindo a tupla
```

``` console
({'chave': 'valor'}, [7])
```
