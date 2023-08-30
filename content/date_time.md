# Data e hora

## O módulo datetime

Módulo que fornece classes para manipular datas e horas de maneiras simples e
complexas.  
Enquanto data e hora são suportados aritmeticamente, o foco da implementação
estão em uma extração eficiente de atributo para saída formatada e
manipulação.

``` python
# Imports:
from datetime import date
from datetime import datetime
from sys import getsizeof
```

``` python
# Inserir dados via teclado conforme sugere o modelo na mensagem:
dt_evento = input('Digite a data e hora do evento (AAAA-MM-DD HH:MM): ')
```

``` console
Digite a data e hora do evento (AAAA-MM-DD HH:MM):
```

``` python
# Verificando o tipo da variável:
type(dt_evento)
```

``` console
str
```

``` python
# Quanto custa essa variável em bytes?:
getsizeof(dt_evento)
```

``` console
65
```

Strings não são adequadas para armazenar data e hora.  
`strptime()` transforma uma *string* para `datetime` conforme uma dada
máscara:

``` python
# Converter a string para datetime:
datetime.strptime(dt_evento, '%Y-%m-%d %H:%M')
```

``` console
datetime.datetime(2019, 12, 27, 19, 0)
```

## strptime: str -> datetime

``` python
# O tamanho em bytes do dado em datetime:
getsizeof(datetime.strptime(dt_evento, '%Y-%m-%d %H:%M'))
```

``` console
48
```

A mesma informação armazenada como datetime ocupa menos espaço que *string*.

``` python
# Recriar a variável como datetime utilizando seu valor antigo de string:
dt_evento = datetime.strptime(dt_evento, '%Y-%m-%d %H:%M')

# Verificando o tipo:
type(dt_evento)
```

``` console
datetime.datetime
```

Pode ser necessário também fazer o caminho inverso, para transformar um dado
`datetime` para *string*.

Para isso pode-se usar `strftime()`:

``` python
# Extrair como string de um dado datetime:
datetime.strftime(dt_evento, '%Y-%m-%d %H:%M')
```

``` console
'2019-12-27 19:00'
```

## strftime: datetime -> str

``` python
# Variável que contém apenas a data atual:
hoje = date.today()

# Exibindo o valor da variável:
print(hoje)
```

``` console
2019-12-26
```

Exibindo apenas partes da data:

``` python
# dia:
print(hoje.day)
```

``` console
26
```

``` python
# mês:
print(hoje.month)
```

``` console
12
```

``` python
# ano:
print(hoje.year)
```

``` console
2019
```

``` python
# Formato ISO:
hoje.isoformat()
```

``` console
'2019-12-26'
```

``` python
# Método toordinal; retorna a quantidade de dias 
# passados desde 01/01/0001:
hoje.toordinal()
```

``` console
737419
```

``` python
# Método fromordinal; retorna a data a partir da quantidade 
# de dias passados desde 01/01/0001:
date.fromordinal(737419)
```

``` console
datetime.date(2019, 12, 26)
```

``` python
# Que dia será daqui a 40 dias?:
date.fromordinal(hoje.toordinal() + 40)   # formato datetime.date
```

``` console
datetime.date(2020, 2, 4)
```

``` python
# Formato ISO:
date.fromordinal(hoje.toordinal() + 40).isoformat()
```

``` console
'2020-02-04'
```

``` python
# Método weekday (dia da semana), em que segunda-feira = 0 e domingo = 6:
hoje.weekday()
```

``` console
3
```

``` python
# Método isoweekday, em que segunda-feira = 1 e domingo = 7
hoje.isoweekday()
```

``` console
4
```

# O Módulo time

Módulo cujos objetos representam uma hora (local) de dia, independente de
qualquer dia em particular, e sujeito a ajustes via um objeto `tzinfo`.  
Fornece várias funções para manipular valores de hora.  
Não confundir com a classe `time` do módulo `datetime`.

``` python
# Imports:
from time import ctime
from time import sleep
from time import time
from time import tzname    
```

``` python
# Criação de função que espera n segundos e exibe uma mensagem no final:
def espera(tempo):
    sleep(tempo)
    print(f'Passaram-se {tempo} segundos')
```

``` python
# Execução da função:
espera(3)
```

``` console
Passaram-se 3 segundos
```

``` python
# time.time retorna o tempo atual em segundos 
# desde Epoch (01/01/1970 00:00:00):
time()
```

``` console
1577375404.8968937
```

``` python
# Converte um tempo em segundos desde Epoch para uma string, 
# se nenhum parâmetro for passado retorna string do momento atual:
ctime()
```

``` console
'Thu Dec 26 12:50:22 2019'
```

``` python
ctime(1540000000)
```

``` console
'Fri Oct 19 22:46:40 2018'
```
