with
****


	É usado para encapsular a execução de um bloco com métodos definidos por um gerenciador de contexto. 

.. code-block:: bash

    # 
    $ cat << EOF > /tmp/numbers.txt
    1
    2
    3
    EOF


    #     
    $ cat << EOF > /tmp/numbers_str.txt
    1
    2
    three
    EOF



.. code-block:: python

    # Abrir o arquivo em modo leitura:    
    f = open('/tmp/numbers.txt', 'r')

    # Loop:
    for line in f:
        print(int(line))

    # Fecha o arquivo:
    f.close()

.. code-block:: console

    1
    2
    3

        

.. code-block:: python

    # O arquivo foi fechado?:
    print(f.closed)

.. code-block:: console

    True


.. code-block:: python

    # 
    f = open('/tmp/numbers_str.txt', 'r')
    for line in f:
        print(int(line))
    f.close()
    print(f.closed)



.. code-block:: console

    1
    2

    ValueError: invalid literal for int() with base 10: 'three\n'

.. code-block:: python

    # 
    f.closed

.. code-block:: console

    False

.. code-block:: python

    # 
    f.close()
    f.closed

.. code-block:: console

    True

.. code-block:: python

    # 
    try:
        f = open('/tmp/numbers_str.txt', 'r')
        for line in f:
            print(int(line))
    except ValueError: 
        print('Ops... Isso não é um número em forma de dígitos...')
    finally:
        f.close()
        print(f.closed)

.. code-block:: console

    1
    2
    Ops... Isso não é um número em forma de dígitos...
    True


.. code-block:: python

    # 
    with open('/tmp/numbers.txt', 'r') as f:
        for line in f:
            print(int(line))
    print(f.closed)

.. code-block:: console

    1
    2
    3
    True


.. code-block:: python

    # 
    try:
        with open('/tmp/numbers_str.txt', 'r') as f:
            for line in f:
                print(int(line))
    except ValueError:
        print('Ops... Isso não é um número em forma de dígitos...')
    finally:
        print(f.closed)

.. code-block:: console

    1
    2
    Ops... Isso não é um número em forma de dígitos...
    True




.. code-block:: python
    
    import psycopg2

    # Parâmetros de conexão
    PGHOST = 'localhost'
    PGDB = 'postgres'
    PGPORT = 5432
    PGUSER = 'postgres'
    PGPASS = '123'
    APPLICATION_NAME = 'python'

    # Máscara da string de conexão
    str_con = f'''
              host={PGHOST}
              dbname={PGDB}
              port={PGPORT}
              user={PGUSER}
              password={PGPASS}
              application_name={APPLICATION_NAME}
              '''

    str_sql = "SELECT 'Teste...';"


    class PgConnection(object):
        def __init__(self, str_con, str_sql):
            self.str_con = str_con
            self.str_sql = str_sql


        def __enter__(self):
            print('===== __enter__ =====\n')
            self.conn = psycopg2.connect(str_con)
            cursor = self.conn.cursor()
            cursor.execute(str_sql)
            self.data = cursor.fetchone()
            return self.data

        def __exit__(self, type, value, traceback):
            print('\n===== __exit__ =====')
            self.conn.close()
            return 0


    with PgConnection(str_con, str_sql) as x:
        print(x[0])


.. code-block:: console

    ===== __enter__ =====

    Teste...

    ===== __exit__ =====