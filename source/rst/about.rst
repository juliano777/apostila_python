Sobre Python
************

O que é Python
--------------

	Python é uma linguagem de programação criada pelo holandês Guido van Rossum no começo dos anos 90 na Stichting Mathematisch Centrum (http://www.cwi.nl/), na Holanda, com o objetivo de ser uma sucessora de uma linguagem chamada ABC.
	O nome linguagem foi inspirado na série humorística Monty Python's Flying Circus, do grupo humorístico britânico Monty Python. 
	É muito atrativa para desenvolvimento ágil de aplicações.

	Site oficial: www.python.org
	Site da comunidade brasileira: www.python.org.br

Características
~~~~~~~~~~~~~~~

Linguagem de altíssimo nível;
Fácil de aprender;
Simples;
Objetiva;
Preza pela legibilidade;
Case sensitive;
Mutiparadigma: orientada a objeto e procedural;
Interpretada;
Compilada (transparente ao usuário);
Tipagem forte;
Tipagem dinâmica;
Suporte a módulos e packages encorajando modularidade e reúso de código;
Multiplataforma (Linux, MacOS, BSDs, Windows e outros);
Não suporte sobrecarga de funções;
Blocos delimitados por endentação (ou espaços ou tabs: não misturar!);
Um comando por linha (podem ser colocados mais que um após um ";", mas não é uma saída elegante);
Possui modo interativo;
Software Livre.

Licença
~~~~~~~

	Python utiliza uma licença similar à licença BSD, a PSF License (Python Software Foundation License).
	É um tipo de licença muito permissiva e compatível com a licença GPL.
	É tão permissiva que permite ao usuário escolher em manter ou não o código-fonte aberto.
	Mesmo empresas que pegam o código-fonte de um projeto sob essa licença, quando o fecham e derivam então gerando um software proprietário, acabam colaborando com o projeto original firmando assim uma parceria em que ambos saem ganhando.
	É o mesmo tipo de licença adotado por outros projetos de software livre como: PostgreSQL, FreeBSD, OpenBSD, NetBSD.

O Interpretador Python
----------------------
	Como o próprio nome diz, é o interpretador que faz a análise sintática e executa as instruções Python.

Modo Interativo do Interpretador Python
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	O modo interativo de Python é um recurso interessante que facilita o trabalho do desenvolvedor de forma que se possa testar algo que esteja fazendo assim que o comando é finalizado.
	É um recurso muito útil para debugging, quick hacking e testes.	

Invocando o Modo Interativo do Interpretador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

	A maioria das distribuições Linux tem já o Python instalado, de forma que para ter acesso ao prompt interativo bastar digitar no terminal o comando python.
	Para sair do interpretador basta digitar o caractere de fim de arquivo (EOF - End-Of-File) (<Ctrl + D> em Unix ou <Ctrl + Z> no Windows). Também pode-se usar as funções exit() ou quit().

A Filosofia de Python
---------------------

	Há um easter egg em Python bem divertido que exprime bem a filosofia de Python, que é conhecido como The Zen Of Python.
	The Zen Of Python é a PEP 20, PEP que significa Python Enhancement Proposals (Propostas de Melhoria para Python).
	Para visualizar esse easter egg basta que no shell interativo dê o seguinte comando:

.. code-block:: python
    
    import this

.. code-block:: console

    The Zen of Python, by Tim Peters

    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!

Tradução:

.. code-block:: console


    O Zen de Python, por Tim Peters

    Bonito é melhor do que feio.
    Explícito é melhor do que implícito.
    Simples é melhor do que complexo.
    Complexo é melhor do que complicado.
    Plano é melhor do que aninhado.
    Disperso é melhor do que denso.
    Legibilidade conta.
    Casos especiais não são especiais o bastante para quebrar as regras.
    Embora a praticidade vença a pureza.
    Erros não devem passar silenciosamente.
    A não ser que sejam explicitamente silenciados.
    Diante a ambigüidade, recuse a tentação de adivinhar.
    Deve haver um-- e preferencialmente apenas um --modo óbvio de fazer isso.
    Embora a maneira não seja óbvia à primeira vista, a menos que seja holandês.
    Agora é melhor do que nunca.
    Embora nunca é muitas vezes melhor do que *agora* mesmo
    Se a implementação é difícil de explicar, é uma má idéia.
    Se a implementação é fácil de explicar, deve ser uma boa idéia.
    Namespaces são uma idéia fantástica – vamos fazer mais desses!



Bytecode
--------

	Formato binário multiplataforma resultante da compilação de um código Python.


Criação de estrutura de diretórios para teste de pacote e bytecode:

.. code-block:: bash

    mkdir -p /tmp/python/PacoteA/PacoteA1

Editar o módulo "Modulo1" que está dentro do pacote "PacoteA":

.. code-block:: bash

    vim /tmp/python/PacoteA/Modulo1.py
    

.. code-block:: python

    def funcao():
        print('Hello World!!!')

Editar o módulo "Modulo1" que está dentro do pacote "PacoteA":

.. code-block:: bash

    vim /tmp/python/PacoteA/PacoteA1/Modulo2.py


.. code-block:: python
    
    def funcao(numero):
        print(numero ** 3)

vim /tmp/python/foo.py

.. code-block:: python

    #!/usr/bin/env python
    #_*_ encoding: utf-8 _*_

    from PacoteA.Modulo1 import funcao
    from PacoteA.PacoteA1 import Modulo2

    print('\nAtenção!!!\n')
    print('O teste vai começar...\n')

    funcao()

    Modulo2.funcao(3)

$ python /tmp/python/foo.py 

Atenção!!!

O teste vai começar...

Hello World!!!
27

Quando um módulo é carregado pela primeira vez ou se seu código é mais novo do que o  arquivo binário ele é compilado e então gera ou gera novamente o arquivo binário .pyc.

ls /tmp/python/PacoteA/
__init__.py  __init__.pyc  Modulo1.py  Modulo1.pyc  PacoteA1

ls /tmp/python/PacoteA/PacoteA1/
__init__.py  __init__.pyc  Modulo2.py  Modulo2.pyc

file /tmp/python/PacoteA/Modulo1.pyc
/tmp/python/PacoteA/Modulo1.pyc: python 2.7 byte-compiled