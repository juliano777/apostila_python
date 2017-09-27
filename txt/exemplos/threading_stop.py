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
