$ vim /tmp/test_pytest.py


#=============================================================================

# Função fatorial
def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1)

# Função que testa se um número é par
def e_par(x):
    if x % 2 == 0:
        return True
    return False

# Função para testar a função fatorial
def test_fatorial():
    assert fatorial(0) == 1

# Função para testar a função e_par
def test_par():
    assert e_par(8)

#=============================================================================

$ py.test /tmp/test_pytest.py

================================================= test session starts =================================================
platform linux -- Python 3.4.3+, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
rootdir: /tmp, inifile: 
collected 2 items 

../../tmp/test_pytest.py .F

====================================================== FAILURES =======================================================
______________________________________________________ test_par _______________________________________________________

    def test_par():
>       assert e_par(8)
E       assert e_par(8)

/tmp/test_pytest.py:19: AssertionError
========================================= 1 failed, 1 passed in 0.01 seconds ==========================================

$ vim /tmp/test_pytest.py


#=============================================================================

# Função fatorial
def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1)

# Função que testa se um número é par
def e_par(x):
    if x % 2 == 0:
        return True
    return False

# Função para testar a função fatorial
def test_fatorial():
    assert fatorial(0) == 1

# Função para testar a função e_par
def test_par():
    assert e_par(8)

#=============================================================================

$ py.test /tmp/test_pytest.py

================================================= test session starts =================================================
platform linux -- Python 3.4.3+, pytest-2.8.7, py-1.4.31, pluggy-0.3.1
rootdir: /tmp, inifile: 
collected 2 items 

../../tmp/test_pytest.py ..

============================================== 2 passed in 0.00 seconds ===============================================

