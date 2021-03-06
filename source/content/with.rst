with
****

|   O comando with é usado para encapsular a execução de um bloco com métodos definidos por um gerenciador de contexto.



Criação de um arquivo via shell do sistema operacional:

.. code-block:: bash

    cat << EOF > /tmp/numbers.txt
    1
    2
    3
    EOF



Abrir o arquivo em modo leitura:

.. code-block:: python

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

        

O arquivo foi fechado?:

.. code-block:: python

    print(f.closed)

.. code-block:: console

    True



Bla bla bla:

.. code-block:: python

    f = open('/tmp/numbers_str.txt', 'r')
    for line in f:
        print(int(line))
    f.close()
    print(f.closed)

.. code-block:: console

    1
    2

    ValueError: invalid literal for int() with base 10: 'three\n'



Bla bla bla:

.. code-block:: python

    # 
    f.closed

.. code-block:: console

    False



Bla bla bla:

.. code-block:: python

    # 
    f.close()
    f.closed

.. code-block:: console

    True



Bla bla bla:

.. code-block:: python

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



Bla bla bla:

.. code-block:: python

    with open('/tmp/numbers.txt', 'r') as f:
        for line in f:
            print(int(line))
    print(f.closed)

.. code-block:: console

    1
    2
    3
    True



Bla bla bla:

.. code-block:: python

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



Exemplo de with com conexão a uma base de dados PostgreSQL:

.. code-block:: python
    
    from psycopg2 import connect as pg_conn

    # Parâmetros de conexão
    PGHOST = 'localhost'
    PGDB = 'postgres'
    PGPORT = 5432
    PGUSER = 'postgres'
    PGPASS = '123'
    APPLICATION_NAME = 'python'

    # String de conexão
    CONN = f'''
              host={PGHOST}
              dbname={PGDB}
              port={PGPORT}
              user={PGUSER}
              password={PGPASS}
              application_name={APPLICATION_NAME}
              '''

    # String SQL
    SQL = "SELECT 'Hello, World!';"

    # Criação de uma classe para conexão ao banco com with.
    # Através dela se conecta à base, executa comando(s) SQL e fecha a conexão
    # ao banco.

    class PgConnection(object):

        def __init__(self, conn, sql):
            self.conn = conn
            self.sql = sql

        def __enter__(self):
            print('===== __enter__ =====\n')
            self.conn = pg_conn(self.conn)
            cursor = self.conn.cursor()
            cursor.execute(self.sql)
            self.data = cursor.fetchone()
            return self.data

        def __exit__(self, type, value, traceback):
            print('\n===== __exit__ =====')
            self.conn.close()
            return 0


    with PgConnection(CONN, SQL) as x:
        print(x[0])


.. code-block:: console

    ===== __enter__ =====

    Hello, World!

    ===== __exit__ =====
    
    
.. code-block:: python

    class DBConnection(object):
    '''
    Classe para conexão de bancos PostgreSQL ou MySQL/MariaDB

    Parâmetros:

    - db_connector: Função connect do driver;
    - conn_params: Dicionário de parâmetros de conexão;
    - sql: String de statements para execução.    
    '''

    def __init__(self, db_connector, conn_params: dict, sql: str):
        self.db_connector = db_connector
        self.conn_params = conn_params
        self.sql = sql

    def __enter__(self):
        self.conn = self.db_connector(**self.conn_params)
        cursor = self.conn.cursor()
        cursor.execute(self.sql)
        self.data = cursor.fetchall()
        return self.data

    def __exit__(self, type, value, traceback):
        self.conn.close()
        return 0    
