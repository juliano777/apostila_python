# O Módulo decimal

Fornece suporte para aritmética de ponto flutuante decimal.  
Oferece muitas vantagens sobre o tipo `float`.  
É baseado em um modelo de ponto flutuante que foi projetado com pessoas em
mente e necessariamente tem um princípio orientador fundamental; computadores
devem fornecer uma aritmética que funciona da mesma maneira que a aritmética
que as pessoas aprendem na escola, extraindo da especificação da aritmética
decimal.  
Números decimais podem ser representados exatamente.  
Em contraste, números como `1.1` e `2.2` não têm representações exatas em
ponto flutuante binário.  
Usuários finais não esperam que `1.1 + 2.2` seja exibido como
`3.3000000000000003` como é feito como o ponto flutuante binário.  
A exatidão leva à aritmética. Com ponto flutuante decimal,
`0.1 + 0.1 + 0.1 - 0.3` é exatamente igual a zero.
Com ponto flutuante binário, o resultado é `5.5511151231257827e-017`. Enquanto
próximo a zero, as diferenças evitam testes de igualdade confiáveis e
diferenças podem acumular. Por essa razão, `decimal` é preferido em aplicações
de contabilidade que têm invariações de igualdade rigorosas.  
O módulo decimal incorpora a noção de posições (casas decimais) significantes
em que `1.30 + 1.20` é `2.50`. O zero no fim é mantido para indicar a
significância. Essa é a apresentação habitual para aplicações monetárias.
Para multiplicação, a abordagem do "livro de escola" usa todos os números nos
multiplicandos. Por exemplo; `1.3 * 1.2` dá `1.56` enquanto que `1.30 * 1.20`
dá `1.5600`. Ao contrário de *hardware* baseado em ponto flutuante binário, o
módulo `decimal` tem uma precisão alterável (padrão 28 casas decimais).

``` python
# Importação do módulo:
import decimal

# Criação do objeto Decimal:
d = decimal.Decimal('0.777')

# Exibindo o valor do objeto decimal:
d
```

``` console
Decimal('0.777')
```

``` python
# Exibe o valor de "d":
print(d)
```

``` console
0.777
```

Algumas coisas \"estranhas\":

``` python
# Somando dois floats:
1.1 + 2.2
```

``` console
3.3000000000000003
```

``` python
# Outra operação com floats:
0.1 + 0.1 + 0.1 - 0.3
```

``` console
5.551115123125783e-17
```

``` python
# Importando apenas a classe Decimal:
from decimal import Decimal

# Fazendo as mesmas operações anteriores com o módulo decimal:
Decimal('1.1') + Decimal('2.2')
```

``` console
Decimal('3.3')
```

``` python
# Importando a função getcontext:
from decimal import getcontext

# Operações de multiplicação:
Decimal('1.3') * Decimal('1.2')
```

``` console
Decimal('1.56')
```

``` python
# Multiplicação de decimais:
Decimal('1.30') * Decimal('1.20')
```

``` console
Decimal('1.5600')
```

O último retorno foi com um número com 4 (quatro) casas decimais.  
  
A função `getcontext()`, com o atributo 'prec' (*precision*) ajusta a
quantidade máxima de dígitos (antes e depois do ponto flutuante) para 3
(três):

``` python
# Alterar o nível de precisão para 3:
getcontext().prec = 3
```

A precisão vai ser refletida em operações com o módulo decimal. Caso
seja necessário o número será arredondado.

``` python
# Operação de multiplicação de números com ponto flutuante
Decimal('1.300') * Decimal('1.200')
```

``` console
Decimal('1.56')
```

``` python
# Ajustando a precisão para 10 (dez)
getcontext().prec = 10

# Multiplicação:
Decimal('1.3897') * 2
```

``` console
Decimal('2.7794')
```

``` python
# Ajustando a precisão para 3 (três):
getcontext().prec = 3

# Multiplicação:
Decimal('1.3897') * 2
```

``` console
Decimal('2.78')
```

Nota-se que foi feito um arredondamento do número.
