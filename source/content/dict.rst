Dicionários
***********

    Em Python um dicionário é uma estrutura de dados envolta por chaves cujos elementos são compostos por chave e valor e separados por vírgula.



Dicionário vazio:

.. code-block:: python

    d = {}



Criação de um dicionário utilizando a função dict:

.. code-block:: python

    d = dict(chave1 = 'valor2', chave2 = 1980)



Criação de um dicionário utilizando chaves:

.. code-block:: python

    d = {
         'nome': 'Chiquinho',
         'sobrenome': 'da Silva',
         'email': 'chiquinho.silva@zeninguem.com',
        }



Exibir o valor de uma chave do dicionário:

.. code-block:: python

    d['nome']

.. code-block:: console

    'Chiquinho'


Loop para exibir cada par de chave e valor do dicionário:

.. code-block:: python

    for k in d:
        print(f'{k} = {d[k]}')

.. code-block:: console

    nome = Chiquinho
    sobrenome = da Silva
    email = chiquinho.silva@zeninguem.com



Loop para exibir cada par de chave e valor do dicionário ordenado por chave:

.. code-block:: python

    for k in sorted(d):
        print(f'{k} = {d[k]}')

.. code-block:: console

    email = chiquinho.silva@zeninguem.com
    nome = Chiquinho
    sobrenome = da Silva



Itens do dicionário:

.. code-block:: python

    d.items()

.. code-block:: console

    dict_items([('nome', 'Chiquinho'), ('sobrenome', 'da Silva'), ('email', 'chiquinho.silva@zeninguem.com')])




Loop sobre os itens do dicionário:

.. code-block:: python

    for k, v in d.items():
        print(f'{k} = {v}')

.. code-block:: console

    nome = Chiquinho
    sobrenome = da Silva
    email = chiquinho.silva@zeninguem.com



Método para exibir as chaves do dicionário:

.. code-block:: python

    d.keys()

.. code-block:: console

    dict_keys(['nome', 'sobrenome', 'email'])



Método para exibir os valores do dicionário:

.. code-block:: python

    d.values()

.. code-block:: console

    dict_values(['Chiquinho', 'da Silva', 'chiquinho.silva@zeninguem.com'])



Método para limpar o dicionário:

.. code-block:: python

    d.clear()



Dicionário após a execução do método clear:

.. code-block:: python

    d

.. code-block:: console

    {}



Método update para adicionar chaves e valores:

.. code-block:: python

    d.update({
              'nome': 'Chiquinho',
              'sobrenome': 'da Silva',
              'email': 'chiquinho.silva@zeninguem.com',
             }
            )



Exibindo o conteúdo do dicionário:

.. code-block:: python

    d

.. code-block:: console

    {'email': 'chiquinho.silva@zeninguem.com',
     'nome': 'Chiquinho',
     'sobrenome': 'da Silva'}



Adicionando uma chave e valor ao dicionário:

.. code-block:: python

    d.update({'data_nascimento': '28/02/1936'})



Exibindo o conteúdo do dicionário:

.. code-block:: python

    d

.. code-block:: console

    {'nome': 'Chiquinho',
     'sobrenome': 'da Silva',
     'email': 'chiquinho.silva@zeninguem.com',
     'data_nascimento': '28/02/1936'}



Alterando uma chave do dicionário:

.. code-block:: python

    d['data_nascimento'] = '08/02/1936'



Exibindo o conteúdo do dicionário:

.. code-block:: python

    d

.. code-block:: console

    {'nome': 'Chiquinho',
     'sobrenome': 'da Silva',
     'email': 'chiquinho.silva@zeninguem.com',
     'data_nascimento': '08/02/1936'}



Adicionando uma nova chave e valor:

.. code-block:: python

    d['cidade_origem'] = 'Cascatinha'


Exibindo o conteúdo do dicionário:

.. code-block:: python

    d

.. code-block:: console

    {'nome': 'Chiquinho',
     'sobrenome': 'da Silva',
     'email': 'chiquinho.silva@zeninguem.com',
     'data_nascimento': '08/02/1936',
     'cidade_origem': 'Cascatinha'}

Como chave só são aceitos tipos que utilizam hash, listas não são aceitas, mas
instâncias de classes e tuplas são aceitas.



Criação de uma lista e uma tupla respectivamente:

.. code-block:: python

    l = [1, 2, 3]
    t = (5, 7)



Criação de uma classe para teste:

.. code-block:: python

    class Funcionario(object):
        pass



Objeto da classe Funcionário:

.. code-block:: python

    f1 = Funcionario()



Tentativa de fazer uma lista ser chave do dicionário e atribuir um valor:

.. code-block:: python

    d[l] = 0

.. code-block:: console

    TypeError: unhashable type: 'list'

Listas são "unhashable", portanto não podem ser chaves de um dicionário.



Objeto da classe Funcionário como chave do dicionário:

.. code-block:: python

    d[f1] = 'Funcionário 1'


Exibir o conteúdo do dicionário:

.. code-block:: python

    d

.. code-block:: console

    {'nome': 'Chiquinho',
     'sobrenome': 'da Silva',
     'email': 'chiquinho.silva@zeninguem.com',
     'data_nascimento': '08/02/1936',
     'cidade_origem': 'Cascatinha',
     <__main__.Funcionario at 0x7f3769ca9c88>: 'Funcionário 1'}



Tupla como chave do dicionário e atribuir um valor:

.. code-block:: python

    d[t] = 0



Exibir o conteúdo do dicionário:

.. code-block:: python

    d

.. code-block:: console

    {'nome': 'Chiquinho',
     'sobrenome': 'da Silva',
     'email': 'chiquinho.silva@zeninguem.com',
     'data_nascimento': '08/02/1936',
     'cidade_origem': 'Cascatinha',
     <__main__.Funcionario at 0x7f3769ca9c88>: 'Funcionário 1',
     (5, 7): 0}



Tentativa de acessar uma chave inexistente:

.. code-block:: python

    d[endereco]

.. code-block:: console

    NameError: name 'endereco' is not defined



Método get:

.. code-block:: python

    d.get('nome')

.. code-block:: console

    'Chiquinho'

Existe a chave "nome", então seu valor foi retornado.

.. code-block:: python

    d.get('endereco')

Não existe a chave "endereço", por isso nada foi retornado, no entanto, não
foi lançada exceção.

.. code-block:: python

    d.get('endereco', 'R. do Cafezal, 30')

.. code-block:: console

    'R. do Cafezal, 30'

Não existe a chave "endereço", mas no método get foi passado um segundo
parâmetro, o qual foi retornado, porém não houve modificação no dicionário.

.. code-block:: python

    d.get('nome', 'Zezinho')

.. code-block:: console

    'Chiquinho'

A chave "nome" já existia, sendo um valor diferente do valor da mesma, foi
retornado o valor que pertence à chave.



Criação de um dicionário:

.. code-block:: python

    carro = {
             'marca': 'Fiat',
             'modelo': '147'
            }



Tentando acessar uma chave inexistente:

.. code-block:: python

    carro['cor']

.. code-block:: console

    KeyError: 'cor'



Método get apenas para retorno:

.. code-block:: python

    carro.get('cor', 'amarelo')

.. code-block:: console

    'amarelo'



Verificando o conteúdo do dicionário:

.. code-block:: python

    carro

.. code-block:: console

    {'marca': 'Fiat', 'modelo': '147'}



Método setdefault:

.. code-block:: python

    carro.setdefault('modelo', 'Topazio')

.. code-block:: console

    '147'

Já havia uma chave "modelo", então foi retornado seu valor e não o segundo
parâmetro fornecido.



.. code-block:: python

    carro.setdefault('cor', 'verde')

.. code-block:: console

    'verde'

Não havia uma chave "cor", agora ela e seu valor fazem parte do dicionário.



Verificando o conteúdo do dicionário:

.. code-block:: python

    carro

.. code-block:: console

    {'cor': 'verde', 'marca': 'Fiat', 'modelo': '147'}



Método update para alterar valores de chaves pré existentes ou mesmo para
adicionar novos pares de chave-valor:

.. code-block:: python

    carro.update(modelo = 'Topazio', cor = 'cinza')


Verificando o conteúdo do dicionário:

.. code-block:: python

    carro

.. code-block:: console

    {'cor': 'cinza', 'marca': 'Fiat', 'modelo': 'Topazio'}



Método pop; retira uma chave do dicionário e retorna seu valor:

.. code-block:: python

    carro.pop('cor')

.. code-block:: console

    'cinza'



Verificando o conteúdo do dicionário:

.. code-block:: python

    carro

.. code-block:: console

    {'marca': 'Fiat', 'modelo': 'Topazio'}



Método pop para uma chave que não existe:

.. code-block:: python

    carro.pop('ano')

.. code-block:: console

    KeyError: 'ano'



Método pop para uma chave que não existe, mas fornecendo um valor:

.. code-block:: python

    carro.pop('ano', 1981)

.. code-block:: console

    1981

O dicionário continua sem a chave, mas não lançou uma exceção.



Existe a chave "marca" no dicionário?:

.. code-block:: python

    'marca' in carro

.. code-block:: console

    True



Existe a chave "cor" no dicionário?:

.. code-block:: python

    'cor' in carro

.. code-block:: console

    False


Adicionando novas chaves e seus respectivos valores:

.. code-block:: python

    carro['cor'] = 'cinza'
    carro['ano'] = 1981



Verificando o conteúdo do dicionário:

.. code-block:: python

    carro

.. code-block:: console

    {'marca': 'Fiat', 'modelo': 'Topazio', 'cor': 'cinza', 'ano': 1981}
