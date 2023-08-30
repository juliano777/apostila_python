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



Supondo que o arquivo não exista, criação do mesmo para leitura e escrita:

.. code-block:: python

    f = open('/tmp/foo.txt', 'w+')



Verificando o tipo de f:

.. code-block:: python

    type(f)

.. code-block:: console

    _io.TextIOWrapper



Escrevendo no arquivo com a função print:

.. code-block:: python

    print('Teste de escrita em arquivo', file=f)



Uma linha em branco:

.. code-block:: python

    print(' ', file=f)



Mais uma linha...:

.. code-block:: python

    print('Uma linha qualquer', file=f)



Fechando o objeto e aplicando todas as escritas feitas:

.. code-block:: python

    f.close()



Reabrindo o arquivo para somente leitura:

.. code-block:: python

    f = open('/tmp/foo.txt', 'r')



Imprimir o arquivo em tela linha por linha:

.. code-block:: python

    for line in f:
        print(line.strip('\n'))



Fechamento de arquivo:

.. code-block:: python

    f.close()



No shell do sistema operacional usar o recurso heredoc para criar linhas em um novo arquivo:

.. code-block:: bash

    cat << EOF > /tmp/linhas.txt
    linha_1
    linha_2
    linha_3
    EOF



Exibir as linhas:

.. code-block:: bash

    cat /tmp/linhas.txt

.. code-block:: console

    linha_1
    linha_2
    linha_3



Em um shell Python abrir o arquivo:

.. code-block:: python

    f = open('/tmp/linhas.txt')



Método readline:

.. code-block:: python

    f.readline()

.. code-block:: console

    'linha_1\n'



Método split na saída do método readline (3X):

.. code-block:: python

    f.readline().split()

.. code-block:: console

    ['linha_2']


.. code-block:: console

    ['linha_3']


.. code-block:: console

    []

|   O método readline interagiu para cada linha retornando-a até não ter mais nada a ler no arquivo.    



Fechando o arquivo:

.. code-block:: python

    f.close()



Reabrindo o arquivo:

.. code-block:: python

    f = open('/tmp/linhas.txt')



Método readlines:

.. code-block:: python

    f.readlines()

.. code-block:: console

    ['linha_1\n', 'linha_2\n', 'linha_3\n']

|   O método readlines retorna cada linha do arquivo como um elemento de uma lista.    



Fechando o arquivo:

.. code-block:: python

    f.close()



Criar um script Python cujo comportamento é o mesmo do utilitário shell cat:

.. code-block:: bash

    vim /tmp/cat.py



Código Python:

.. code-block:: python

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



Tornar o script executável:

.. code-block:: bash

    chmod +x /tmp/cat.py



Teste do script:

.. code-block:: bash

    /tmp/cat.py /tmp/linhas.txt

.. code-block:: console

    linha_1
    linha_2
    linha_3



Novo arquivo criado via shell do sistema operacional:

.. code-block:: bash

    cat << EOF > /tmp/cores.txt
    1 - Verde
    2 - Preto
    3 - Branco
    EOF



Abrir o arquivo em modo somente leitura:

.. code-block:: python

    f = open('/tmp/cores.txt', 'r')



Um simples loop for sobre o arquivo:

.. code-block:: python

    for i in f:
        print(i.strip())

.. code-block:: python

    1 - Verde
    2 - Preto
    3 - Branco



Nova execução do loop:

.. code-block:: python

    for i in f:
        print(i.strip())



Método seek; posição 0 do cursor:

.. code-block:: python

    f.seek(0)



Nova execução do loop:

.. code-block:: python

    for i in f:
        print(i.strip())

.. code-block:: console

    1 - Verde
    2 - Preto
    3 - Branco



Posição 1:

.. code-block:: python

    f.seek(1)



Nova execução do loop:

.. code-block:: python

    for i in f:
        print(i.strip())

.. code-block:: console

    - Verde
    2 - Preto
    3 - Branco



Posição 0 (zero) do cursor:

.. code-block:: python

    f.seek(0)



Lê as 7 (sete) primeiras posições:

.. code-block:: python

    f.read(7)

.. code-block:: console

    '1 - Ver'



Ler as próximas 7 (sete) posições (repetir):

.. code-block:: python

    f.read(7)

.. code-block:: console

    'de\n2 - '

.. code-block:: console

    'Preto\n3'


.. code-block:: console

    ' - Bran'



Fechar o arquivo:

.. code-block:: python

    f.close()



Verificar se o arquivo está fechado como o atributo closed:

.. code-block:: python

    f.closed

.. code-block:: console

    True



Abrir o arquivo como escrita:

.. code-block:: python

    f = open('/tmp/cores.txt', 'w')



Verificar se o arquivo está fechado como o atributo closed:

.. code-block:: python

    f.closed

.. code-block:: console

    False



Fechar o arquivo:

.. code-block:: python

    f.close()



Verificar o conteúdo do arquivo via shell do sistema operacional:

.. code-block:: bash

    cat /tmp/cores.txt



Abrir p arquivo como escrita:

.. code-block:: python

    f = open('/tmp/cores.txt', 'w')



Escrever no arquivo:

.. code-block:: python

    f.write('1 - Verde\n')



Fechar o arquivo:

.. code-block:: python

    f.close()



Verificar o conteúdo do arquivo via shell do sistema operacional:

.. code-block:: bash

    cat /tmp/cores.txt

.. code-block:: console

    1 - Verde

|   Todo o conteúdo foi substituído por essa linha...    



Exibir a localização do arquivo:

.. code-block:: python

    print(f.name)

.. code-block:: console

    /tmp/cores.txt



Abrir o arquivo em modo append:

.. code-block:: python

    f = open('/tmp/cores.txt', 'a')



Adicionar novas linhas ao arquivo:

.. code-block:: python

    f.write('2 - Preto\n')
    f.write('3 - Branco\n')



Efetivar a escrita no arquivo sem fechá-lo:

.. code-block:: python

    f.flush()



Verificar o conteúdo do arquivo via shell do sistema operacional:

.. code-block:: bash

    cat /tmp/cores.txt

.. code-block:: console

    1 - Verde
    2 - Preto
    3 - Branco



Fechar o arquivo:

.. code-block:: python

    f.close()



Abrir o arquivo em modo leitura:

.. code-block:: python

    f = open('/tmp/cores.txt', 'r')



Método tell; retorna a posição atual:

.. code-block:: python

    f.tell()

.. code-block:: console

    0



Método read:

.. code-block:: python

    f.read()

.. code-block:: console

    '1 - Verde\n2 - Preto\n3 - Branco\n'



Veriricando a atual posição:

.. code-block:: python

    f.tell()

.. code-block:: console

    31



Método seek recoloca o cursor na posição 0 (zero):

.. code-block:: python

    f.seek(0)

.. code-block:: console

    0



Método tell confirma:

.. code-block:: python

    f.tell()

.. code-block:: console

    0



Ler 7 (sete) posições adiante:

.. code-block:: python

    f.read(7)

.. code-block:: console

    '1 - Ver'



Método tell:

.. code-block:: python

    f.tell()

.. code-block:: console

    7



Fechar o arquivo:

.. code-block:: python

    f.close()



Criar um novo arquivo como escrita:

.. code-block:: python

    f = open('/tmp/planetas.txt', 'w')



Tupla com 3 (três) elementos:

.. code-block:: python

    planetas = ('Saturno\n', 'Urano\n', 'Netuno\n')



Escreve linhas no arquivo com os elementos da tupla:

.. code-block:: python

    f.writelines(planetas)



Efetiva a escrita:

.. code-block:: python

    f.flush()



Verificando o conteúdo do arquivo via shell do sistema operacional:

.. code-block:: bash

    cat /tmp/planetas.txt

.. code-block:: console

    Saturno
    Urano
    Netuno



Redefinindo a tupla com outros elementos:

.. code-block:: python

    planetas = ('Marte\n', 'Vênus\n', 'Plutão\n', 'Júpiter\n')



Escrevendo (adicionando) linhas:

.. code-block:: python

    f.writelines(planetas)



Fechar o arquivo:

.. code-block:: python

    f.close()



Verificando o conteúdo do arquivo via shell do sistema operacional:

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