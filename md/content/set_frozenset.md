---
title: set e frozenset
---

|    Similarmente a list e tuple, a diferença entre eles é que frozenset
  é um tipo imutável.
|    Seus elementos são únicos.
|    Implementam operações matemáticas de conjuntos.

``` python
# Set vazio:
s = {*()}
```

ou

``` python
s = set()
```

``` python
# Criação de um conjunto (set) não vazio:
s = set([1, 1, 2, 3])
```

ou

``` python
s = set((1, 1, 2, 3))
```

ou

``` python
s = set([1, 1, 2, 3])
```

ou

``` python
s = set({1, 1, 2, 3})
```

ou

``` python
s = {1, 2, 3}
```

``` python
# Exibindo o conteúdo do set:
s
```

``` console
{1, 2, 3}
```

``` python
# Definição de dois conjuntos:
a = set([1,2,3])
b = set([2,3,4])
```

``` python
# Operação de união entre os conjuntos:
a | b
```

ou

``` python
a.union(b)
```

``` console
{1, 2, 3, 4}
```

``` python
# Operação de intersecção entre os conjuntos:
a & b
```

ou

``` python
a.intersection(b)
```

``` console
{2, 3}
```

``` python
# Frozenset vazio:
f = frozenset()
```

``` python
# Frozenset não vazio:
f = frozenset((1, 2, 3))
```

ou

``` python
f = frozenset({1, 2, 3})
```

ou

``` python
f = frozenset([1, 2, 3])
```

ou

``` python
f = frozenset({1, 2, 3})
```

``` python
# Exibindo o conteúdo do frozenset:
f
```

``` console
frozenset({1, 2, 3})
```
