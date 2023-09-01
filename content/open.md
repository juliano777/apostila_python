# open

É a forma nativa de Python para manipular arquivos (leitura e escrita).  
Um arquivo é iterável, cujas iterações são por linha.  

> **`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`**

| **Modo** | **Descrição**                                                            |
|----------|--------------------------------------------------------------------------|
| `r`      | Leitura (padrão)                                                         |
| `w`      | Escrita (novo arquivo, ou se o mesmo existir será truncado)              |
| `x`      | Cria um novo arquivo e o abre para escrita                               |
| `a`      | Escrita (*append*; o novo conteúdo é adicionado ao arquivo preexistente) |
| `b`      | Modo binário                                                             |
| `t`      | Modo de texto (padrão)                                                   |
| `+`      | Abre um arquivo em disco para a atualização (leitura e escrita)          |


``` python
# Supondo que o arquivo não exista, criação do mesmo para leitura e escrita
f = open('/tmp/foo.txt', 'w+')

# Verificando o tipo de f
type(f)
```

``` console
_io.TextIOWrapper
```

``` python
# Escrevendo no arquivo com a função print
print('Teste de escrita em arquivo', file=f)

# Uma linha em branco
print(' ', file=f)

# Mais uma linha\...
print('Uma linha qualquer', file=f)

# Fechando o objeto e aplicando todas as escritas feitas
f.close()

# Reabrindo o arquivo para somente leitura
f = open('/tmp/foo.txt', 'r')

# Imprimir o arquivo em tela linha por linha
for line in f:
    print(line.strip('\n'))
```

```
Teste de escrita em arquivo
 
Uma linha qualquer
```
``` python
# Fechamento de arquivo
f.close()
```

No shell do sistema operacional usar o recurso *heredoc* para criar linhas em
um novo arquivo:

``` bash
cat << EOF > /tmp/linhas.txt
linha_1
linha_2
linha_3
EOF
```

Exibir as linhas:

``` bash
cat /tmp/linhas.txt
```

``` console
linha_1
linha_2
linha_3
```

Em um shell Python abrir o arquivo:

``` python
f = open('/tmp/linhas.txt')

# Método readline
f.readline()

```

``` console
'linha_1\n'
```

Método split na saída do método readline (3X):

``` python
f.readline().split()
```

``` console
['linha_2']
```

``` console
['linha_3']
```

``` console
[]
```

O método `readline()` interagiu para cada linha retornando-a até não ter mais
nada a ler no arquivo.


``` python
# Fechando o arquivo
f.close()

# Reabrindo o arquivo
f = open('/tmp/linhas.txt')

# Método readlines()
f.readlines()
```

``` console
['linha_1\n', 'linha_2\n', 'linha_3\n']
```

O método `readlines()` retorna cada linha do arquivo como um elemento de uma
lista.

``` python
# Fechando o arquivo
f.close()
```

Criar um script Python cujo comportamento é o mesmo do utilitário *shell*
`cat`:

``` bash
vim /tmp/cat.py
```

Código Python:

``` python
#!/usr/bin/env python3
#_*_ encoding: utf8 _*_

import sys

# Primeiro argumento do script
f = sys.argv[1]

# Abrir o arquivo como somente leitura (sobrescreve a variável original)
f = open(f, 'r')

# Para cada linha imprimir, com o método strip suprimindo linhas em branco
# desnecessárias. (Supressão de \n no final de cada linha)
for i in f:
    print(i.strip())

f.close()
```

Tornar o script executável:

``` bash
chmod +x /tmp/cat.py
```

Teste do script:

``` bash
/tmp/cat.py /tmp/linhas.txt
```

``` console
linha_1
linha_2
linha_3
```

Novo arquivo criado via shell do sistema operacional:

``` bash
cat << EOF > /tmp/cores.txt
1 - Verde
2 - Preto
3 - Branco
EOF
```

``` python
# Abrir o arquivo em modo somente leitura
f = open('/tmp/cores.txt', 'r')

# Um simples loop for sobre o arquivo
for i in f:
    print(i.strip())
```

``` python
1 - Verde
2 - Preto
3 - Branco
```

``` python
# Nova execução do loop
for i in f:
    print(i.strip())

# Método seek; posição 0 do cursor
f.seek(0)

# Nova execução do loop
for i in f:
    print(i.strip())
```

``` console
1 - Verde
2 - Preto
3 - Branco
```

``` python
# Posição 1
f.seek(1)

# Nova execução do loop
for i in f:
    print(i.strip())
```

``` console
- Verde
2 - Preto
3 - Branco
```

``` python
# Posição 0 (zero) do cursor
f.seek(0)

# Ler as 7 (sete) primeiras posições
f.read(7)
```

``` console
'1 - Ver'
```

Ler as próximas 7 (sete) posições (repetir):
``` python
f.read(7)
```

``` console
'de\n2 - '
```

``` console
'Preto\n3'
```

``` console
' - Bran'
```

``` python
# Fechar o arquivo
f.close()

# Verificar se o arquivo está fechado como o atributo closed
f.closed
```

``` console
True
```

``` python
# Abrir o arquivo como escrita
f = open('/tmp/cores.txt', 'w')

# Verificar se o arquivo está fechado como o atributo closed
f.closed
```

``` console
False
```

``` python
# Fechar o arquivo
f.close()
```

Verificar o conteúdo do arquivo via shell do sistema operacional:

``` bash
cat /tmp/cores.txt
```

``` python
# Abrir p arquivo como escrita
f = open('/tmp/cores.txt', 'w')

# Escrever no arquivo
f.write('1 - Verde\n')

# Fechar o arquivo
f.close()
```

Verificar o conteúdo do arquivo via *shell* do sistema operacional:

``` bash
cat /tmp/cores.txt
```

``` console
1 - Verde
```

Todo o conteúdo foi substituído por essa linha...

``` python
# Exibir a localização do arquivo
print(f.name)
```

``` console
/tmp/cores.txt
```

``` python
# Abrir o arquivo em modo append
f = open('/tmp/cores.txt', 'a')

# Adicionar novas linhas ao arquivo
f.write('2 - Preto\n')
f.write('3 - Branco\n')

# Efetivar a escrita no arquivo sem fechá-lo
f.flush()
```

Verificar o conteúdo do arquivo via *shell* do sistema operacional:

``` bash
cat /tmp/cores.txt
```

``` console
1 - Verde
2 - Preto
3 - Branco
```

``` python
# Fechar o arquivo
f.close()

# Abrir o arquivo em modo leitura
f = open('/tmp/cores.txt', 'r')

# Método tell; retorna a posição atual
f.tell()
```

``` console
0
```

``` python
# Método read
f.read()
```

``` console
'1 - Verde\n2 - Preto\n3 - Branco\n'
```

``` python
# Veriricando a atual posição
f.tell()
```

``` console
31
```

``` python
# Método seek recoloca o cursor na posição 0 (zero)
f.seek(0)
```

``` console
0
```

``` python
# Método tell confirma
f.tell()
```

``` console
0
```

``` python
# Ler 7 (sete) posições adiante
f.read(7)
```

``` console
'1 - Ver'
```

``` python
# Método tell
f.tell()
```

``` console
7
```

``` python
# Fechar o arquivo
f.close()

# Criar um novo arquivo como escrita
f = open('/tmp/planetas.txt', 'w')

# Tupla com 3 (três) elementos
planetas = ('Saturno\n', 'Urano\n', 'Netuno\n')

# Escreve linhas no arquivo com os elementos da tupla
f.writelines(planetas)

# Efetiva a escrita
f.flush()
```

Verificando o conteúdo do arquivo via *shell* do sistema operacional:

``` bash
cat /tmp/planetas.txt
```

``` console
Saturno
Urano
Netuno
```

``` python
# Redefinindo a tupla com outros elementos
planetas = ('Marte\n', 'Vênus\n', 'Plutão\n', 'Júpiter\n')

# Escrevendo (adicionando) linhas
f.writelines(planetas)

# Fechar o arquivo
f.close()
```

Verificando o conteúdo do arquivo via shell do sistema operacional:

``` bash
cat /tmp/planetas.txt
```

``` console
Saturno
Urano
Netuno
Marte
Vênus
Plutão
Júpiter
```
