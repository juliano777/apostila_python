'''
Use py.test test_pytest.py
'''

def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x - 1)

def e_par(x):
    if x % 2 == 0:
        return True
    return False

def test_fatorial():
    assert fatorial(0) == 1

def test_par():
    assert e_par(8)
