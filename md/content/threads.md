---
title: Threads
---

``` python
import threading
import time

def funcao1():
    linha = ('_' * 79)
    while (True):
        print(linha)
        time.sleep(10)

def funcao2(tempo):
    while (True):
        print('funcao2')
        time.sleep(tempo)

t1 = threading.Thread(target=funcao1, name='primeira_thread')

t2 = threading.Thread(target=funcao2, name='segunda_thread', args=(3,))

t1.start()

t2.start()
```

``` console
funcao2
funcao2
funcao2
```

``` python
t1.getName()
```

``` console
'primeira_thread'
```

E se quisermos parar uma thread?

``` python
import threading
import os
import time

class FileChecker(threading.Thread):
  def __init__(self, file_path):
    super(FileChecker, self).__init__()
    self._kill = False
    self._file_path = file_path

  def run(self):
      while (not os.path.isfile(self._file_path)):
          print("File {} not found!".format(self._file_path))
          time.sleep(5)
          if self._kill:
            break

  def stop(self):
    self._kill = True
    self.join()

t = FileChecker('/tmp/teste.txt')
t.start()

time.sleep(10)

t.stop()

print('fim')
```
