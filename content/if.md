
# if / elif / else

O comando if, que inglês significa "se" indica uma condição.  
  
``` python
# Criação de dois objetos int
x = 7
y = 5
```

``` python
# Bloco if teste se x é maior que y
if x > y:
    print('X é maior')
```

``` console
X é maior
```

``` python
# Bloco if teste se x é menor que y
if x < y:
    print('Y é maior')
```

Aqui nada aconteceu, pois a condição de if não foi satisfeita.  

``` python
# Criação de duas variáveis booleanas
foo = True
bar = False
```

``` python
# Modo "pythônico" de se testar um valor booleano
if foo:
    print('foo é verdadeiro!')
```

``` console
foo é verdadeiro!
```

Note que não foi testado `[foo == False]`, utilizou-se uma maneira muito mais elegante.  

``` python
# Testando uma Variável booleana com negação
if not bar:
    print('bar é falso!')
```

``` console
bar é falso!
```

Podemos também de maneira parecida, se a variável tiver um conteúdo:

``` python
# Objeto string:
texto = 'Python e PostgreSQL: Poder!'

# Bloco if:
if texto:
    print('A string NÃO é vazia!')
```

``` console
A string NÃO é vazia!
```

Teste de negação com string vazia:

``` python
# String vazia:
texto = ''

# Bloco if:
if not texto:
    print('A string é vazia!')
```

``` console
A string é vazia!
```

Boco if com else:

``` python
# Objetos int:
x = 1
y = 2

# Bloco if:
if x > y:
    print('X é maior')
else:
    print('Y é maior')
```

``` python
Y é maior
```

Bloco if com elif:

``` python
# Objetos int:
y = 1
x = 1

# Bloco if:
if x > y:
    print('X é maior')
elif x < y:    
    print('Y é maior')
else:    
    print('Valores iguais')
```

``` console
Valores iguais
```

O valor de y depende de x:

``` python
# Objeto int:
x = 10

# Bloco if:    
if (x > 5):
    y = 3
else:
    y = 0

# Exibe o resultado
print(y)
```

``` console
3
```

## Operador ternário

Um recurso bastante interessante em outras linguagens como em C, por
exemplo.  
Seu objetivo é abreviar um bloco if em apenas uma linha.  
  
Sintaxe:
  
> `retorno_se_verdadeiro` **`if`** `condição` **`else`** `retorno_se_falso`

Declaração de uma variável x com valor, atribui a y o resultado e exibe seu
valor:

``` python
x = 10  # Variável int

# Atribuição de valor condicional:
y = (50 if (x > 5) else 40)

# Exibe o valor de "y":
print(y)
```

``` console
50
```

``` python
# Variável float para receber a nota
nota = float(input('Digite a nota do aluno: '))
```

``` console
Digite a nota do aluno: 8
```

``` python
# Atribuição condicional
estado = 'aprovado' if nota >= 7 else 'reprovado'

# Exibe a mensagem
print(f'Aluno {estado}!')
```

``` console
Aluno aprovado!
```

``` python
# Variável int
num = int(input('Digite um número: '))
```

``` console
Digite um número: -2
```

``` python
# Atribuição condicional
sinal = 'positivo' if num > 0 else 'negativo' if num < 0 else 'zero'

# Exibe mensagem
print(f'O número é {sinal}'
```

``` console
O número é negativo
```
