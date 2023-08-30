# Tipos Numéricos - int, float e complex


# int

> Para representação de todos números inteiros é o tipo int. A princípio
> utilizamos para números inteiros o tipo int. O número máximo de int
> que é aceito pode variar de uma máquina para outra. Para sabermos qual
> é o número máximo do tipo int fazemos:

``` python
# Objeto inteiro:
i = int(7)
```

ou

``` python
i = 7
```

``` python
# Verificando seu valor:
i
```

``` console
7
```

``` python
# Verificando seu tipo:
type(i)
```

``` console
int
```

``` python
# Tipo de "bar":
type(bar)
```

``` console
long
```

``` python
# Representação hexadecimal de 178
0xb2
```

``` console
178
```

``` python
# Representação octal de 8:
0o10
```

``` console
8
```

``` python
# Representação binária de 14:
0b1110
```

``` console
14
```

``` python
# Número 7 (sete) convertido para as bases 
# binária, hexadecimal e octal respectivamente:
bin(7)
```

``` console
'0b111'
```

``` python
# Retorna a forma octal de 7:
oct(7)
```

``` console
'0o7'
```

``` python
# Retorna a versão hexadecimal de 7:
hex(7)
```

``` console
'0x7'
```

``` python
# Descobrir o decimal dada uma base:
int('facada', base=16)
```

``` console
16435930
```

``` python
# 25 octal em decimal é:
int('25', base=8)
```

``` console
21
```

``` python
# 1111 binário é em decimal:
int('1111', base=2)
```

``` console
15
```

# float

> Ponto flutuante; não tem precisão absoluta, sua precisão é relativa.
> Para uma maior precisão com números que tenham ponto flutuante,
> utilizar o módulo decimal.

``` python
# Criação de um float:
f = float(3)
```

ou

``` python
f = 3.0
```

``` python
f  # Veririca o valor
```

``` console
3.0
```

Formas de se definir um float:

``` python
x = 0.5000000000
```

ou

``` python
x = 0.5
```

ou

``` python
x = .5

x  # Exibe o valor
```

``` console
0.5
```

``` python
type(x)  # Tipo
```

``` console
float
```

``` python
x = 2.

x  # Verifica o valor
```

``` console
2.0
```

``` python
# Que tipo resulta de da soma de um inteiro e um float?:
type(7 + 3.0)
```

``` console
float
```

``` python
# Resultado:
7 + 3.0
```

``` console
10.0
```

``` python
# Divisão:
3 / 2
```

ou

``` python
3 / 2.0
```

ou

``` python
3.0 / 2
```

ou

``` python
3.0 / 2.0
```

``` console
1.5
```

``` python
# Divisão Inteira:
3 // 2.0
```

``` console
1.0
```

``` python
# Notação Científica:
1e+2
```

``` console
100.0
```

``` python
# Notação científica com expoente negativo:
1e-3
```

``` console
0.001
```

# complex

> É o tipo de dados em Python que trata de números complexos, que são
> muito utilizados em engenharia elétrica.

``` python
# Número complexo somente com a parte real:
c = complex(1)
print(c)
```

``` console
(1+0j)
```

``` python
# Verificando seu valor e seu tipo:
type(c)
```

``` console
complex
```

``` python
# Novo valor do número complexo com parte real e imaginária:
c = complex(5, 3)
```

``` python
c  # Verificando o valor
```

``` console
(5+3j)
```

``` python
# Número complexo somente com a parte imaginária:
c = complex(0, 3)
```

``` python
c  # Verificando seu valor
```

``` console
3j
```

``` python
c.imag  # Extraindo somente a parte imaginária
```

``` console
3.0
```

``` python
c.real  # Extraindo somente a parte real
```

``` console
0.0
```

``` python
c + 1  # Somando o número com a parte real
```

``` console
(1+3j)
```

``` python
c + complex('7j')  # Somando o número com a parte imaginária
```

``` console
10j
```

``` python
c + complex(2, 17)  # somando o número complexo com outro complexo
```

``` console
(2+20j)
```
