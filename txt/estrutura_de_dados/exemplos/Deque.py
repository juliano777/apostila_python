# _*_ encoding: utf-8 _*_

from SQD import SQD


class Deque(SQD):

    @SQD.pop
    def pop_first(self):
        return self.elements.pop(0)

    @SQD.pop
    def pop_last(self):
        return self.elements.pop(-1)

    @SQD.push
    def push_first(self, x):
        self.elements.insert(0, x)

    @SQD.push
    def push_last(self, x):
        self.elements.append(x)

    # Métodos herdados a serem anulados

    def pop(self):
        print('Use pop_first ou pop_last')

    def push(self):
        print('Use push_first ou push_last')

d = Deque()

for i in range(1, 10):
    d.push_last(i)
