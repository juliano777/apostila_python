# with

O comando `with` é usado para encapsular a execução de um bloco com métodos
definidos por um gerenciador de contexto.  
  
Criação de um arquivo via *shell* do sistema operacional:

``` bash
cat << EOF > /tmp/numbers.txt
1
2
3
EOF
```

``` python
# Abrir o arquivo em modo leitura
f = open('/tmp/numbers.txt', 'r')

# Loop para ler as linhas
for line in f:
    print(int(line))

# Fecha o arquivo:
f.close()
```

``` console
1
2
3
```

``` python
# O arquivo foi fechado?
print(f.closed)
```

``` console
True
```

``` python
# Criar um novo arquivo
f = open('/tmp/numbers.txt', 'r')

# Loop para ler as linhas do arquivo
for line in f:
    print(int(line))
f.close()
print(f.closed)
```

``` console
1
2

ValueError: invalid literal for int() with base 10: 'three\n'
```

Bla bla bla:

``` python
# 
f.closed
```

``` console
False
```

Bla bla bla:

``` python
# 
f.close()
f.closed
```

``` console
True
```

Bla bla bla:

``` python
try:
    f = open('/tmp/numbers_str.txt', 'r')
    for line in f:
        print(int(line))
except ValueError: 
    print('Ops... Isso não é um número em forma de dígitos...')
finally:
    f.close()
    print(f.closed)
```

``` console
1
2
Ops... Isso não é um número em forma de dígitos...
True
```

Bla bla bla:

``` python
with open('/tmp/numbers.txt', 'r') as f:
    for line in f:
        print(int(line))
print(f.closed)
```

``` console
1
2
3
True
```

Bla bla bla:

``` python
try:
    with open('/tmp/numbers_str.txt', 'r') as f:
        for line in f:
            print(int(line))
except ValueError:
    print('Ops... Isso não é um número em forma de dígitos...')
finally:
    print(f.closed)
```

``` console
1
2
Ops... Isso não é um número em forma de dígitos...
True
```

Exemplo de with com conexão a uma base de dados PostgreSQL:

``` python
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
```

``` console
===== __enter__ =====

Hello, World!

===== __exit__ =====
```

``` python
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
```
