# Dicionário

Em Python um dicionário é uma estrutura de dados envolta por chaves cujos
elementos são compostos por chave e valor e separados por vírgula.  
Muito similar a [JSON](https://www.json.org).  
  
Dicionário vazio:

``` python
d = {}
```

Criação de um dicionário utilizando a função `dict()`:

``` python
d = dict(chave1 = 'valor2', chave2 = 1980)
```

Criação de um dicionário utilizando chaves:

``` python
d = {
     'nome': 'Chiquinho',
     'sobrenome': 'da Silva',
     'email': 'chiquinho.silva@zeninguem.com',
    }
```

Exibir o valor de uma chave do dicionário:

``` python
d['nome']
```

``` console
'Chiquinho'
```

Loop para exibir cada par de chave e valor do dicionário:

``` python
for k in d:
    print(f'{k} = {d[k]}')
```

``` console
nome = Chiquinho
sobrenome = da Silva
email = chiquinho.silva@zeninguem.com
```

Loop para exibir cada par de chave e valor do dicionário ordenado por
chave:

``` python
for k in sorted(d):
    print(f'{k} = {d[k]}')
```

``` console
email = chiquinho.silva@zeninguem.com
nome = Chiquinho
sobrenome = da Silva
```

Itens do dicionário:

``` python
d.items()
```

``` console
dict_items([('nome', 'Chiquinho'), ('sobrenome', 'da Silva'), ('email', 'chiquinho.silva@zeninguem.com')])
```

Loop sobre os itens do dicionário:

``` python
for k, v in d.items():
    print(f'{k} = {v}')
```

``` console
nome = Chiquinho
sobrenome = da Silva
email = chiquinho.silva@zeninguem.com
```

Método para exibir as chaves do dicionário:

``` python
d.keys()
```

``` console
dict_keys(['nome', 'sobrenome', 'email'])
```

Método para exibir os valores do dicionário:

``` python
d.values()
```

``` console
dict_values(['Chiquinho', 'da Silva', 'chiquinho.silva@zeninguem.com'])
```

Método para limpar o dicionário:

``` python
d.clear()
```

Dicionário após a execução do método clear:

``` python
d
```

``` console
{}
```

Método update para adicionar chaves e valores:

``` python
d.update({
          'nome': 'Chiquinho',
          'sobrenome': 'da Silva',
          'email': 'chiquinho.silva@zeninguem.com',
         }
        )
```

Exibindo o conteúdo do dicionário:

``` python
d
```

``` console
{'email': 'chiquinho.silva@zeninguem.com',
 'nome': 'Chiquinho',
 'sobrenome': 'da Silva'}
```

Adicionando uma chave e valor ao dicionário:

``` python
d.update({'data_nascimento': '28/02/1936'})
```

Exibindo o conteúdo do dicionário:

``` python
d
```

``` console
{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '28/02/1936'}
```

Alterando uma chave do dicionário:

``` python
d['data_nascimento'] = '08/02/1936'
```

Exibindo o conteúdo do dicionário:

``` python
d
```

``` console
{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936'}
```

Adicionando uma nova chave e valor:

``` python
d['cidade_origem'] = 'Cascatinha'
```

Exibindo o conteúdo do dicionário:

``` python
d
```

``` console
{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936',
 'cidade_origem': 'Cascatinha'}
```

Como chave só são aceitos tipos que utilizam hash, listas não são
aceitas, mas instâncias de classes e tuplas são aceitas.

Criação de uma lista e uma tupla respectivamente:

``` python
l = [1, 2, 3]
t = (5, 7)
```

Criação de uma classe para teste:

``` python
class Funcionario(object):
    pass
```

Objeto da classe Funcionário:

``` python
f1 = Funcionario()
```

Tentativa de fazer uma lista ser chave do dicionário e atribuir um
valor:

``` python
d[l] = 0
```

``` console
TypeError: unhashable type: 'list'
```

Listas são "*unhashable*", portanto não podem ser chaves de um dicionário.  
  
Objeto da classe `Funcionário` como chave do dicionário:

``` python
d[f1] = 'Funcionário 1'
```

Exibir o conteúdo do dicionário:

``` python
d
```

``` console
{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936',
 'cidade_origem': 'Cascatinha',
 <__main__.Funcionario at 0x7f3769ca9c88>: 'Funcionário 1'}
```

Tupla como chave do dicionário e atribuir um valor:

``` python
d[t] = 0
```

Exibir o conteúdo do dicionário:

``` python
d
```

``` console
{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936',
 'cidade_origem': 'Cascatinha',
 <__main__.Funcionario at 0x7f3769ca9c88>: 'Funcionário 1',
 (5, 7): 0}
```

Tentativa de acessar uma chave inexistente:

``` python
d[endereco]
```

``` console
NameError: name 'endereco' is not defined
```

Método get:

``` python
d.get('nome')
```

``` console
'Chiquinho'
```

Existe a chave "nome", então seu valor foi retornado.

``` python
d.get('endereco')
```

Não existe a chave "endereço", por isso nada foi retornado, no entanto, não
foi lançada exceção.

``` python
d.get('endereco', 'R. do Cafezal, 30')
```

``` console
'R. do Cafezal, 30'
```

Não existe a chave "endereço", mas no método get foi passado um segundo
parâmetro, o qual foi retornado, porém não houve modificação no dicionário.

``` python
d.get('nome', 'Zezinho')
```

``` console
'Chiquinho'
```

A chave "nome" já existia, sendo um valor diferente do valor da mesma, foi
retornado o valor que pertence à chave.

Criação de um dicionário:

``` python
carro = {
         'marca': 'Fiat',
         'modelo': '147'
        }
```

Tentando acessar uma chave inexistente:

``` python
carro['cor']
```

``` console
KeyError: 'cor'
```

Método get apenas para retorno:

``` python
carro.get('cor', 'amarelo')
```

``` console
'amarelo'
```

Verificando o conteúdo do dicionário:

``` python
carro
```

``` console
{'marca': 'Fiat', 'modelo': '147'}
```

Método setdefault:

``` python
carro.setdefault('modelo', 'Topazio')
```

``` console
'147'
```

Já havia uma chave "modelo", então foi retornado seu valor e não o segundo
parâmetro fornecido.

``` python
carro.setdefault('cor', 'verde')
```

``` console
'verde'
```

Não havia uma chave "cor", agora ela e seu valor fazem parte do dicionário.

Verificando o conteúdo do dicionário:

``` python
carro
```

``` console
{'cor': 'verde', 'marca': 'Fiat', 'modelo': '147'}
```

Método update para alterar valores de chaves pré existentes ou mesmo para
adicionar novos pares de chave-valor:

``` python
carro.update(modelo = 'Topazio', cor = 'cinza')
```

Verificando o conteúdo do dicionário:

``` python
carro
```

``` console
{'cor': 'cinza', 'marca': 'Fiat', 'modelo': 'Topazio'}
```

Método pop; retira uma chave do dicionário e retorna seu valor:

``` python
carro.pop('cor')
```

``` console
'cinza'
```

Verificando o conteúdo do dicionário:

``` python
carro
```

``` console
{'marca': 'Fiat', 'modelo': 'Topazio'}
```

Método pop para uma chave que não existe:

``` python
carro.pop('ano')
```

``` console
KeyError: 'ano'
```

Método `pop()` para uma chave que não existe, mas fornecendo um valor:

``` python
carro.pop('ano', 1981)
```

``` console
1981
```

O dicionário continua sem a chave, mas não lançou uma exceção.

Existe a chave "marca" no dicionário?:

``` python
'marca' in carro
```

``` console
True
```

Existe a chave "cor" no dicionário?:

``` python
'cor' in carro
```

``` console
False
```

Adicionando novas chaves e seus respectivos valores:

``` python
carro['cor'] = 'cinza'
carro['ano'] = 1981
```

Verificando o conteúdo do dicionário:

``` python
carro
```

``` console
{'marca': 'Fiat', 'modelo': 'Topazio', 'cor': 'cinza', 'ano': 1981}
```
