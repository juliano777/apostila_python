open
****


|   É a forma nativa de Python para manipular arquivos (leitura e escrita).
|   Um arquivo é iterável, cujas iterações são por linha.

`open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`

+---------+--------------------------------------------------------------------------+
|**Modo** | **Descrição**                                                            |
+---------+--------------------------------------------------------------------------+
| r       | Leitura (padrão).                                                        |
+---------+--------------------------------------------------------------------------+
| w       | Escrita (novo arquivo, ou se o mesmo existir será truncado).             |
+---------+--------------------------------------------------------------------------+
| x       | Cria um novo arquivo e o abre para escrita.                              |
+---------+--------------------------------------------------------------------------+
| a       | Escrita (append; o novo conteúdo é adicionado ao arquivo pré existente). |
+---------+--------------------------------------------------------------------------+
| b       | Modo binário.                                                            |
+---------+--------------------------------------------------------------------------+
| t       | Modo de texto (padrão).                                                  |
+---------+--------------------------------------------------------------------------+
| \+      | Abre um arquivo em disco para a atualização (leitura e escrita).         |
+---------+--------------------------------------------------------------------------+



bla bla bla:

.. code-block:: python

    f = open('/tmp/foo.txt', 'w+')



bla bla bla:

.. code-block:: python

    type(f)

.. code-block:: console

    _io.TextIOWrapper



bla bla bla:

.. code-block:: python

    print('Teste de escrita em arquivo', file=f)



bla bla bla:

.. code-block:: python

    print(' ', file=f)



bla bla bla:

.. code-block:: python

    print('Uma linha qualquer', file=f)



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: python

    f = open('/tmp/foo.txt', 'r')



bla bla bla:

.. code-block:: python

    for line in f:
    print(line.strip('\n'))



Fechamento de arquivo:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: bash

    cat << EOF > /tmp/linhas.txt
    linha_1
    linha_2
    linha_3
    EOF



bla bla bla:

.. code-block:: bash

    cat /tmp/linhas.txt

.. code-block:: console

    linha_1
    linha_2
    linha_3



bla bla bla:

.. code-block:: python

    f = open('/tmp/linhas.txt')



bla bla bla:

.. code-block:: python

    f.readline()

.. code-block:: console

    'linha_1\n'



bla bla bla:

.. code-block:: python

    f.readline().split()

.. code-block:: console

    ['linha_2']



bla bla bla:

.. code-block:: python

    f.readline().split()

.. code-block:: console

    ['linha_3']



bla bla bla:

.. code-block:: python

    f.readline().split()

.. code-block:: console

    []



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: python

    f = open('/tmp/linhas.txt')



bla bla bla:

.. code-block:: python

    f.readlines()

.. code-block:: console

    ['linha_1\n', 'linha_2\n', 'linha_3\n']



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: bash

    cat << EOF > /tmp/teste.py
    #!/usr/bin/env python3
    #_*_ encoding: utf8 _*_

    import sys

    file_open = sys.argv[1]


    file_open = open(file_open, 'r')

    for i in file_open:
        print(i.strip())

    file_open.close()
    EOF



bla bla bla:

.. code-block:: bash

    chmod +x /tmp/teste.py



bla bla bla:

.. code-block:: bash

    ./teste.py linhas.txt

.. code-block:: console

    linha_1
    linha_2
    linha_3



O Método seek:

.. code-block:: bash

    cat << EOF > /tmp/cores.txt
    1 - Verde
    2 - Preto
    3 - Branco
    EOF



bla bla bla:

.. code-block:: python

    f = open('/tmp/cores.txt', 'r')



bla bla bla:

.. code-block:: python

    for i in f:
        print(i.strip())

.. code-block:: python

    1 - Verde
    2 - Preto
    3 - Branco



bla bla bla:

.. code-block:: python

    for i in f:
        print(i.strip())



bla bla bla:

.. code-block:: python

    f.seek(0)



bla bla bla:

.. code-block:: python

    for i in f:
        print(i.strip())

.. code-block:: console

    1 - Verde
    2 - Preto
    3 - Branco



bla bla bla:

.. code-block:: python

    f.seek(1)



bla bla bla:

.. code-block:: python

    for i in f:
        print(i.strip())

.. code-block:: console

    1 - Verde
    2 - Preto
    3 - Branco



bla bla bla:

.. code-block:: python

    f.seek(0)

.. code-block:: console

    0

.. code-block:: python

    f.read(7)

.. code-block:: console

    '1 - Ver'


.. code-block:: python

    f.read(7)

.. code-block:: console

    'de\n2 - '

.. code-block:: python

    f.read(7)

.. code-block:: console

    'Preto\n3'

.. code-block:: python

    f.read(7)

.. code-block:: console

    ' - Bran'



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: python

    f.closed

.. code-block:: console

    True



bla bla bla:

.. code-block:: python

    f = open('/tmp/cores.txt', 'w')



bla bla bla:

.. code-block:: python

    f.closed

.. code-block:: console

    False



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: bash

    cat /tmp/cores.txt



bla bla bla:

.. code-block:: python

    f = open('/tmp/cores.txt', 'w')



bla bla bla:

.. code-block:: python

    f.write('1 - Verde\n')



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: bash

    cat /tmp/cores.txt

.. code-block:: console

    1 - Verde



bla bla bla:

.. code-block:: python

    print(f.name)

.. code-block:: console

    /tmp/cores.txt



bla bla bla:

.. code-block:: python

    f = open('/tmp/cores.txt', 'a')



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: bash

    cat /tmp/cores.txt

.. code-block:: console

    1 - Verde



bla bla bla:

.. code-block:: python

    f = open('/tmp/cores.txt', 'a')



bla bla bla:

.. code-block:: python

    f.write('2 - Preto\n')



bla bla bla:

.. code-block:: python

    f.write('3 - Branco\n')



bla bla bla:

.. code-block:: python

    f.flush()



bla bla bla:

.. code-block:: bash

    cat /tmp/cores.txt

.. code-block:: console

    1 - Verde
    2 - Preto
    3 - Branco



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: python

    f = open('/tmp/cores.txt', 'r')



bla bla bla:

.. code-block:: python

    f.tell()

.. code-block:: console

    0



bla bla bla:

.. code-block:: python

    f.read()

.. code-block:: console

    '1 - Verde\n2 - Preto\n3 - Branco\n'



bla bla bla:

.. code-block:: python

    f.tell()

.. code-block:: console

    31



bla bla bla:

.. code-block:: python

    f.seek(0)

.. code-block:: console

    0



bla bla bla:

.. code-block:: python

    f.tell()

.. code-block:: console

    0



bla bla bla:

.. code-block:: python

    f.read(7)

.. code-block:: console

    '1 - Ver'



bla bla bla:

.. code-block:: python

    f.tell()

.. code-block:: console

    7



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: python

    f = open('/tmp/planetas.txt', 'w')



bla bla bla:

.. code-block:: python

    planetas = ('Saturno\n', 'Urano\n', 'Netuno\n')



bla bla bla:

.. code-block:: python

    f.writelines(planetas)



bla bla bla:

.. code-block:: python

    f.flush()



bla bla bla:

.. code-block:: bash

    cat /tmp/planetas.txt

.. code-block:: console

    Saturno
    Urano
    Netuno



bla bla bla:

.. code-block:: python

    planetas = ('Marte\n', 'Vênus\n', 'Plutão\n', 'Júpiter\n')



bla bla bla:

.. code-block:: python

    f.writelines(planetas)



bla bla bla:

.. code-block:: python

    f.close()



bla bla bla:

.. code-block:: bash

    cat /tmp/planetas.txt

.. code-block:: console

    Saturno
    Urano
    Netuno
    Marte
    Vênus
    Plutão
    Júpiter