Dicionários

    Em Python um dicionário é uma estrutura de dados envolta por chaves cujos elementos são compostos por chave:valor e separados por vírgula.



Dicionário vazio:

> d = {}



Criação de um dicionário utilizando a função dict:

> d = dict(chave1 = 'valor2', chave2 = 1980)



Criação de um dicionário utilizando chaves:

> d = {
    'nome': 'Chiquinho',
    'sobrenome': 'da Silva',
    'email': 'chiquinho.silva@zeninguem.com',
}



Exibir o valor de uma chave do dicionário:

> d['nome']

'Chiquinho'



Loop para exibir cada par de chave e valor do dicionário:

> for k in d:
    print(f'{k} = {d[k]}')

nome = Chiquinho
sobrenome = da Silva
email = chiquinho.silva@zeninguem.com



Loop para exibir cada par de chave e valor do dicionário ordenado por chave:

> for k in sorted(d):
    print(f'{k} = {d[k]}')

email = chiquinho.silva@zeninguem.com
nome = Chiquinho
sobrenome = da Silva



Itens do dicionário:

> d.items()

dict_items([('nome', 'Chiquinho'), ('sobrenome', 'da Silva'), ('email', 'chiquinho.silva@zeninguem.com')])



Loop sobre os itens do dicionário:

> for k, v in d.items():
    print(f'{k} = {v}')

nome = Chiquinho
sobrenome = da Silva
email = chiquinho.silva@zeninguem.com



Método para exibir as chaves do dicionário:

> d.keys()

dict_keys(['nome', 'sobrenome', 'email'])



Método para exibir as chaves do dicionário:

> d.values()

dict_values(['Chiquinho', 'da Silva', 'chiquinho.silva@zeninguem.com'])



Método para limpar o dicionário:

> d.clear()



Dicionário após a execução do método clear:

> d

{}



Método update para adicionar chaves e valores:

> d.update({
    'nome': 'Chiquinho',
    'sobrenome': 'da Silva',
    'email': 'chiquinho.silva@zeninguem.com',
})



Exibindo o conteúdo do dicionário:

> d

{'email': 'chiquinho.silva@zeninguem.com',
 'nome': 'Chiquinho',
 'sobrenome': 'da Silva'}



Adicionando uma chave e valor ao dicionário:

> d.update({'data_nascimento': '28/02/1936'})



Exibindo o conteúdo do dicionário:

> d

{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '28/02/1936'}



Alterando uma chave do dicionário:

> d['data_nascimento'] = '08/02/1936'



Exibindo o conteúdo do dicionário:

> d

{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936'}



Adicionando uma nova chave e valor:

> d['cidade_origem'] = 'Cascatinha'



Exibindo o conteúdo do dicionário:

> d

{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936',
 'cidade_origem': 'Cascatinha'}



    Como chave só são aceitos tipos que utilizam hash, listas não são aceitas, mas instâncias de classes e tuplas são aceitas.



Criação de uma lista e uma tupla respectivamente:

> l = [1, 2, 3]

> t = (5, 7)



Criação de uma classe para teste:

> class Funcionario(object):
    pass



Objeto da classe Funcionário:

> f1 = Funcionario()



Tentativa de fazer uma lista ser chave do dicionário e atribuir um valor:

> d[l] = 0

TypeError: unhashable type: 'list'

    Listas são "unhashable", portanto não podem ser chaves de um dicionário.



Objeto da classe Funcionário como chave do dicionário:

> d[f1] = 'Funcionário 1'



Exibir o conteúdo do dicionário:

> d

{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936',
 'cidade_origem': 'Cascatinha',
 <__main__.Funcionario at 0x7f3769ca9c88>: 'Funcionário 1'}



Tupla como chave do dicionário e atribuir um valor:

> d[t] = 0



Exibir o conteúdo do dicionário:

> d

{'nome': 'Chiquinho',
 'sobrenome': 'da Silva',
 'email': 'chiquinho.silva@zeninguem.com',
 'data_nascimento': '08/02/1936',
 'cidade_origem': 'Cascatinha',
 <__main__.Funcionario at 0x7f3769ca9c88>: 'Funcionário 1',
 (5, 7): 0}



Tentativa de acessar uma chave inexistente:

> d[endereco]

NameError: name 'endereco' is not defined



Método get:

> d.get('nome')

'Chiquinho'

    Existe a chave "nome", então seu valor foi retornado.

> d.get('endereco')

    Não existe a chave "endereço", por isso nada foi retornado, no entanto, não foi lançada exceção.

> d.get('endereco', 'R. do Cafezal, 30')

'R. do Cafezal, 30'

    Não existe a chave "endereço", mas no método get foi passado um segundo parâmetro, o qual foi retornado, porém não houve modificação no dicionário.

> d.get('nome', 'Zezinho')

'Chiquinho'

    A chave "nome" já existia, sendo um valor diferente do valor da mesma, foi retornado o valor que pertence à chave.



Criação de um dicionário:

> carro = {
    'marca': 'Fiat',
    'modelo': '147'
}



Tentando acessar uma chave inexistente:

> carro['cor']

KeyError: 'cor'



Método get apenas para retorno:

> carro.get('cor', 'amarelo')

'amarelo'



Verificando o conteúdo do dicionário:

> carro

{'marca': 'Fiat', 'modelo': '147'}



Método setdefault:

> carro.setdefault('modelo', 'Topazio')

'147'

    Já havia uma chave "modelo", então foi retornado seu valor e não o segundo parâmetro fornecido.

> carro.setdefault('cor', 'verde')

'verde'

    Não havia uma chave "cor", agora ela e seu valor fazem parte do dicionário.



Verificando o conteúdo do dicionário:

> carro

{'cor': 'verde', 'marca': 'Fiat', 'modelo': '147'}



Método update para alterar valores de chaves pré existentes ou mesmo para adicionar novos pares de chave-valor:

> carro.update(modelo = 'Topazio', cor = 'cinza')



Verificando o conteúdo do dicionário:

> carro

{'cor': 'cinza', 'marca': 'Fiat', 'modelo': 'Topazio'}



Método pop; retira uma chave do dicionário e retorna seu valor:

> carro.pop('cor')

'cinza'



Verificando o conteúdo do dicionário:

> carro

{'marca': 'Fiat', 'modelo': 'Topazio'}



Método pop para uma chave que não existe:

> carro.pop('ano')

KeyError: 'ano'



Método pop para uma chave que não existe, mas fornecendo um valor:

> carro.pop('ano', 1981)

1981

    O dicionário continua sem a chave, mas não lançou uma exceção.



Existe a chave "marca" no dicionário?:

> 'marca' in carro

True



Existe a chave "cor" no dicionário?:

> 'cor' in carro

False



Adicionando novas chaves e seus respectivos valores:

> carro['cor'] = 'cinza'

> carro['ano'] = 1981



Verificando o conteúdo do dicionário:

> carro

{'marca': 'Fiat', 'modelo': 'Topazio', 'cor': 'cinza', 'ano': 1981}
