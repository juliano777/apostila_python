Expressões vs Statements
************************

    Expressão: é algo que pode ser reduzido para um valor.

    Statement: sinônimo de comando.



exec
----

    É uma função que executa um comando (statement) passado como string.



bla bla bla:

.. code-block:: python

    exec('print(5)')  # prints 5.

.. code-block:: comando

    5

.. code-block:: python

    exec('print(5)\nprint(6)')  # prints 5{newline}6.

.. code-block:: console

    5
    6


sdsdsdsdsd:

.. code-block:: python

    exec('if True: print(6)')  # prints 6.

.. code-block:: console

    6



.. code-block:: python

    exec('5')  # does nothing and returns nothing.
    exec('x = 7')  # does nothing and returns nothing.



eval
----

    É uma função que retorna o resultado de uma expressão.



bla bla bla:

.. code-block:: python

    x = eval('5')  # x <- 5
    x = eval('%d + 6' % x)  # x <- 11
    x = eval('abs(%d)' % -100)  # x <- 100
    x = eval('x = 5')  # INVÁLIDO; atribuição não é uma expressão

.. code-block:: console

    SyntaxError: invalid syntax



wewewewe:

.. code-block:: python

    x = eval('if 1: x = 4')  # INVÁLIDO; if é um statement e não uma expressão

.. code-block:: console

    SyntaxError: invalid syntax



.. https://nedbatchelder.com/blog/201206/eval_really_is_dangerous.html

bla bla bla:

.. code-block:: python

    execfile(file)



bla bla bla:

.. code-block:: bash

    cat << EOF > /tmp/foo.py
    print('hello, world!')
    EOF



bla bla bla:

.. code-block:: bash

    python /tmp/foo.py

.. code-block:: console

    hello, world!



bla bla bla:

.. code-block:: bash

    execfile('/tmp/foo.py')

.. code-block:: console

    hello, world!


compile
-------

compile is a lower level version of exec and eval. It does not execute or evaluate your statements or expressions, but returns a code object that can do it. The modes are as follows:

    compile(string, '', 'eval') returns the code object that would have been executed had you done eval(string). Note that you cannot use statements in this mode; only a (single) expression is valid.
    compile(string, '', 'exec') returns the code object that would have been executed had you done exec(string). You can use any number of statements here.
    compile(string, '', 'single') is like the exec mode, but it will ignore everything except for the first statement. Note that an if/else statement with its results is considered a single statement.

.. http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html




.. python3.7 -mtimeit -s 'code = "a = 2; b = 3; c = a * b"' 'exec(code)'


.. python3.7 -mtimeit -s 'code = compile("a = 2; b = 3; c = a * b", "<string>", "exec")' 'exec(code)'