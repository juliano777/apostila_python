Data e Hora
***********

datetime
--------

Módulo que fornece classes para manipular datas e horas de maneiras simples e complexas. Enquanto data e hora são suportados aritmeticamente, o foco da implementação estã em uma extração eficiente de atributo para saída formatada e manipulação.


.. code-block:: python

    # Imports:
    from datetime import date
    from datetime import datetime
    from sys import getsizeof


.. code-block:: python

    # Inserir dados via teclado conforme sugere o modelo na mensagem:
    dt_evento = input('Digite a data e hora do evento (AAAA-MM-DD HH:MM): ')

.. code-block:: console

    Digite a data e hora do evento (AAAA-MM-DD HH:MM):

.. code-block:: python

    # Verificando o tipo da variável:
    type(dt_evento)

.. code-block:: console

    str

.. code-block:: python

    # Quanto custa essa variável em bytes?:
    getsizeof(dt_evento)

.. code-block:: console

    65


| Strings não são adequadas para armazenar data e hora.
| strptime transforma uma string para datetime conforme uma dada máscara:



.. code-block:: python

    # Converter a string para datetime:
    datetime.strptime(dt_evento, '%Y-%m-%d %H:%M')

.. code-block:: console

    datetime.datetime(2019, 12, 27, 19, 0)

.. class:: center    
    
    **strptime: str -> datetime**


.. code-block:: python

    # O tamanho em bytes do dado em datetime:
    getsizeof(datetime.strptime(dt_evento, '%Y-%m-%d %H:%M'))

.. code-block:: console

    48

A mesma informação armazenada como datetime ocupa menos espaço que string.

.. code-block:: python

    # Recriar a variável como datetime utilizando seu valor antigo de string:
    dt_evento = datetime.strptime(dt_evento, '%Y-%m-%d %H:%M')

    # Verificando o tipo:
    type(dt_evento)

.. code-block:: console

    datetime.datetime



Pode ser necessário também fazer o caminho inverso, para transformar um dado datetime para string.

    Para isso pode-se usar strftime:

    strftime: datetime -> str

.. code-block:: python

    # Extrair como string de um dado datetime:
    datetime.strftime(dt_evento, '%Y-%m-%d %H:%M')

.. code-block:: console

    '2019-12-27 19:00'

.. code-block:: python

    # Variável que contém apenas a data atual:
    hoje = date.today()

    # Exibindo o valor da variável:
    print(hoje)

.. code-block:: console

    2019-12-26

Exibindo apenas partes da data:    

.. code-block:: python

    # dia:
    print(hoje.day)

.. code-block:: console

    26

.. code-block:: python

    # mês:
    print(hoje.month)

.. code-block:: console

    12

.. code-block:: python

    # ano:
    print(hoje.year)

.. code-block:: console

    2019

.. code-block:: python

    # Formato ISO:
    hoje.isoformat()

.. code-block:: console

    '2019-12-26'

.. code-block:: python

    # Método toordinal; retorna a quantidade de dias 
    # passados desde 01/01/0001:
    hoje.toordinal()

.. code-block:: console

    737419

.. code-block:: python

    # Método fromordinal; retorna a data a partir da quantidade 
    # de dias passados desde 01/01/0001:
    date.fromordinal(737419)

.. code-block:: console

    datetime.date(2019, 12, 26)

.. code-block:: python

    # Que dia será daqui a 40 dias?:
    date.fromordinal(hoje.toordinal() + 40)   # formato datetime.date

.. code-block:: console

    datetime.date(2020, 2, 4)

.. code-block:: python

    # Formato ISO:
    date.fromordinal(hoje.toordinal() + 40).isoformat()

.. code-block:: console

    '2020-02-04'

.. code-block:: python

    # Método weekday (dia da semana), em que segunda-feira = 0 e domingo = 6:
    hoje.weekday()

.. code-block:: console

    3

.. code-block:: python

    # Método isoweekday, em que segunda-feira = 1 e domingo = 7
    hoje.isoweekday()

.. code-block:: console

    4


O Módulo time
-------------

    Módulo cujos objetos representam uma hora (local) de dia, independente de qualquer dia em particular, e sujeito a ajustes via um objeto tzinfo.
    Fornece várias funções para manipular valores de hora. Não confundir com a classe time do módulo datetime.

.. code-block:: python

    # Imports:
    from time import ctime
    from time import sleep
    from time import time
    from time import tzname    

.. code-block:: python

    # Criação de função que espera n segundos e exibe uma mensagem no final:
    def espera(tempo):
        sleep(tempo)
        print(f'Passaram-se {tempo} segundos')

.. code-block:: python

    # Execução da função:
    espera(3)

.. code-block:: console

    Passaram-se 3 segundos

.. code-block:: python

    # time.time retorna o tempo atual em segundos 
    # desde Epoch (01/01/1970 00:00:00):
    time()

.. code-block:: console

    1577375404.8968937

.. code-block:: python

    # Converte um tempo em segundos desde Epoch para uma string, 
    # se nenhum parâmetro for passado retorna string do momento atual:

.. code-block:: python

    # :
    ctime()

.. code-block:: console

    'Thu Dec 26 12:50:22 2019'

.. code-block:: python

    # :
    ctime(1540000000)

.. code-block:: console

    'Fri Oct 19 22:46:40 2018'