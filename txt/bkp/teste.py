#_*_ encoding: utf-8 _*_

import time

''' Fibonacci function '''
def fibo(n):
    if (n < 2): return n
    else:
        return fibo(n - 1) + fibo(n - 2)


''' Memoize function '''
def memoize(f):
    # dictionary
    mem = {}

    ''' Helper function '''
    def memoizer(*param):
        key = repr(param)
        if not key in mem:
            mem[key] = f(*param)
        return mem[key]

    return memoizer

# Start time
t1 = time.time()

# Loop 
for i in xrange(35):
    print('fib(%s) = %s' % (i, fibo(i)))

# End time
t2 = time.time()

# Total time
print('Tempo de execução: %.3fs' % (t2 - t1))

# Take a pause
raw_input('Pressione <ENTER> para continuar\n')

# Memoization of fibo (closure)
fibo = memoize(fibo)

# Start time
t1 = time.time()

# loop after memoization
for i in xrange(40):
    print('fib(%s) = %s' % (i, fibo(i)))

# End time
t2 = time.time()

# Total time
print('Tempo de execução: %.3fs' % (t2 - t1))
