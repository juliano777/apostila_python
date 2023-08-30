# Loops - laços de Repetição

## while

|   Executa em laço (loop) **enquanto** a condição for verdadeira.

Enquanto i for menor que 5, exiba i:

``` python
i = 0

while i < 5:
    print(i)
    i += 1
```

``` console
0
1
2
3
4
```

# O else no loop while

|   Opcionalmente, pode-se adicionar um else ao while em Python.
|   A idéia é que se caso o loop seja executado sem interrupção, um
  break, por exemplo, o que estiver dentro do bloco else será executado.

Loop while com else sem interrupção:

``` python
i = 0
while i < 5:
    print(i)
    i += 1
else:   
    print('Fim')
```

``` console
0
1
2
3
4
Fim
```

Loop while com else com interrupção (break):

``` python
i = 0

while i <= 10:
    if i == 5: break       
    print(i)
    i += 1
else:   
    print('Fim')
```

``` console
0
1
2
3
4
```

Loop while com else e sem break:

``` python
i = 0

while i <= 10:
    if (i % 2 == 0): 
        i += 1
        continue
    print(i)
    i += 1        
else:   
    print('Fim')
```

``` console
1
3
5
7
9
Fim
```

# Loop Infinito

|   Em determinadas situações se faz necessário o uso de um loop sem
  fim.
|   Para que esse loop infinito seja rompido é preciso que uma ação
  externa ocorra, como uma interrupção com a combinação de teclas
  \<Ctrl\> + C.

Enquanto não houver uma interrupção externa, o loop abaixo exibirá \"x\"
eternamente:

``` python
while True:
    print('x')
```

``` console
x
x
x
. . .
```

# for

|   O loop for interage sobre cada membro de um objeto iterável.

Um simples loop for com a função range:

``` python
for i in range(5):
    print(i)
```

``` console
0
1
2
3
4
```

Loop sobre os elementos de uma tupla:

``` python
lor = ('Gandalf', 'Bilbo', 'Frodo', 'Sauron', 'Aragorn', 'Legolas')

for i in lor:
    print(i)
```

``` console
Gandalf
Bilbo
Frodo
Sauron
Aragorn
Legolas
```

Loop sobr os elementos da tupla enumerados:

``` python
for i, personagem in enumerate(lor):
    print(f'{i} - {personagem}')
```

``` console
0 - Gandalf
1 - Bilbo
2 - Frodo
3 - Sauron
4 - Aragorn
5 - Legolas
```

Enumerando a tupla e convertendo-a para uma lista:

``` python
list(enumerate(lor))
```

``` console
[(0, 'Gandalf'), (1, 'Bilbo'), (2, 'Frodo'), (3, 'Sauron'), (4, 'Aragorn'), (5, 'Legolas')]
```

Lista cujos elementos são tuplas cujos elementos representam chave e
valor, e por fim loop:

``` python
dados =  [('Nome', 'Chiquinho'), ('Sobrenome', 'da Silva'), ('Idade', 50)]

for k, v in dados:
    print(f'{k}: {v}')
```

``` console
Nome: Chiquinho
Sobrenome: da Silva
Idade: 50
```

Criação de um dicionário:

``` python
dados = {
    'Nome': 'Chiquinho',
    'Sobrenome': 'da Silva',
    'Idade': 50
}
```

Loop sobre um dicionário:

``` python
for k, v in dados.items():
    print(f'{k}: {v}')
```

``` console
Sobrenome: da Silva
Idade: 50
Nome: Chiquinho
```

Loop for com else e sem interrupção:

``` python
for i in range(5):
    print(i)
else:
    print('Fim')
```

``` console
0
1
2
3
4
Fim
```

Loop for com else e com interrupção:

``` python
for i in range(10):
    if i == 6:
        break
    print(i)
else:
    print('Fim')
```

``` console
0
1
2
3
4
5
```

Loop for com else e sem interrupção:

``` python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
else:
    print('Fim')
```

``` console
1
3
5
7
9
Fim
```
